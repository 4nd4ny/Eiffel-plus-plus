# Besoin illustratif — REQ-0001

**Exemple fictif — statut `PROPOSED`.**

## Source

Phrase fictive d'un organisateur : « Je veux accepter les inscriptions tant qu'il reste des places, sans survente ni doublon si une personne réessaie après une coupure. »

## Service attendu

Accepter les demandes valides lorsqu'une place est disponible au point où l'opération prend effet. Pour deux demandes distinctes valides se disputant la dernière place, sans panne ni annulation et avec des appels qui aboutissent, exactement une est confirmée ; l'autre reçoit le refus prévu.

## Contraintes et questions

Capacité fixe dans ce périmètre. Une confirmation persiste après redémarrage selon les garanties du stockage choisi. La définition de « même demande », la durée de conservation des clés et l'annulation restent à préciser. Q-0001 concerne le sens de la répétition.

## Hors périmètre

Paiement, liste d'attente, changement de capacité, transferts et annulations. Leur absence ne doit pas être présentée comme une fonctionnalité validée.
