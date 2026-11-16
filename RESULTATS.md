---
title: Résultats par station
---

# Résultats par station

TxR a été appliqué à plusieurs stations avec exactement les mêmes réglages : seuils, zigzag, lissage par la neige et longueurs des passages. Seules changent les données propres à chaque station : relief, tracés, climatologie de la neige, points de relevé. Les résultats ci-dessous sont agrégés par couleur. Aucune note n'est publiée piste par piste.

Ces résultats sont exploratoires. Les réglages ont été fixés sur la première station, La Foux d'Allos ; les stations suivantes ne servent pas non plus à les valider, car elles ne sont comparées qu'aux couleurs du plan. Seules des mesures sur neige damée le permettront (voir le [protocole de validation](VALIDATION.md)).

## Vue d'ensemble

| Station | Massif | Pistes de couleur vérifiée | Conformes en trajectoire (θ = 30°) | Attendu au hasard | Conformes sans zigzag | τ-b couleur / note (IC 95 %) |
|---|---|---|---|---|---|---|
| [La Foux d'Allos](PILOTE.md) | Haut-Var/Haut-Verdon | 42 | 19 | 14,3 | 10 | 0,75 (0,66–0,82) |
| Pra-Loup | Ubaye | 39 | 24 | 18,9 | 11 | 0,58 (0,39–0,73) |
| Grand Tourmalet | Haute-Bigorre | 42 | 17 | 14,1 | 10 | 0,71 (0,58–0,82) |
| Val d'Isère–Tignes | Haute-Tarentaise | 120 | 49 | 41,0 | 30 | 0,51 (0,39–0,62) |

« Conformes » : pistes dont la note T tombe dans la plage attendue pour leur couleur (verte T0–T1, bleue T1–T2, rouge T3–T4, noire T4 et au-delà). Le τ-b de Kendall mesure si l'ordre des notes suit celui des couleurs : 1 pour un ordre identique, 0 pour aucun lien. Dans chaque station, la pente moyenne seule donne déjà un ordre assez proche de celui des couleurs (voir [l'essai à La Foux](PILOTE.md)).

## Pra-Loup

Pra-Loup (Alpes-de-Haute-Provence) est reliée à La Foux d'Allos par le secteur des Agneliers, dont les cinq pistes sont comptées dans les deux stations. Les points de relevé de la neige sont à 1 650 m et 2 503 m.

Les pistes viennent d'OpenStreetMap, et leurs couleurs ont été vérifiées sur le plan officiel de la station. Sur 55 pistes, 38 ont la même couleur dans les deux sources. Une piste est rouge dans OpenStreetMap et noire sur le plan : c'est le plan qui fait foi. Les 16 autres, surtout les vertes de l'espace débutants et des chemins de liaison, n'ont pas d'étiquette sur le plan. Elles sont notées mais ne comptent pas dans l'accord avec les couleurs, si bien qu'aucune verte n'y figure. Le relief vient de 15 dalles LiDAR HD de l'IGN.

| | Bleue | Rouge | Noire |
|---|---|---|---|
| Pistes | 14 | 20 | 5 |
| Pente moyenne | 17 % (7–24) | 27 % (22–36) | 32 % (28–35) |
| Pente maximale sur 30 m, sol nu | 37 % (10–50) | 53 % (40–62) | 62 % (53–71) |
| Pente maximale sur 30 m, piste estimée | 35 % (8–47) | 48 % (37–61) | 57 % (51–65) |
| Pente maximale sur 10 m, piste estimée | 36 % | 49 % | 56 % |
| Note T affichée (sans zigzag) | T0 : 1, T3 : 6, T4 : 5, T5 : 2 | T4 : 6, T5 : 13, T6 : 1 | T5 : 3, T6 : 2 |
| Note T avec zigzag à 30° | T0 : 1, T2 : 3, T3 : 5, T4 : 5 | T3 : 3, T4 : 13, T5 : 4 | T4 : 2, T5 : 3 |
| Note R | R0 : 4, R1 : 3, R2 : 4, R3 : 3 | R1 : 11, R2 : 7, R3 : 1, R4 : 1 | R1 : 1, R2 : 3, R3 : 1 |
| Classe T attendue pour la couleur | T1–T2 | T3–T4 | T4–T6 |

