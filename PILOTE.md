---
title: Essai à La Foux d'Allos
---

# Essai à La Foux d'Allos

La méthode a été mise au point sur La Foux d'Allos, le site le plus haut du domaine de Val d'Allos (Alpes-de-Haute-Provence), entre 1 800 et 2 600 m environ. Les résultats ci-dessous sont exploratoires. Plusieurs réglages ont été choisis en regardant ces mêmes données, si bien qu'elles ne peuvent pas servir à les valider. Les notes piste par piste ne sont pas publiées ici. Ce travail est indépendant de l'exploitant du domaine.

## Les données

- Tracés : extrait OpenStreetMap du 14/11/2026, 42 pistes du plan officiel (2 vertes, 17 bleues, 19 rouges, 4 noires), sans les variantes.
- Relief : RGE ALTI et LiDAR HD de l'IGN, 26 dalles d'un kilomètre.
- Neige : réanalyse S2M de Météo-France, massif Haut-Var/Haut-Verdon, saisons 1996 à 2026.
- Largeur : mesurée sur les surfaces de piste OpenStreetMap pour la plupart des tracés ; pour 16 tracés, la médiane mesurée (35 m).

## Accord avec les couleurs

Pour chaque piste, on regarde si sa note T tombe dans la plage attendue pour sa couleur : verte T0–T1, bleue T1–T2, rouge T3–T4, noire T4 et au-delà. Les plages se chevauchent, et une noire est conforme dès T4 : ce contrôle est donc indulgent par construction.

| Mesure de la pente | Pistes conformes sur 42 | Attendu au hasard | Accord corrigé du hasard |
|---|---|---|---|
| Sol nu, sans correction | 8 | | −0,04 |
| Ligne de pente (θ = 0°) | 10 | | −0,02 |
| Trajectoire (θ = 30°) | 20 | 14,7 | 0,19 |
| Trajectoire (θ = 45°) | 32 | | |

Les cases vides n'ont pas été calculées dans l'essai. L'intervalle de confiance à 95 % de la conformité en trajectoire va de 33 à 62 % (rééchantillonnage des pistes). La conformité augmente mécaniquement avec θ : toutes les corrections réduisent la pente, et sur sol nu aucune piste ne sort plus facile que sa couleur. Comme le zigzag revient à diviser les seuils par cos θ (voir la [méthode](METHODE.md)), ce tableau mesure surtout l'effet de ce réglage. Quand une piste n'est pas conforme, c'est presque toujours parce que TxR la trouve plus difficile que sa couleur. Cela peut venir de seuils trop sévères, d'une correction trop faible, ou du fait que la couleur tient compte d'autres critères. On ne peut pas trancher avec ces données.

## Ordre des pistes

On compare aussi l'ordre des pistes selon leur couleur et selon leur note, avec le τ-b de Kendall (1 pour un ordre identique, 0 pour aucun lien). Les intervalles à 95 % viennent de 2 000 rééchantillonnages des pistes.

| Indicateur | τ-b | Intervalle à 95 % |
|---|---|---|
| Pente moyenne de la piste | 0,59 | 0,43 à 0,71 |
| Dénivelé (note R) | 0,56 | 0,34 à 0,72 |
| T sur sol nu | 0,69 | 0,57 à 0,80 |
| T en trajectoire | 0,75 | 0,64 à 0,82 |
| T en ligne de pente | 0,76 | 0,61 à 0,88 |

Les notes T suivent l'ordre des couleurs un peu mieux que la pente moyenne ou le dénivelé, mais les intervalles se recouvrent largement. Il n'y a là rien d'étonnant : les couleurs ont été données en grande partie d'après la pente, si bien que tout indicateur de pente leur ressemble. Le résultat montre que TxR ne brouille pas l'ordre des pistes. Il ne montre pas que la correction vers la piste damée est juste. Avec seulement 2 vertes et 4 noires, l'essentiel de l'information vient de la distinction entre bleues et rouges.

## Neige

Sur des passages de 30 m, l'enneigement modifie peu les notes. Il agit surtout sur quelques murs courts, qui perdent une classe au-delà d'un certain enneigement. Pour quelques pistes, la note monte au contraire quand la neige augmente, parce que la neige se répartit inégalement selon l'orientation. Ces cas sont à vérifier sur place (voir [l'abaque](ABAQUE.md)).

## Ce que l'essai a appris

- Le calcul tourne de bout en bout et se refait à l'identique sans réseau.
- Les notes sur sol nu sont trop hautes pour la plupart des bleues : une correction vers la piste damée est nécessaire, mais son ampleur n'est pas connue.
- La suite passe par des mesures de pente sur neige damée, décrites dans le [protocole de validation](VALIDATION.md), puis par d'autres stations.

<small>Chiffres agrégés calculés à partir de données © contributeurs OpenStreetMap (ODbL 1.0, œuvre produite au sens de l'article 4.3), IGN et Météo-France (Licence Ouverte Etalab 2.0). Les couleurs des pistes sont relevées sur le plan officiel du domaine.</small>
