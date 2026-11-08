"""Contre-exemples de la cascade ; les avis humains sont des fixtures synthétiques."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import cascade


class CascadeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.session = self.root / "session"
        self.serial = 0

    def bundle(self, *, level=2, **changes):
        self.serial += 1
        directory = self.root / f"bundle-{self.serial}"
        directory.mkdir()
        (directory / "source.md").write_text("Besoin synthétique : préserver les octets utiles.\n")
        (directory / "evidence.txt").write_text("Observation synthétique : critère exercé sur un cas négatif.\n")
        value = {
            "level": level,
            "purpose": "Qualifier la suffisance du niveau pour le prochain travail.",
            "criteria": {"CTR-0001": "PASS"},
            "evidence": ["evidence.txt"],
            "coverage": [{"requirement": "REQ-0001", "criterion": "CTR-0001"}],
            "required_inputs": [{"id": "INPUT-0001", "status": "AVAILABLE", "source": "source.md"}],
            "blocking_unknowns": [],
            "observation": "Les mêmes obligations ont été examinées dans ce cycle.",
            "hypothesis": "Une revue stable permet de préciser le niveau suivant.",
            "change": "Conserver les critères et examiner leurs limites.",
            "novelty": [],
            "stability_probe": "Rejouer le contre-exemple et rechercher une exigence encore inconnue.",
            "limits": ["Fixture sans preuve métier ni décision humaine réelle."],
        }
        value.update(changes)
        (directory / "cycle.json").write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
        return directory

    def record(self, **changes):
        return cascade.cycle(self.session, self.bundle(**changes))

    def approve(self, cycle, *, decision="DESCEND"):
        self.serial += 1
        response = self.root / f"response-{self.serial}.txt"
        response.write_text(
            "FIXTURE DE TEST, aucun avis humain réel.\n"
            f"Décision simulée : {decision}, cycle {cycle['event_sha256']}.\n"
        )
        return cascade.review(self.session, cycle["event_sha256"], decision,
                              "reviewer-synthetique", response)

    def ready(self, *, level=2):
        self.record(level=level, novelty=["Clarifier la portée du critère avant de conclure."])
        last = self.record(level=level)
        self.approve(last, decision="ACCEPT" if level == 0 else "DESCEND")
        return last

    def assert_pending(self):
        result = cascade.gate(self.session)
        self.assertEqual(result["verdict"], "INCONCLUSIVE")
        self.assertTrue(result["reasons"])

    def test_cascade_descends_only_after_stability_and_referenced_review(self):
        cascade.start(self.session, mode="cascade")
        for level in (2, 1, 0):
            self.ready(level=level)
            self.assertEqual(cascade.gate(self.session)["verdict"], "READY")
            self.assertEqual(cascade.verify(self.session)["verdict"], "PASS")
            if level:
                cascade.advance(self.session)
                self.assert_pending()

    def test_direct_starts_at_zero_and_never_requires_artificial_parent_levels(self):
        cascade.start(self.session, mode="direct")
        self.ready(level=0)
        self.assertEqual(cascade.gate(self.session)["verdict"], "READY")
        cascade.advance(self.session)
        self.assertTrue(cascade.verify(self.session)["completed"])
        self.assert_pending()
        with self.assertRaises(ValueError):
            self.record(level=0)
        with self.assertRaises(ValueError):
            cascade.cycle(self.session, self.bundle(level=1))

    def test_one_cycle_or_human_silence_cannot_make_a_ready_gate(self):
        cascade.start(self.session)
        first = self.record()
        self.approve(first)
        self.assert_pending()
        second = self.record()
        self.assert_pending()
        self.approve(second)
        self.assertEqual(cascade.gate(self.session)["verdict"], "READY")

    def test_novelty_or_missing_stability_probe_prevents_descent(self):
        for changes in ({"novelty": ["Un nouveau besoin reste à traiter."]},
                        {"stability_probe": ""}):
            with self.subTest(changes=changes):
                self.session = self.root / f"session-{self.serial}"
                cascade.start(self.session)
                self.record()
                last = self.record(**changes)
                self.approve(last)
                self.assert_pending()

    def test_last_two_cycles_must_both_pass_not_only_the_last_one(self):
        for status in ("FAIL", "UNKNOWN"):
            with self.subTest(status=status):
                self.session = self.root / f"session-{status}"
                cascade.start(self.session)
                self.record(criteria={"CTR-0001": status})
                last = self.record()
                self.approve(last)
                self.assert_pending()
                last = self.record()
                self.approve(last)
                self.assertEqual(cascade.gate(self.session)["verdict"], "READY")

    def test_renaming_a_criterion_does_not_count_as_stable_success(self):
        cascade.start(self.session)
        self.record()
        last = self.record(criteria={"CTR-0002": "PASS"},
                           coverage=[{"requirement": "REQ-0001", "criterion": "CTR-0002"}])
        self.approve(last)
        self.assert_pending()

    def test_changing_the_requirement_under_the_same_criterion_resets_stability(self):
        cascade.start(self.session)
        self.record()
        last = self.record(coverage=[{"requirement": "REQ-0002", "criterion": "CTR-0001"}])
        self.approve(last)
        self.assert_pending()

    def test_changed_input_bytes_require_a_fresh_stability_cycle(self):
        cascade.start(self.session)
        self.record()
        bundle = self.bundle()
        (bundle / "source.md").write_text("Le besoin exige désormais une propriété différente.\n")
        last = cascade.cycle(self.session, bundle)
        self.approve(last)
        self.assert_pending()
        last = cascade.cycle(self.session, bundle)
        self.approve(last)
        self.assertEqual(cascade.gate(self.session)["verdict"], "READY")

    def test_coverage_must_name_existing_criteria_and_cover_the_whole_inventory(self):
        cascade.start(self.session)
        for changes in (
            {"coverage": []},
            {"coverage": [{"requirement": "REQ-0001", "criterion": "CTR-absent"}]},
            {"criteria": {"CTR-0001": "PASS", "CTR-0002": "PASS"}},
        ):
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                cascade.cycle(self.session, self.bundle(**changes))

    def test_missing_inputs_and_unresolved_business_questions_block_descent(self):
        for changes in (
            {"blocking_unknowns": ["Quelle donnée métier doit être préservée ?"]},
            {"required_inputs": [{"id": "INPUT-0001", "status": "MISSING", "source": "source.md"}]},
        ):
            with self.subTest(changes=changes):
                self.session = self.root / f"session-{self.serial}"
                cascade.start(self.session)
                self.record(**changes)
                last = self.record(**changes)
                self.approve(last)
                self.assert_pending()

    def test_a_new_cycle_requires_a_new_human_review_even_when_criteria_match(self):
        cascade.start(self.session)
        self.ready()
        last = self.record()
        self.assert_pending()
        self.approve(last)
        self.assertEqual(cascade.gate(self.session)["verdict"], "READY")

    def test_advance_is_guarded_and_reopening_an_ancestor_resets_stability(self):
        cascade.start(self.session)
        with self.assertRaises(ValueError):
            cascade.advance(self.session)
        self.ready()
        cascade.advance(self.session)
        with self.assertRaises(ValueError):
            cascade.reopen(self.session, 0, "Un descendant ne peut pas être rouvert depuis N1.")
        cascade.reopen(self.session, 2, "Une exigence amont a changé.")
        self.assert_pending()
        last = self.record()
        self.approve(last)
        self.assert_pending()
        last = self.record()
        self.approve(last)
        self.assertEqual(cascade.gate(self.session)["verdict"], "READY")

    def test_cycle_copies_its_inputs_instead_of_trusting_mutable_originals(self):
        cascade.start(self.session)
        bundle = self.bundle()
        cascade.cycle(self.session, bundle)
        (bundle / "source.md").write_text("Une source modifiée après enregistrement.\n")
        (bundle / "evidence.txt").unlink()
        self.assertEqual(cascade.verify(self.session)["verdict"], "PASS")

    def test_altering_an_archived_evidence_invalidates_the_journal(self):
        cascade.start(self.session)
        self.record()
        copies = list(self.session.rglob("evidence.txt"))
        self.assertTrue(copies, "Le journal doit conserver une copie des pièces du cycle.")
        copies[0].write_text("PASS fabriqué après coup.\n")
        self.assertEqual(cascade.verify(self.session)["verdict"], "STALE")

    def test_altering_an_event_breaks_its_fingerprint(self):
        cascade.start(self.session)
        self.record()
        path = sorted((self.session / "events").glob("*.json"))[-1]
        value = json.loads(path.read_text())
        value["forged_annotation"] = "Une modification ne doit pas rester invisible."
        path.write_text(json.dumps(value) + "\n")
        self.assertEqual(cascade.verify(self.session)["verdict"], "STALE")

    def test_rehashing_an_illegal_descent_does_not_make_the_transition_valid(self):
        cascade.start(self.session)
        last = self.record()
        sequence = len(list((self.session / "events").glob("*.json"))) + 1
        value = {"sequence": sequence, "kind": "advance", "at": "fixture",
                 "session_sha256": cascade.meta.digest((self.session / "session.json").read_bytes()),
                 "previous": last["event_sha256"], "level": 2, "epoch": 0,
                 "gate_head": last["event_sha256"]}
        value["event_sha256"] = cascade.meta.digest(cascade.meta.canonical(value))
        (self.session / "events" / f"{sequence:06d}.json").write_bytes(cascade.meta.canonical(value))
        self.assertEqual(cascade.verify(self.session)["verdict"], "STALE")
        self.assert_pending()

    def test_session_mode_is_bound_to_the_journal_not_a_mutable_bypass(self):
        cascade.start(self.session, mode="cascade")
        path = self.session / "session.json"
        value = json.loads(path.read_text())
        value["mode"] = "direct"
        path.write_text(json.dumps(value) + "\n")
        self.assertEqual(cascade.verify(self.session)["verdict"], "STALE")

    def test_external_head_detects_truncation_of_an_otherwise_valid_prefix(self):
        cascade.start(self.session)
        self.record()
        last = self.record()
        self.assertEqual(cascade.verify(self.session, expected_head=last["event_sha256"])["verdict"], "PASS")
        sorted((self.session / "events").glob("*.json"))[-1].unlink()
        self.assertEqual(cascade.verify(self.session, expected_head=last["event_sha256"])["verdict"], "STALE")

    def test_symlinks_and_evidence_path_traversal_are_rejected(self):
        cascade.start(self.session)
        linked = self.bundle()
        (linked / "evidence.txt").unlink()
        (linked / "evidence.txt").symlink_to(linked / "source.md")
        with self.assertRaises(ValueError):
            cascade.cycle(self.session, linked)
        outside = self.root / "outside.txt"
        outside.write_text("Une pièce hors du paquet.\n")
        with self.assertRaises(ValueError):
            cascade.cycle(self.session, self.bundle(evidence=["../outside.txt"]))

    def test_duplicate_json_keys_are_rejected_instead_of_silently_overriding_status(self):
        cascade.start(self.session)
        bundle = self.bundle()
        path = bundle / "cycle.json"
        raw = path.read_text().replace('"CTR-0001": "PASS"',
                                       '"CTR-0001": "FAIL", "CTR-0001": "PASS"', 1)
        path.write_text(raw)
        with self.assertRaises(ValueError):
            cascade.cycle(self.session, bundle)

    def test_review_response_is_copied_and_its_archived_bytes_are_checked(self):
        cascade.start(self.session)
        self.record()
        last = self.record()
        response = self.root / "synthetic-human-response.txt"
        response.write_text("FIXTURE : DESCEND pour ce cycle uniquement.\n")
        cascade.review(self.session, last["event_sha256"], "DESCEND", "reviewer-synthetique", response)
        original = response.read_bytes()
        response.write_text("Cette source extérieure n'est plus le reçu conservé.\n")
        self.assertEqual(cascade.verify(self.session)["verdict"], "PASS")
        archived = [p for p in self.session.rglob("*") if p.is_file() and p.read_bytes() == original]
        self.assertTrue(archived, "La réponse humaine doit être conservée dans le journal.")
        archived[0].write_text("ACCEPT inventé après la revue.\n")
        self.assertEqual(cascade.verify(self.session)["verdict"], "STALE")


class PublicationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "prepared-public"
        self.source.mkdir()
        (self.source / "EXAMPLE.md").write_text("Exemple fictif, sans matériau de projet privé.\n")
        self.review = self.root / "review.json"
        self.destination = self.root / "export"
        self.declaration = {
            "publication": "public", "contains_private_material": False,
            "authorization_ref": "FIXTURE: autorisation synthétique de ce paquet uniquement",
            "reviewer": "reviewer-synthetique", "license": "MIT",
            "scope": "Un exemple fictif préparé séparément de toute preuve privée.",
            "files": cascade._tree(self.source),
        }
        self.save_review()

    def save_review(self):
        self.review.write_text(json.dumps(self.declaration, ensure_ascii=False) + "\n")

    def test_export_preserves_exact_reviewed_files_and_publication_receipt(self):
        result = cascade.export_reviewed(self.source, self.review, self.destination)
        self.assertEqual(result["verdict"], "PASS")
        self.assertEqual(result["files"], 1)
        self.assertEqual((self.source / "EXAMPLE.md").read_bytes(),
                         (self.destination / "EXAMPLE.md").read_bytes())
        self.assertEqual(json.loads((self.destination / "PUBLICATION.json").read_text()), self.declaration)
        self.assertFalse((self.source / "PUBLICATION.json").exists())

    def test_changed_package_is_rejected_after_review(self):
        (self.source / "EXAMPLE.md").write_text("Texte ajouté après la revue.\n")
        with self.assertRaises(ValueError):
            cascade.export_reviewed(self.source, self.review, self.destination)
        self.assertFalse(self.destination.exists())

    def test_added_file_is_rejected_after_review(self):
        (self.source / "PRIVATE.txt").write_text("Pièce synthétique non incluse dans la revue.\n")
        with self.assertRaises(ValueError):
            cascade.export_reviewed(self.source, self.review, self.destination)
        self.assertFalse(self.destination.exists())

    def test_private_or_missing_publication_declarations_are_rejected(self):
        for name, replacement in (("contains_private_material", True),
                                  ("contains_private_material", None),
                                  ("publication", "private"),
                                  ("authorization_ref", None)):
            with self.subTest(name=name, replacement=replacement):
                saved = self.declaration[name]
                if replacement is None:
                    self.declaration.pop(name)
                else:
                    self.declaration[name] = replacement
                self.save_review()
                with self.assertRaises(ValueError):
                    cascade.export_reviewed(self.source, self.review, self.destination)
                self.assertFalse(self.destination.exists())
                self.declaration[name] = saved

    def test_reserved_publication_receipt_cannot_be_supplied_by_the_package(self):
        (self.source / "PUBLICATION.json").write_text("{}\n")
        self.declaration["files"] = cascade._tree(self.source)
        self.save_review()
        with self.assertRaises(ValueError):
            cascade.export_reviewed(self.source, self.review, self.destination)

    def test_export_rejects_a_destination_inside_the_reviewed_source(self):
        with self.assertRaises(ValueError):
            cascade.export_reviewed(self.source, self.review, self.source / "nested")
        self.assertFalse((self.source / "nested").exists())


if __name__ == "__main__":
    unittest.main()