Valeurs médianes, avec entre parenthèses la plus petite et la plus grande. On y retrouve ce que montrait La Foux : les pentes montent avec la couleur, mais les bleues sortent le plus souvent en T3 ou T4, au-dessus de la classe attendue. La seule bleue notée T0 est un chemin presque plat. L'accord avec les couleurs en trajectoire est meilleur qu'à La Foux, mais l'ordre des notes suit moins bien celui des couleurs.

## Grand Tourmalet

Le Grand Tourmalet (Hautes-Pyrénées) réunit deux versants, Barèges et La Mongie, reliés au col du Tourmalet. Chaque versant a ses propres points de relevé de neige, à 1 400 m et 2 500 m, et chaque piste prend la neige de son versant.

Les pistes viennent d'OpenStreetMap. Leurs couleurs ont été vérifiées sur le plan officiel 2021-2022, un document vectoriel dont les noms se lisent avec leur couleur, recoupé avec l'image du plan 2025-2026. Sur ce domaine, plusieurs pistes différentes portent le même nom : il y a trois « Sapins », une bleue, une rouge et une noire, et deux « Espade », « Sud » ou « Tourmalet ». Elles sont comptées comme des pistes distinctes. Sur 53 pistes, 42 ont une couleur vérifiée, dont deux corrigées d'après le plan. Onze n'ont pas d'étiquette sur le plan et sept pistes du plan n'ont pas de tracé nommé dans OpenStreetMap. Aucune surface de piste n'est dessinée dans OpenStreetMap pour cette station : la largeur n'a pu être mesurée nulle part, et toutes les pistes reçoivent une largeur de 30 m. Le relief vient de 28 dalles LiDAR HD de l'IGN.

| | Verte | Bleue | Rouge | Noire |
|---|---|---|---|---|
| Pistes | 3 | 20 | 14 | 5 |
| Pente moyenne | 11 % (5–11) | 19 % (8–23) | 31 % (10–36) | 31 % (26–54) |
| Pente maximale sur 30 m, sol nu | 28 % (18–37) | 41 % (18–57) | 57 % (33–76) | 64 % (57–76) |
| Pente maximale sur 30 m, piste estimée | 22 % (12–29) | 37 % (16–49) | 53 % (23–69) | 61 % (52–73) |
| Pente maximale sur 10 m, piste estimée | 26 % | 40 % | 54 % | 64 % |
| Note T affichée (sans zigzag) | T1 : 1, T2 : 1, T3 : 1 | T1 : 3, T3 : 5, T4 : 8, T5 : 4 | T2 : 1, T4 : 1, T5 : 10, T6 : 2 | T5 : 2, T6 : 3 |
| Note T avec zigzag à 30° | T1 : 2, T3 : 1 | T1 : 3, T2 : 2, T3 : 8, T4 : 7 | T2 : 1, T4 : 5, T5 : 8 | T5 : 4, T6 : 1 |
| Note R | R0 : 2, R1 : 1 | R0 : 3, R1 : 7, R2 : 10 | R1 : 6, R2 : 7, R3 : 1 | R1 : 1, R2 : 2, R3 : 2 |
| Classe T attendue pour la couleur | T0–T1 | T1–T2 | T3–T4 | T4–T6 |

Le Grand Tourmalet suit le même schéma que les deux stations des Alpes du Sud, avec l'accord le plus faible : 17 pistes sur 42 en trajectoire, à peine plus que le hasard. Une partie de l'écart tient sans doute à la largeur, qui n'a pu être mesurée. La seule rouge notée T2 est une piste de 10 % de pente moyenne, rouge sur le plan mais bleue dans OpenStreetMap : il s'agit peut-être d'un homonyme de plus, à vérifier sur place.

## Val d'Isère–Tignes

