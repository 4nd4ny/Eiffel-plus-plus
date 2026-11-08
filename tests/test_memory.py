"""Contrats d'oubli : données fictives, aucune décision humaine réelle ni appel LLM."""
from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import memory

NOW = "2026-11-08T12:00:00+00:00"
POLICY = {"maintainers": ["owner"], "writers": ["worker", "peer"]}


def source(ident, text, origin="agent"):
    return {"op": "source", "id": ident, "origin": origin,
            "locator": "synthetic-test:" + ident, "text": text}


def note(ident, text, kind="hypothesis", **changes):
    value = {"op": "remember", "id": ident, "kind": kind, "source": "src-" + ident,
             "quote": text, "scope": ["*"], "depends_on": [],
             "basis": {} if kind == "requirement" else {"phase": "pilot"}, "expires_at": None}
    value.update(changes)
    return value


class MemoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.work = Path(self.temp.name)
        self.store = self.work / "memory"
        memory.init(self.store, "synthetic", POLICY)
        self.serial = 0
        self.change([source("src-R", "Préserver les données utiles.", "human"),
                     note("R", "Préserver les données utiles.", "requirement")], actor="owner")

    def change(self, ops, actor="worker"):
        proposal = memory.propose(self.store, actor, ops, "Fixture synthétique : adaptation examinée.")
        return memory.apply(self.store, proposal, memory.meta.digest(memory.meta.canonical(proposal)), actor)

    def remember(self, ident, text="Consigne temporaire synthétique.", kind="hypothesis", actor="worker", **changes):
        return self.change([source("src-" + ident, text, "human" if kind == "requirement" else "agent"),
                            note(ident, text, kind, **changes)], actor)

    def status(self, ident, op="retire", actor="worker", origin="agent"):
        self.serial += 1
        sid = "status-" + str(self.serial)
        text = "Décision synthétique : " + op + " " + ident
        return self.change([source(sid, text, origin), {"op": op, "id": ident, "source": sid, "quote": text}], actor)

    def selected(self, **kwargs):
        return memory.select(self.store, kwargs.get("scope", "task"), kwargs.get("bindings", {"phase": "pilot"}), kwargs.get("now", NOW))

    def ids(self, **kwargs):
        return {n["id"] for n in self.selected(**kwargs)["notes"]}

    def packet(self, **kwargs):
        self.serial += 1
        directory = self.work / ("packet-" + str(self.serial))
        receipt = memory.prepare(self.store, directory, "task", {"phase": "pilot"}, "Travail synthétique.", kwargs.get("now", NOW))
        return directory, receipt["packet_sha256"]

    def launch(self, directory, digest, **kwargs):
        return memory.launch_request(self.store, directory, digest, kwargs.get("scope", "task"),
                                     kwargs.get("bindings", {"phase": "pilot"}),
                                     kwargs.get("task", "Travail synthétique."), kwargs.get("now", NOW))

    def test_expiration_removes_temporary_rule_but_keeps_old_rare_requirement(self):
        self.remember("T", basis={}, expires_at="2026-11-08T11:59:00Z")
        self.assertEqual(self.ids(), {"R"})
        self.assertEqual(self.selected()["omitted"], {"T": "expired"})
        self.assertEqual(self.ids(now="2040-01-01T00:00:00Z"), {"R"})

    def test_expiration_at_exact_boundary_and_timezone_conversion(self):
        self.remember("T", basis={}, expires_at="2026-11-08T13:00:00+01:00")
        self.assertEqual(self.ids(now="2026-11-08T11:59:59Z"), {"R", "T"})
        self.assertEqual(self.ids(), {"R"})

    def test_changed_or_missing_basis_filters_hypothesis(self):
        self.remember("T")
        for values in ({}, {"phase": "production"}):
            with self.subTest(values=values):
                self.assertEqual(self.ids(bindings=values), {"R"})

    def test_requirement_basis_change_blocks_instead_of_silently_dropping_it(self):
        self.remember("R2", kind="requirement", actor="owner", basis={"schema": "v1"})
        with self.assertRaisesRegex(ValueError, "Exigences à réexaminer"):
            self.selected()
        self.assertEqual(self.ids(bindings={"schema": "v1"}), {"R", "R2"})

    def test_scope_limits_do_not_leak_temporary_instruction_to_other_task(self):
        self.remember("T", scope=["migration"])
        self.assertEqual(self.ids(), {"R"})
        self.assertEqual(self.ids(scope="migration"), {"R", "T"})

    def test_retirement_is_immediate_transitive_and_cannot_be_reactivated(self):
        self.remember("T")
        self.remember("copy", depends_on=["T"])
        self.remember("summary", depends_on=["copy"])
        old = self.packet()
        self.status("T")
        self.assertEqual(self.ids(), {"R"})
        self.assertEqual(self.selected()["omitted"]["summary"], "dependency_invalid")
        self.assertEqual(memory.recall(self.store, "T", "task", {"phase": "pilot"}, NOW), {"id": "T", "status": "retired"})
        with self.assertRaises(ValueError): self.launch(*old)
        with self.assertRaises(ValueError): self.status("T", "resolve", actor="owner")
        with self.assertRaises(ValueError):
            self.change([note("T", "Consigne temporaire synthétique.")])

    def test_inactive_text_remains_in_history_but_not_new_request_or_markdown(self):
        text = "TEMPORARY-POISON-DO-NOT-REINJECT"
        self.remember("T", text=text)
        self.status("T")
        path, anchor = self.packet()
        self.assertIn(text, (self.store / "ledger.json").read_text())
        self.assertNotIn(text, (path / "request.json").read_text())
        self.assertNotIn(text, (path / "CONTEXT.md").read_text())
        request = self.launch(path, anchor)
        self.assertEqual(request["context_mode"], "fresh")
        self.assertEqual(len(request["messages"]), 2)
        self.assertEqual({n["id"] for n in json.loads(request["messages"][1]["content"])["notes"]}, {"R"})

    def test_hypothesis_cannot_promote_itself_into_requirement(self):
        self.remember("T")
        for actor in ("worker", "owner"):
            with self.subTest(actor=actor), self.assertRaisesRegex(ValueError, "exigence exige"):
                self.change([note("forged", "Consigne temporaire synthétique.", "requirement", source="src-T")], actor)

    def test_authoritative_quote_cannot_hide_derivation_from_hypothesis(self):
        self.remember("T")
        with self.assertRaisesRegex(ValueError, "par dérivation"):
            self.remember("forged", kind="requirement", actor="owner", depends_on=["T"])

    def test_agent_cannot_claim_human_source_or_documentary_authority(self):
        for origin in ("human", "document"):
            with self.subTest(origin=origin), self.assertRaises(ValueError):
                self.change([source("forged", "Une consigne inventée.", origin)])

    def test_quotes_must_exist_and_sources_cannot_be_silently_edited(self):
        with self.assertRaisesRegex(ValueError, "Citation absente"):
            self.change([note("forged", "Une consigne inventée.", source="src-R")])
        with self.assertRaisesRegex(ValueError, "ne se réécrit"):
            self.change([source("src-R", "Nouvelle version inventée.")])

    def test_assumptions_need_explicit_reexamination_condition(self):
        with self.assertRaisesRegex(ValueError, "condition de réexamen"):
            self.remember("T", basis={})

    def test_requirements_never_expire_by_age(self):
        with self.assertRaisesRegex(ValueError, "Pas d'expiration"):
            self.remember("R2", kind="requirement", actor="owner", expires_at="2026-12-01T00:00:00Z")

    def test_challenged_requirement_blocks_only_its_applicable_scope(self):
        self.remember("R2", kind="requirement", actor="owner", scope=["migration"])
        self.status("R2", "challenge")
        self.assertEqual(self.ids(), {"R"})
        with self.assertRaisesRegex(ValueError, "Exigences à réexaminer"):
            self.ids(scope="migration")
        with self.assertRaises(ValueError): self.status("R2", "resolve")
        self.status("R2", "resolve", actor="owner", origin="human")
        self.assertEqual(self.ids(scope="migration"), {"R", "R2"})

    def test_agent_cannot_retire_requirements_or_other_agents_notes(self):
        with self.assertRaises(ValueError): self.status("R")
        self.remember("T", actor="peer")
        with self.assertRaises(ValueError): self.status("T")

    def test_requirement_retirement_needs_competent_source_even_for_maintainer(self):
        with self.assertRaisesRegex(ValueError, "source compétente"):
            self.status("R", actor="owner")
        self.status("R", actor="owner", origin="human")
        self.assertEqual(self.ids(), set())

    def test_dependency_invalidation_never_silently_drops_child_requirement(self):
        self.remember("R2", kind="requirement", actor="owner", depends_on=["R"])
        self.status("R", actor="owner", origin="human")
        with self.assertRaisesRegex(ValueError, "dependency_invalid"):
            self.selected()

    def test_future_dependency_and_unknown_fields_are_rejected(self):
        with self.assertRaises(ValueError): self.remember("T", depends_on=["T"])
        with self.assertRaises(ValueError): self.remember("T", silently_approved=True)

    def test_proposal_is_not_acceptance_and_keeps_proposer_distinct(self):
        before = memory.inspect(self.store)
        proposal = memory.propose(self.store, "worker", [source("new", "Proposition synthétique.")], "Consolidation proposée.")
        self.assertEqual(memory.inspect(self.store), before)
        memory.apply(self.store, proposal, memory.meta.digest(memory.meta.canonical(proposal)), "owner")
        event = json.loads((self.store / "ledger.json").read_text())["events"][-1]
        self.assertEqual(event["proposer"], "worker")
        self.assertEqual(event["actor"], "owner")

    def test_modified_proposal_and_stale_base_are_rejected(self):
        proposal = memory.propose(self.store, "worker", [source("new", "Proposition synthétique.")], "Consolidation.")
        anchor = memory.meta.digest(memory.meta.canonical(proposal))
        changed = deepcopy(proposal); changed["reason"] = "Autre motif."
        with self.assertRaises(ValueError): memory.apply(self.store, changed, anchor, "worker")
        self.remember("T")
        with self.assertRaisesRegex(ValueError, "Révision périmée"):
            memory.apply(self.store, proposal, anchor, "worker")

    def test_global_approval_does_not_make_agent_proposed_source_human(self):
        proposal = memory.propose(self.store, "worker", [source("invented-human", "L'agent invente une obligation.", "human")], "Consolidation à examiner.")
        with self.assertRaisesRegex(ValueError, "même approuvée globalement"):
            memory.apply(self.store, proposal, memory.meta.digest(memory.meta.canonical(proposal)), "owner")

    def test_failed_batch_is_atomic(self):
        before = (self.store / "ledger.json").read_bytes()
        with self.assertRaises(ValueError):
            self.change([source("new", "Note valide."), note("bad", "Citation absente.", source="new")])
        self.assertEqual((self.store / "ledger.json").read_bytes(), before)

    def test_two_concurrent_writers_cannot_overwrite_each_other(self):
        processes = []
        for ident in ("a", "b"):
            proposal = memory.propose(self.store, "worker", [source(ident, ident)], "Écriture concurrente synthétique.")
            path = self.work / (ident + ".json")
            path.write_bytes(memory.meta.canonical(proposal))
            anchor = memory.meta.digest(path.read_bytes())
            processes.append(subprocess.Popen([sys.executable, "-B", str(ROOT / "tools/memory.py"), "apply", str(self.store), str(path), anchor, "worker"], stdout=subprocess.PIPE, stderr=subprocess.PIPE))
        results = [p.communicate(timeout=20) for p in processes]
        self.assertEqual(sorted(p.returncode for p in processes), [0, 1], results)
        self.assertEqual(memory.inspect(self.store)["events"], 2)

    def test_changed_file_or_history_in_request_is_rejected(self):
        path, anchor = self.packet()
        value = json.loads((path / "request.json").read_text())
        value["messages"].append({"role": "assistant", "content": "Ancienne consigne."})
        (path / "request.json").write_text(json.dumps(value))
        with self.assertRaises(ValueError): self.launch(path, anchor)

    def test_reanchored_packet_cannot_omit_valid_requirement(self):
        path, _ = self.packet()
        value = json.loads((path / "request.json").read_text())
        body = json.loads(value["messages"][1]["content"]); body["notes"] = []
        value["messages"][1]["content"] = json.dumps(body)
        (path / "request.json").write_text(json.dumps(value))
        receipt = json.loads((path / "receipt.json").read_text())
        receipt["files"]["request.json"] = memory.meta.digest((path / "request.json").read_bytes())
        (path / "receipt.json").write_bytes(memory.meta.canonical(receipt))
        anchor = memory.meta.digest((path / "receipt.json").read_bytes())
        with self.assertRaisesRegex(ValueError, "incomplet"):
            self.launch(path, anchor)

    def test_pending_packet_expires_before_dispatch(self):
        self.remember("T", basis={}, expires_at="2026-11-08T12:01:00Z")
        path, anchor = self.packet()
        with self.assertRaises(ValueError): self.launch(path, anchor, now="2026-11-08T12:01:00Z")

    def test_task_scope_and_runtime_versions_are_bound_to_dispatch(self):
        path, anchor = self.packet()
        for change in ({"scope": "other"}, {"task": "Autre tâche."}, {"bindings": {"phase": "production"}}):
            with self.subTest(change=change), self.assertRaises(ValueError): self.launch(path, anchor, **change)

    def test_old_revision_anchor_detects_rollback(self):
        old = (self.store / "ledger.json").read_bytes()
        latest = self.remember("T")["revision"]
        (self.store / "ledger.json").write_bytes(old)
        with self.assertRaisesRegex(ValueError, "Révision périmée"):
            memory.inspect(self.store, latest)

    def test_duplicate_keys_symlinks_and_tampered_history_are_rejected(self):
        original = (self.store / "ledger.json").read_bytes()
        (self.store / "ledger.json").write_bytes(original.replace(b'"format":', b'"format":"fake","format":', 1))
        with self.assertRaises(ValueError): memory.inspect(self.store)
        (self.store / "ledger.json").write_bytes(original.replace("Préserver".encode(), "Supprimer".encode()))
        with self.assertRaises(ValueError): memory.inspect(self.store)
        original_path = self.work / "original.json"; original_path.write_bytes(original)
        (self.store / "ledger.json").unlink(); (self.store / "ledger.json").symlink_to(original_path)
        with self.assertRaises(ValueError): memory.inspect(self.store)

    def test_fresh_request_can_cross_process_boundary_without_raw_archive(self):
        self.remember("T", text="TEMPORARY-POISON-DO-NOT-REINJECT", expires_at="2000-01-01T00:00:00Z")
        path, anchor = self.packet()
        bindings = self.work / "bindings.json"; bindings.write_text('{"phase":"pilot"}')
        task = self.work / "task.txt"; task.write_text("Travail synthétique.")
        result = subprocess.run([sys.executable, "-B", str(ROOT / "tools/memory.py"), "request", str(self.store), str(path), "--scope", "task", "--bindings", str(bindings), "--task-file", str(task), "--packet-sha256", anchor], capture_output=True, text=True, timeout=20)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertNotIn("TEMPORARY-POISON", result.stdout)
        self.assertIn("Préserver les données utiles.", result.stdout)

    def test_cli_proposal_is_reviewable_and_never_applied_implicitly(self):
        before = memory.inspect(self.store)
        change = self.work / "change.json"
        change.write_text(json.dumps({"reason": "Fixture CLI.", "operations": [source("new", "Note de travail.")]}))
        proposal = self.work / "proposal.json"
        command = [sys.executable, "-B", str(ROOT / "tools/memory.py"), "propose", str(self.store), "worker", str(change), "--output", str(proposal)]
        result = subprocess.run(command, capture_output=True, text=True, timeout=20)
        self.assertEqual(result.returncode, 0, result.stdout)
        receipt = json.loads(result.stdout)
        self.assertFalse(receipt["applied"])
        self.assertEqual(memory.inspect(self.store), before)
        self.assertEqual(memory.meta.digest(proposal.read_bytes()), receipt["proposal_sha256"])
        result = subprocess.run([sys.executable, "-B", str(ROOT / "tools/memory.py"), "apply", str(self.store), str(proposal), receipt["proposal_sha256"], "worker"], capture_output=True, text=True, timeout=20)
        self.assertEqual(result.returncode, 0, result.stdout)
        result = subprocess.run(command, capture_output=True, text=True, timeout=20)
        self.assertEqual(result.returncode, 1, "Une proposition existante ne doit pas être remplacée.")

    def test_unknown_actor_and_other_project_packet_are_rejected(self):
        proposal = memory.propose(self.store, "stranger", [source("new", "Texte.")], "Fixture.")
        with self.assertRaisesRegex(ValueError, "sans droit"):
            memory.apply(self.store, proposal, memory.meta.digest(memory.meta.canonical(proposal)), "stranger")
        path, anchor = self.packet()
        other = self.work / "other-store"
        memory.init(other, "other-project", POLICY)
        with self.assertRaises(ValueError):
            memory.launch_request(other, path, anchor, "task", {"phase": "pilot"}, "Travail synthétique.", NOW)

    def test_public_example_preserves_requirement_and_rejects_old_context(self):
        import importlib.util
        spec = importlib.util.spec_from_file_location("memory_example", ROOT / "examples/memory-0.8.0/demo.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        result = module.demo(self.work / "demo")
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(result["requirements_preserved"], ["R1"])
        self.assertEqual(result["omitted"], {"T1": "retired"})
        self.assertFalse(result["model_called"])


if __name__ == "__main__":
    unittest.main()
