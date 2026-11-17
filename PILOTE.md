---
title: Essai à La Foux d'Allos
description: "Premier essai de TxR sur les 42 pistes de La Foux d'Allos : pentes, notes et contrôles."
---

# Essai à La Foux d'Allos

La méthode a été mise au point sur La Foux d'Allos, le site le plus haut du domaine de Val d'Allos (Alpes-de-Haute-Provence), entre 1 800 et 2 600 m environ. Les résultats ci-dessous sont exploratoires. Plusieurs réglages ont été choisis en regardant ces mêmes données, si bien qu'elles ne peuvent pas servir à les valider. Les notes piste par piste ne sont pas publiées ici. Ce travail est indépendant de l'exploitant du domaine.

## Les données

- Tracés : extrait OpenStreetMap du 14/11/2026, 42 pistes du plan officiel (2 vertes, 17 bleues, 19 rouges, 4 noires), sans les variantes.
- Relief : RGE ALTI et LiDAR HD de l'IGN, 26 dalles d'un kilomètre.
- Neige : réanalyse S2M de Météo-France, massif Haut-Var/Haut-Verdon, saisons 1996 à 2026.
- Largeur : mesurée sur les surfaces de piste OpenStreetMap pour 16 tracés sur 72 (les seuls bien couverts par une surface dessinée) ; pour les autres, la médiane mesurée (34 m). Les résultats ci-dessous viennent du calcul 0.5 (relief interpolé, largeur mesurée surface par surface) ; ils diffèrent de moins d'une piste de ceux du calcul 0.4.

## Couleurs, pentes et notes

Le tableau rassemble, couleur par couleur, les principales caractéristiques des pistes et les notes que leur donne TxR. Pour chaque grandeur, il donne la médiane des pistes, avec entre parenthèses la plus petite et la plus grande valeur. Les pentes maximales sont celles du passage le plus raide de chaque piste. Le sol nu est le relief sans neige ni correction ; la piste estimée tient compte de la largeur et de la neige, sans zigzag.

| | Verte | Bleue | Rouge | Noire |
|---|---|---|---|---|
| Pistes | 2 | 17 | 19 | 4 |
| Dénivelé | 55 m (41–70) | 131 m (18–364) | 244 m (83–626) | 438 m (421–528) |
| Pente moyenne | 8 % (6–9) | 20 % (4–30) | 29 % (11–45) | 34 % (29–37) |
| Pente maximale sur 30 m, sol nu | 29 % (16–42) | 39 % (24–53) | 56 % (43–68) | 71 % (64–78) |
| Pente maximale sur 30 m, piste estimée | 19 % (15–24) | 37 % (17–48) | 52 % (40–62) | 65 % (61–74) |
| Pente maximale sur 10 m, piste estimée | 21 % | 37 % | 54 % | 67 % |
| Note T affichée (sans zigzag) | T1 : 1, T2 : 1 | T1 : 3, T3 : 5, T4 : 5, T5 : 4 | T4 : 2, T5 : 16, T6 : 1 | T6 : 4 |
| Note T avec zigzag à 30° | T1 : 2 | T1 : 3, T2 : 3, T3 : 5, T4 : 6 | T3 : 1, T4 : 6, T5 : 12 | T5 : 3, T6 : 1 |
| Note R | R0 : 2 | R0 : 4, R1 : 7, R2 : 6 | R1 : 8, R2 : 6, R3 : 5 | R3 : 4 |
| Classe T attendue pour la couleur | T0–T1 | T1–T2 | T3–T4 | T4–T6 |

« T3 : 5 » se lit « cinq pistes notées T3 ». Toutes les grandeurs montent avec la couleur, mais les plages se recouvrent largement : des bleues sont plus raides que certaines rouges, sur sol nu comme sur la piste estimée. Les notes T sortent le plus souvent au-dessus de la classe attendue pour la couleur, surtout sans zigzag. Les pentes du plus raide passage des bleues (37 % en médiane) dépassent nettement les repères habituels des bleues damées : c'est soit le signe que la correction vers la piste damée reste trop faible, soit que les couleurs tiennent compte d'autres critères que le passage le plus raide. Seules des mesures sur neige damée permettront de trancher.

## Comparaison avec les couleurs : un contrôle