Val d'Isère et Tignes (Savoie) forment un seul domaine skiable, de 1 550 m à plus de 3 400 m, avec deux glaciers. Les deux stations sont traitées séparément pour la neige : chacune a ses propres points de relevé, à 1 550 m et 3 456 m pour Tignes, à 1 785 m et 3 300 m pour Val d'Isère. La limite suit la crête qui va de la Tovière au col de Fresse. Quatre noms sont portés par une piste de chaque côté (Face, Génépy, Glacier, Signal) : ce sont des pistes distinctes.

Les pistes viennent d'OpenStreetMap, et leurs couleurs ont été vérifiées sur le plan officiel 2026-2027, commun aux deux stations. Le fond de ce plan est une image : les noms ont été relevés à l'œil, sur des vues agrandies. Sur 170 pistes, 133 ont la même couleur dans les deux sources, et trois ont été corrigées d'après le plan. Les 34 autres n'ont pas d'étiquette sur le plan ; elles sont notées mais ne comptent pas dans l'accord avec les couleurs.

Quinze pistes noires sont marquées « Naturide » sur le plan : balisées et sécurisées, mais non damées. La méthode suppose une neige damée, qui lisse le relief. Depuis la version 0.6.0, elles sont notées sans l'effet de la dameuse, avec la mention « non damée » (voir [la méthode](METHODE.md)), et ne comptent pas dans l'accord avec les couleurs. Le relief vient de 89 dalles LiDAR HD de l'IGN.

| | Verte | Bleue | Rouge | Noire |
|---|---|---|---|---|
| Pistes | 10 | 58 | 39 | 13 |
| Pente moyenne | 15 % (8–19) | 17 % (6–32) | 25 % (4–39) | 30 % (12–43) |
| Pente maximale sur 30 m, sol nu | 32 % (12–48) | 42 % (25–55) | 51 % (11–74) | 62 % (38–70) |
| Pente maximale sur 30 m, piste estimée | 30 % (10–42) | 37 % (18–51) | 46 % (9–69) | 53 % (37–66) |
| Pente maximale sur 10 m, piste estimée | 31 % | 38 % | 47 % | 55 % |
| Note T affichée (sans zigzag) | T1 : 1, T2 : 1, T3 : 6, T4 : 2 | T1 : 1, T2 : 1, T3 : 16, T4 : 35, T5 : 5 | T0 : 1, T1 : 1, T3 : 2, T4 : 12, T5 : 21, T6 : 2 | T4 : 4, T5 : 5, T6 : 4 |
| Note T avec zigzag à 30° | T0 : 1, T2 : 2, T3 : 6, T4 : 1 | T1 : 2, T2 : 6, T3 : 36, T4 : 12, T5 : 2 | T0 : 1, T1 : 1, T3 : 7, T4 : 22, T5 : 7, T6 : 1 | T3 : 2, T4 : 4, T5 : 7 |
| Note R | R0 : 3, R1 : 1, R2 : 6 | R0 : 5, R1 : 34, R2 : 13, R3 : 6 | R0 : 3, R1 : 11, R2 : 17, R3 : 7, R4 : 1 | R1 : 5, R2 : 3, R3 : 3, R4 : 2 |
| Classe T attendue pour la couleur | T0–T1 | T1–T2 | T3–T4 | T4–T6 |

C'est le plus grand échantillon, et l'accord y est le plus faible : 49 pistes sur 120 en trajectoire, pour 41 attendues au hasard. Les rouges et les noires tombent le plus souvent dans leur classe. Les bleues, qui font la moitié de l'échantillon, sortent presque toutes en T3, et six vertes sur dix aussi. Leurs pentes sont pourtant du même ordre que dans les autres stations : 42 % de pente maximale sur 30 m pour les bleues, contre 41 % au Grand Tourmalet. Le poids des bleues dans l'échantillon suffit à faire baisser l'accord. Il faudra des mesures sur place pour savoir si la grille est trop sévère pour ces pistes ou si leur couleur tient compte d'autre chose que la pente.

<small>Chiffres agrégés calculés à partir de données © contributeurs OpenStreetMap (ODbL 1.0, œuvre produite au sens de l'article 4.3), IGN et Météo-France (Licence Ouverte Etalab 2.0). Couleurs des pistes : plans officiels des stations, non redistribués. Ce travail est indépendant des exploitants des stations.</small>
