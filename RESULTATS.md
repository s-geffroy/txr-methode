---
title: Résultats par station
---

# Résultats par station

TxR a été appliqué à plusieurs stations avec exactement les mêmes réglages : seuils, zigzag, lissage par la neige et longueurs des passages. Seules changent les données propres à chaque station : relief, tracés, climatologie de la neige, points de relevé. Les résultats ci-dessous sont agrégés par couleur. Aucune note n'est publiée piste par piste.

Ces résultats sont exploratoires. Les réglages ont été fixés sur la première station, La Foux d'Allos, qui est donc la station de réglage : ses chiffres sont sans doute optimistes. Les stations suivantes ne valident pas non plus la méthode : les couleurs du plan ne sont pas une référence, seulement un contrôle. Seules des mesures sur neige damée le permettront (voir le [protocole de validation](VALIDATION.md)).

La note affichée est celle de la ligne de pente, sans zigzag : c'est la plus prudente (voir [la méthode](METHODE.md)). La note avec un zigzag à 30° sert aux essais ; elle est donnée pour comparaison, mais sa proximité avec les couleurs dépend directement de l'angle choisi, fixé après avoir vu les résultats.

## Ce que TxR dit des pistes

TxR ne cherche pas à retrouver les couleurs : il les complète en disant où la pente est forte. Le tableau compte, pour chaque station, les pistes dont la note affichée (ligne de pente) dépasse ce que leur couleur laisse habituellement attendre : une verte avec un passage de niveau bleu ou plus (T2 et au-delà), une bleue avec un passage de niveau rouge (T3 et au-delà), une rouge avec un passage de niveau noir (T5 et au-delà).