TxR ne cherche pas à retrouver les couleurs ; la comparaison sert à repérer une erreur grossière et à voir ce qui revient aux réglages. Pour chaque piste, on regarde si sa note T tombe dans la plage habituelle de sa couleur : verte T0–T1, bleue T1–T2, rouge T3–T4, noire T4 et au-delà. Les plages se chevauchent, et une noire y est dès T4 : ce contrôle est donc indulgent par construction.

| Mesure de la pente | Pistes dans la plage sur 42 | Au hasard | Accord corrigé du hasard |
|---|---|---|---|
| Sol nu, sans correction | 8 | 9,2 | −0,04 |
| Ligne de pente (θ = 0°), note affichée | 10 | 10,7 | −0,02 |
| Trajectoire (θ = 30°) | 19 | 14,3 | 0,17 |
| Trajectoire (θ = 45°) | 32 | 19,2 | 0,56 |

Pour la note affichée, celle de la ligne de pente, l'accord ne se distingue pas du hasard : accord corrigé de −0,02, avec un intervalle à 95 % de −0,14 à 0,12. En trajectoire, il est de 0,17 (−0,01 à 0,38) et la part dans la plage va de 31 à 60 % (rééchantillonnage des pistes). Cette part augmente mécaniquement avec θ : toutes les corrections réduisent la pente, et sur sol nu aucune piste ne sort plus facile que sa couleur. Comme le zigzag revient à diviser les seuils par cos θ (voir la [méthode](METHODE.md)), ce tableau mesure surtout l'effet de ce réglage. Quand une piste sort de la plage, c'est presque toujours parce que TxR lui trouve un passage plus raide que sa couleur ne le laisse attendre. C'est l'information que TxR veut donner, à condition qu'elle soit juste : cela peut aussi venir de seuils trop sévères ou d'une correction trop faible. Seules des mesures sur neige damée trancheront.

## Ordre des pistes

On compare aussi l'ordre des pistes selon leur couleur et selon leur note, avec le τ-b de Kendall (1 pour un ordre identique, 0 pour aucun lien). Les intervalles à 95 % viennent de rééchantillonnages des pistes (500 pour les notes T, 2 000 pour la pente moyenne et le dénivelé).

| Indicateur | τ-b | Intervalle à 95 % |
|---|---|---|
| Pente moyenne de la piste | 0,59 | 0,43 à 0,71 |
| Dénivelé (note R) | 0,56 | 0,34 à 0,72 |
| T sur sol nu | 0,69 | 0,56 à 0,79 |
| T en trajectoire | 0,75 | 0,66 à 0,82 |
| T en ligne de pente | 0,76 | 0,62 à 0,88 |

Les notes T suivent l'ordre des couleurs un peu mieux que la pente moyenne ou le dénivelé, mais les intervalles se recouvrent largement. Il n'y a là rien d'étonnant : les couleurs ont été données en grande partie d'après la pente, si bien que tout indicateur de pente leur ressemble. Le résultat montre que TxR ne brouille pas l'ordre des pistes. Il ne montre pas que la correction vers la piste damée est juste. Avec seulement 2 vertes et 4 noires, l'essentiel de l'information vient de la distinction entre bleues et rouges.

## Neige

Sur des passages de 30 m, l'enneigement modifie peu les notes. Il agit surtout sur quelques murs courts, qui perdent une classe au-delà d'un certain enneigement. Pour quelques pistes, la note monte au contraire quand la neige augmente, parce que la neige se répartit inégalement selon l'orientation. Ces cas sont à vérifier sur place (voir [l'abaque](ABAQUE.md)).

## Ce que l'essai a appris

- Le calcul tourne de bout en bout et se refait à l'identique sans réseau.
- Les notes sur sol nu sont trop hautes pour la plupart des bleues : une correction vers la piste damée est nécessaire, mais son ampleur n'est pas connue.
- La suite passe par des mesures de pente sur neige damée, décrites dans le [protocole de validation](VALIDATION.md), puis par d'autres stations.

<small>Chiffres agrégés calculés à partir de données © contributeurs OpenStreetMap (ODbL 1.0, œuvre produite au sens de l'article 4.3), IGN et Météo-France (Licence Ouverte Etalab 2.0). Les couleurs des pistes sont relevées sur le plan officiel du domaine.</small>
