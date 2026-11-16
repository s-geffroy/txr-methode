---
title: Virages et rayon des skis
---

# Virages et rayon des skis

Personne ne descend une piste tout droit. Selon sa façon de tourner, un skieur ne parcourt pas la même pente : plus il finit ses virages en travers, plus la pente qu'il emprunte réellement est douce. Cette page décrit comment TxR en tient compte, et ce que cela change selon le rayon des skis. C'est un calcul expérimental : la note affichée reste celle de la descente dans l'axe, la plus prudente.

## Des virages en arcs de cercle

On représente la trajectoire par des arcs de cercle de rayon R, enchaînés d'un côté puis de l'autre. Au fil de chaque arc, la direction du skieur passe d'un angle φ à droite de l'axe de la piste à un angle φ à gauche. La largeur balayée a, d'un bord de la trajectoire à l'autre, vaut

$$a = 2R\,(1 - \cos\varphi)$$

Sur une pente régulière g, la pente moyenne de la trajectoire vaut, avec φ en radians :

$$g_{\mathrm{trajet}} = g\,\frac{\sin\varphi}{\varphi}$$

La pente au moment où le skieur coupe la ligne de pente, au milieu de chaque virage, reste celle de la piste.

Le skieur ne peut pas balayer plus que la largeur de la piste. Pour un rayon donné, φ est donc le plus grand angle, jusqu'à 90°, dont la largeur balayée tient dans la piste, moins un mètre de chaque côté :

$$\cos\varphi = 1 - \frac{\min(a_{\mathrm{type}},\ \ell - 2)}{2R}$$

où ℓ est la largeur de la piste en mètres et a_type la largeur que balaie habituellement ce type de virage.

## Quatre façons de tourner

Les rayons et les largeurs balayées ci-dessous sont des hypothèses de travail. Ils n'ont pas encore été mesurés sur des traces de skieurs.

| Virage | Rayon | Largeur balayée | φ sur une piste large | Pente moyenne / pente de la piste |
|---|---|---|---|---|
| Godille | 4 m | 3 m au plus | 51° | 0,87 |
| Virages courts | 8 m | 8 m au plus | 60° | 0,83 |
| Virages moyens | 15 m | 16 m au plus | 62° | 0,81 |
| Grands virages | 25 m | 30 m au plus | 64° | 0,81 |

Sur une piste de 10 m de large, les grands virages ne passent plus : φ tombe à 33° et la pente moyenne remonte à 0,95 fois celle de la piste. Pour comparaison, le zigzag droit à 30° utilisé dans les essais donne 0,87, comme la godille.

## Le rayon des skis

Un ski taillé a un rayon de cotes, inscrit sur le ski : environ 11 à 13 m pour un ski de slalom, 14 à 18 m pour un ski polyvalent, 20 m et plus pour un ski de géant. Quand le skieur coupe son virage, sans déraper, le rayon du virage vaut à peu près le rayon de cotes multiplié par le cosinus de l'angle de carre α, l'inclinaison du ski sur la neige :

$$R_{\mathrm{virage}} \approx R_{\mathrm{ski}} \cos\alpha$$

Avec un angle de 45°, celui d'un bon skieur, un ski de 15 m trace un virage d'environ 10,6 m.

Pour garder sa vitesse en main, un skieur qui coupe ses virages cherche à les finir en travers de la pente. Il lui faut pour cela une largeur d'environ deux fois le rayon de son virage, plus les marges. Le tableau donne, pour chaque rayon de ski et chaque largeur de piste, le rapport entre la pente moyenne de sa trajectoire et la pente de la piste. Plus le chiffre est proche de 1, plus le skieur subit la pente de la piste.

| Rayon du ski | Piste de 10 m | 15 m | 20 m | 30 m | 40 m | Largeur pour finir ses virages |
|---|---|---|---|---|---|---|
| 11 m (slalom) | 0,82 | 0,70 | 0,64 | 0,64 | 0,64 | 18 m |
| 13 m | 0,85 | 0,75 | 0,65 | 0,64 | 0,64 | 20 m |
| 15 m (polyvalent) | 0,87 | 0,79 | 0,70 | 0,64 | 0,64 | 23 m |
| 17 m | 0,89 | 0,81 | 0,74 | 0,64 | 0,64 | 26 m |
| 20 m | 0,90 | 0,84 | 0,78 | 0,64 | 0,64 | 30 m |
| 24 m | 0,92 | 0,87 | 0,82 | 0,71 | 0,64 | 36 m |
| 30 m (géant) | 0,94 | 0,90 | 0,85 | 0,77 | 0,68 | 44 m |

<small>Angle de carre de 45°, un mètre de marge de chaque côté. Avec un angle de 60° (skieur expert), le rayon du virage est la moitié du rayon de cotes ; avec 30°, il en fait 87 %.</small>

Exemple : sur une piste de 15 m de large et 40 % de pente, un skieur en skis de slalom qui coupe ses virages suit une pente moyenne d'environ 28 %. Avec des skis de géant, il en suit 36 %, à moins de déraper pour resserrer ses virages. Le même passage se classe alors une classe plus haut pour lui.

## Ce qu'en fait TxR

Pour chaque piste, le calcul donne la note T pour chacun des quatre types de virages et pour un virage coupé avec chaque rayon de ski, de 11 à 30 m. Il tient compte de la largeur réelle de la piste à chaque endroit où on la connaît. Ces notes servent à comprendre pourquoi un passage paraît plus dur avec certains skis ou sur une piste étroite. Elles ne remplacent pas la note affichée.

## Limites

- Les rayons, les largeurs balayées et l'angle de carre sont des hypothèses.
- La relation entre rayon de cotes et rayon du virage néglige la flexion du ski et le dérapage. En neige molle ou en dérapant, un skieur tourne plus court que ce qu'elle indique.
- Le modèle décrit la pente moyenne d'un passage, pas l'instant le plus raide d'un virage, qui reste celui de la pente de la piste.
- Des traces GPS de skieurs de plusieurs niveaux et avec plusieurs types de skis permettront de mesurer φ et les rayons réels (voir le [protocole de validation](VALIDATION.md)).