| Station | Pistes | Avec un passage au-dessus de leur couleur | Vertes au-dessus | Bleues au-dessus | Rouges au-dessus |
|---|---|---|---|---|---|
| [La Foux d'Allos](PILOTE.md) | 42 | 32 | 1 sur 2 | 14 sur 17 | 17 sur 19 |
| Pra-Loup | 39 | 27 | — | 13 sur 14 | 14 sur 20 |
| Grand Tourmalet | 42 | 31 | 2 sur 3 | 17 sur 20 | 12 sur 14 |
| Val d'Isère–Tignes | 119 | 88 | 9 sur 10 | 56 sur 58 | 23 sur 38 |

Sur les quatre stations, 100 bleues sur 109 ont au moins un passage que TxR classe comme une rouge, et 66 rouges sur 91 un passage de niveau noir. Ces notes sont des bornes provisoires : les seuils ne sont pas calibrés, et le passage qui fixe la note est à vérifier sur place dans 94 % des cas (tracé OpenStreetMap qui suit la ligne de plus grande pente, ou passage court). Elles disent où regarder, pas encore ce qu'il faut afficher. Seules des mesures de pente sur neige damée diront si ces passages sont aussi raides sur la piste que sur le relief d'été (voir le [protocole de validation](VALIDATION.md)).

## Comparaison avec les couleurs : un contrôle, pas un objectif

La comparaison avec les couleurs du plan ne sert qu'à deux choses. Elle permet de **repérer une erreur grossière** : une noire notée T1, ou un ordre des notes sans rapport avec celui des couleurs, signale un tracé ou un relief faux. Les relectures de ces notes ont fait trouver un tracé incomplet et deux tracés mal orientés. Elle sert aussi de **garde-fou contre le réglage déguisé** : toutes les corrections réduisent la pente, si bien que la part des pistes « dans la plage » de leur couleur monte mécaniquement avec l'angle de zigzag ou la largeur supposés. La comparer au hasard montre ce qui revient au réglage.

| Station | Massif | Pistes comparées | Note affichée : dans la plage / au hasard | κ note affichée (IC 95 %) | Zigzag à 30° : dans la plage / au hasard | κ zigzag (IC 95 %) | τ-b couleur / note affichée (IC 95 %) | τ-b couleur / pente moyenne |
|---|---|---|---|---|---|---|---|---|
| [La Foux d'Allos](PILOTE.md) (réglage) | Haut-Var/Haut-Verdon | 42 | 10 / 10,7 | −0,02 (−0,14 à 0,12) | 19 / 14,3 | 0,17 (−0,01 à 0,38) | 0,76 (0,62–0,88) | 0,59 |
| Pra-Loup | Ubaye | 39 | 11 / 12,8 | −0,07 (−0,18 à 0,06) | 24 / 18,9 | 0,25 (0,03 à 0,50) | 0,66 (0,49–0,80) | 0,65 |
| Grand Tourmalet | Haute-Bigorre | 42 | 10 / 11,7 | −0,06 (−0,19 à 0,09) | 17 / 14,1 | 0,10 (−0,08 à 0,30) | 0,67 (0,48–0,80) | 0,58 |
| Val d'Isère–Tignes | Haute-Tarentaise | 119 | 29 / 36,9 | −0,10 (−0,17 à −0,01) | 48 / 40,3 | 0,10 (0,01 à 0,20) | 0,56 (0,44–0,68) | 0,46 |

« Pistes comparées » : pistes dont la couleur est vérifiée sur le plan, damées, au tracé complet et notées. « Dans la plage » : la note T tombe dans la plage habituelle de la couleur (verte T0–T1, bleue T1–T2, rouge T3–T4, noire T4 et au-delà ; les noires y sont presque par construction). « Au hasard » : nombre qu'on obtiendrait avec la même répartition des notes, sans lien avec la couleur. κ est l'accord corrigé du hasard : 0 pour un accord dû au hasard ; un intervalle qui contient 0 veut dire que l'accord ne se distingue pas du hasard. Les intervalles viennent d'un rééchantillonnage des pistes (bootstrap). Le τ-b de Kendall mesure si l'ordre des notes suit celui des couleurs : 1 pour un ordre identique, 0 pour aucun lien.

Ce que montrent ces contrôles :

- **Pas d'erreur grossière visible.** L'ordre des notes suit celui des couleurs dans les quatre stations (τ-b de 0,56 à 0,76). La pente moyenne seule (dénivelé divisé par la longueur) donne déjà un ordre proche : T ne fait mieux que de 0,09 à 0,17, et pas du tout à Pra-Loup ; l'écart le plus grand est à La Foux, la station de réglage.
- **Pas d'accord fabriqué pour la note affichée.** Sa part « dans la plage » ne dépasse le hasard dans aucune station ; quand elle sort de la plage, c'est presque toujours vers le haut (178 pistes sur 182). Avec le zigzag à 30°, choisi après avoir vu les résultats, la part dans la plage dépasse le hasard à Pra-Loup et à Val d'Isère–Tignes : c'est l'effet du réglage, et c'est pourquoi cette note n'est pas affichée.
- Quatre pistes du secteur des Agneliers comptent à la fois pour La Foux et pour Pra-Loup, avec les mêmes notes. Les stations ne sont donc pas tout à fait indépendantes.

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

Valeurs médianes, avec entre parenthèses la plus petite et la plus grande. On y retrouve ce que montrait La Foux : les pentes montent avec la couleur, mais les bleues sortent le plus souvent en T3 ou T4, au-dessus de la classe attendue. La seule bleue notée T0 est un chemin presque plat. Pra-Loup n'a aucune verte contrôlée, ce qui limite la comparaison avec les autres stations.

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

Le Grand Tourmalet suit le même schéma que les deux stations des Alpes du Sud : 31 pistes sur 42 ont un passage au-dessus de leur couleur avec la note affichée ; 10 sont dans la plage de leur couleur, pour 11,7 au hasard. La largeur n'a pu être mesurée nulle part, ce qui ajoute une incertitude à toutes les notes. La seule rouge notée T2 est une piste de 10 % de pente moyenne, rouge sur le plan mais bleue dans OpenStreetMap : il s'agit peut-être d'un homonyme de plus, à vérifier sur place.

## Val d'Isère–Tignes

Val d'Isère et Tignes (Savoie) forment un seul domaine skiable, de 1 550 m à plus de 3 400 m, avec deux glaciers. Les deux stations sont traitées séparément pour la neige : chacune a ses propres points de relevé, à 1 550 m et 3 456 m pour Tignes, à 1 785 m et 3 300 m pour Val d'Isère. La limite suit la crête qui va de la Tovière au col de Fresse. Quatre noms sont portés par une piste de chaque côté (Face, Génépy, Glacier, Signal) : ce sont des pistes distinctes.

Les pistes viennent d'OpenStreetMap, et leurs couleurs ont été vérifiées sur le plan officiel 2026-2027, commun aux deux stations. Le fond de ce plan est une image : les noms ont été relevés à l'œil, sur des vues agrandies. Sur 170 pistes, 133 ont la même couleur dans les deux sources, et trois ont été corrigées d'après le plan. Les 34 autres n'ont pas d'étiquette sur le plan ; elles sont notées mais ne comptent pas dans l'accord avec les couleurs. La piste rouge OK n'est dessinée dans OpenStreetMap que sur un tronçon de 110 m : elle est notée sur ce tronçon, avec la mention « tracé incomplet », mais sort elle aussi de l'accord.

Quinze pistes noires sont marquées « Naturide » sur le plan : balisées et sécurisées, mais non damées. La méthode suppose une neige damée, qui lisse le relief. Depuis la version 0.6.0, elles sont notées sans l'effet de la dameuse, avec la mention « non damée » (voir [la méthode](METHODE.md)), et ne comptent pas dans l'accord avec les couleurs. Pour ces quinze pistes, la règle ne change aucune note : sans dameuse, elles sortent dans la même classe que si elles étaient damées. Seule la mention les distingue. Le relief vient de 89 dalles LiDAR HD de l'IGN.

| | Verte | Bleue | Rouge | Noire |
|---|---|---|---|---|
| Pistes | 10 | 58 | 38 | 13 |
| Pente moyenne | 15 % (8–19) | 17 % (6–32) | 24 % (4–39) | 30 % (12–43) |
| Pente maximale sur 30 m, sol nu | 32 % (12–48) | 42 % (25–55) | 51 % (11–74) | 62 % (38–70) |
| Pente maximale sur 30 m, piste estimée | 30 % (10–42) | 37 % (18–51) | 46 % (9–69) | 53 % (37–66) |
| Pente maximale sur 10 m, piste estimée | 31 % | 38 % | 48 % | 55 % |
| Note T affichée (sans zigzag) | T1 : 1, T2 : 1, T3 : 6, T4 : 2 | T1 : 1, T2 : 1, T3 : 16, T4 : 35, T5 : 5 | T0 : 1, T1 : 1, T3 : 1, T4 : 12, T5 : 21, T6 : 2 | T4 : 4, T5 : 5, T6 : 4 |
| Note T avec zigzag à 30° | T0 : 1, T2 : 2, T3 : 6, T4 : 1 | T1 : 2, T2 : 6, T3 : 36, T4 : 12, T5 : 2 | T0 : 1, T1 : 1, T3 : 6, T4 : 22, T5 : 7, T6 : 1 | T3 : 2, T4 : 4, T5 : 7 |
| Note R | R0 : 3, R1 : 1, R2 : 6 | R0 : 5, R1 : 34, R2 : 13, R3 : 6 | R0 : 2, R1 : 11, R2 : 17, R3 : 7, R4 : 1 | R1 : 5, R2 : 3, R3 : 3, R4 : 2 |
| Classe T attendue pour la couleur | T0–T1 | T1–T2 | T3–T4 | T4–T6 |

C'est le plus grand échantillon : 88 pistes sur 119 ont un passage au-dessus de leur couleur avec la note affichée, et 29 sont dans la plage de leur couleur (36,9 au hasard). Toutes les noires sont dans leur plage, ce qui tient surtout à sa largeur (T4 et au-delà). Les rouges le sont un peu plus d'une fois sur trois. Les bleues, qui font la moitié de l'échantillon, sortent presque toutes en T3 ou T4, et neuf vertes sur dix au-dessus de T1. Leurs pentes brutes sont du même ordre que dans les autres stations (42 % de pente maximale sur 30 m pour les bleues, 41 % au Grand Tourmalet), mais elles dépassent plus souvent qu'ailleurs la plage de leur couleur. Il faudra des mesures sur place pour savoir si la grille est trop sévère pour ces pistes ou si leur couleur tient compte d'autre chose que la pente.

<small>Chiffres agrégés calculés à partir de données © contributeurs OpenStreetMap (ODbL 1.0, œuvre produite au sens de l'article 4.3), IGN et Météo-France (Licence Ouverte Etalab 2.0). Couleurs des pistes : plans officiels des stations, non redistribués. Ce travail est indépendant des exploitants des stations.</small>
