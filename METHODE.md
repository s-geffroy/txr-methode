---
title: Méthode
---

# Méthode de calcul

Ce document décrit le calcul complet, dans l'ordre où il se fait. Il vaut pour n'importe quelle station : ce qui dépend du lieu (sources de relief, altitudes des relevés de neige, largeur par défaut…) est rassemblé dans [Appliquer TxR à une station](STATIONS.md). Les choix discutables et leurs variantes sont dans [Hypothèses](HYPOTHESES.md). La version décrite est celle du programme de calcul 0.5, qui n'est pas publié à ce jour.

## Ce que la méthode produit

Pour chaque piste du plan, TxR donne deux notes indépendantes.

- **T**, de T0 à T6, mesure la difficulté technique : elle dépend de la pente des passages les plus raides.
- **R**, de R0 à R5, mesure l'exigence physique : elle dépend du dénivelé de la piste.

L'exposition (E) et les conditions du jour (C : glace, visibilité, affluence) restent en dehors des notes. Elles ne sont pas calculées aujourd'hui.

Chaque note porte un statut. Tant que les seuils ne sont pas validés, T est une *borne basse provisoire* : « T3 » se lit « au moins T3, sous les hypothèses du modèle ». Une note manque (*non déterminée*) quand les données ne permettent pas de la calculer. Le statut *définitif* demanderait des seuils validés, des pentes stables d'un pas de profil à l'autre, et la largeur, le dévers et les obstacles connus. Aucune piste ne l'atteint pour l'instant.

## Les tracés

Les pistes viennent d'OpenStreetMap : les lignes marquées `piste:type=downhill`, et celles qui appartiennent à une relation de piste, rattachées une à une aux pistes du plan officiel de la station. Toutes les distances sont mesurées à plat, dans une projection conforme (Lambert-93 en France).

Deux lignes d'une même piste ne sont mises bout à bout que si elles partagent un point OpenStreetMap, et seulement si ce point ne sert pas aussi d'embranchement. Des extrémités proches (moins de 5 m) sans point commun ne sont pas raccordées : on les signale. Une piste peut donc compter plusieurs morceaux indépendants, chacun avec son profil, et elle prend alors la note de son morceau le plus difficile.

Chaque morceau est orienté vers l'aval d'après l'altitude de ses deux extrémités. On compare ce sens à celui dans lequel la ligne a été dessinée dans OpenStreetMap et on signale les désaccords. Si les deux extrémités sont à moins de 0,5 m d'écart, l'altitude ne tranche pas : on garde le sens dans lequel la piste a été dessinée, puisque les pistes y sont dessinées vers l'aval. Si une altitude manque, on ne calcule aucune pente.

## Le profil en long

Le long de chaque tracé, on lit l'altitude du terrain sur un modèle numérique de terrain (MNT) de **sol nu**, c'est-à-dire sans arbres ni bâtiments. Un modèle de surface, qui garde la végétation, produirait de fausses pentes en lisière de forêt : il ne convient pas.

On lit un premier profil tous les 5 m sur le MNT de référence, puis, là où un MNT plus fin couvre au moins 99 % des points, des profils tous les 5, 2 et 1 m. En France, le MNT de référence est le RGE ALTI de l'IGN (maille de 1 m) et le MNT fin est issu du LiDAR HD de l'IGN (maille de 50 cm). L'altitude est interpolée entre les quatre mailles voisines (interpolation bilinéaire). Une altitude introuvable reste vide, avec son motif.

## Les pentes

La pente d'un passage de longueur W, qui commence au point s, vaut en pour cent :

$$g_W(s) = 100 \times \frac{z(s) - z(s+W)}{W}$$

Elle est positive quand on descend. L'altitude en s + W est interpolée entre les deux points de profil voisins. On fait glisser ce passage tout le long du tracé, pour trois longueurs : 10 m (murs courts), 30 m (passages) et 100 m (sections).

Un passage n'est pas retenu s'il dépasse la fin du tracé, s'il contient une altitude manquante, ou si le profil est trop grossier pour lui. Il faut que le passage soit au moins trois fois plus long que le pas du profil ou que la maille du MNT, le plus grand des deux :

$$W \geq 3 \times \max(\mathrm{pas},\ \mathrm{maille})$$

Avec un profil tous les 5 m, le passage de 10 m n'existe donc pas. La maille nominale d'un MNT n'est pas sa précision réelle, et ce critère est un minimum.

Pour chaque tracé et chaque longueur, on garde la pente maximale (Gmax), les centiles P50, P90 et P95, et l'endroit du maximum. On y note aussi la pente maximale du terrain. Si la pente du tracé atteint 90 % de celle du terrain, le tracé descend face à la pente à cet endroit, ce qui peut venir d'un tracé imprécis ou d'un talus : on le signale, sans corriger.

## La stabilité des mesures

Pour une même source, on compare Gmax, P90 et P95 d'un pas au suivant (5, puis 2, puis 1 m). L'écart toléré, en points de pente, vaut

$$\Delta g_{\max} = \frac{400\,u}{W}$$

où u est l'erreur verticale maximale du MNT, en mètres. Quand aucune documentation du producteur ne donne u, le statut reste « incertitude inconnue ». Une valeur de u = 0,10 m pour le LiDAR HD sert de test de sensibilité ; elle vient de sources secondaires. Ce contrôle ne dit rien de la position du tracé ni de la surface sous la neige.

## Du sol nu à la piste damée

Le relief est mesuré sans neige, alors que l'on skie sur une piste damée, large, où chacun choisit son passage. Trois corrections, toutes expérimentales, ramènent la mesure vers cette piste.

**La largeur.** On mesure la largeur de la piste perpendiculairement au tracé, sur les surfaces de piste dessinées dans OpenStreetMap. Il faut au moins 5 mesures couvrant 30 % du tracé ; sinon on prend la largeur médiane mesurée dans la station. On trace ensuite des lignes parallèles au tracé, tous les 2 m, jusqu'à 1 m des bords et au plus à 20 m de part et d'autre. Chaque point d'une parallèle est pris en face du point correspondant du tracé. Les parallèles vides, coupées ou de longueur anormale (hors de 0,7 à 1,3 fois le tracé) sont écartées. Pour chaque passage, on retient la parallèle la moins raide.

**Le zigzag.** Un skieur ne descend pas droit dans l'axe : on suppose qu'il s'en écarte d'un angle θ, en zigzag régulier, sans sortir de la piste. Sur un trajet de W m, il n'avance que de W × cos θ le long de la piste, et la pente de son trajet vaut le dénivelé divisé par W. Sur une pente régulière g, cela revient à multiplier la pente par cos θ, soit 0,87 à 30° et 0,71 à 45° :

$$g_{\mathrm{trajet}} = g \cos\theta$$

La valeur de référence est θ = 30°. Sur une piste de moins de 10 m de large, on ne descend pas en traversées : θ vaut 0. Multiplier toutes les pentes par cos θ revient à multiplier tous les seuils par 1 / cos θ. θ joue donc le rôle d'un réglage des seuils, et il a été fixé après avoir vu les résultats (voir [Hypothèses](HYPOTHESES.md)).

**La neige.** La neige damée comble les creux et arrondit les bosses. On la représente par une moyenne glissante du profil sur une longueur

$$L = L_0 + k\,h$$

où h est la hauteur de neige en mètres, L0 = 5 m représente l'effet de la dameuse et k = 5 le comblement par la neige. Près d'une extrémité ou d'un trou, la moyenne se fait sur moins de points pour rester centrée. Ajouter une couche d'épaisseur égale ne change rien en soi : c'est le lissage, plus long sous une neige épaisse, qui adoucit les murs. Par défaut, h vient d'une climatologie de la neige naturelle (en France, la réanalyse S2M de Météo-France : hauteur médiane de février selon l'altitude, l'orientation et la pente). La neige de culture et le tassement ne sont pas représentés.

Ces corrections ne valent pas toutes autant. Sur 30 m, la neige change peu la pente, car L reste plus court que le passage. Sur 10 m, elle peut faire baisser un mur d'une classe : c'est donc surtout par la règle du mur court que l'enneigement change la note.

## Deux façons de lire la pente

On calcule la pente selon deux conventions, côte à côte :

- **la trajectoire**, pente du trajet en zigzag à θ = 30°, qui sert de référence pour les essais ;
- **la ligne de pente**, pente de la piste dans sa propre direction, sans zigzag (θ = 0).

La ligne de pente suit la direction de la piste, pas la plus grande pente du versant : sinon un chemin tracé en travers d'un versant prendrait la note du versant. Tant que les mesures sur neige damée n'ont pas tranché, la note affichée est la plus prudente des deux, c'est-à-dire toujours celle de la ligne de pente, puisque le zigzag ne peut que réduire la pente. La trajectoire sert aux essais.

## Les virages

Le zigzag droit est une simplification. Un calcul complémentaire représente la trajectoire par des arcs de cercle : godille, virages courts, moyens ou grands, et virage coupé dont le rayon dépend du rayon de cotes des skis. Sur une pente régulière, la pente moyenne de la trajectoire vaut celle de la piste multipliée par sin φ / φ, où φ est l'angle de fin de virage que permet la largeur de la piste. Ces notes complémentaires ne changent pas la note affichée ; le détail est dans [Virages et rayon des skis](VIRAGES.md).

## La note T

T est la plus haute des classes données par trois règles. Aucune ne peut en compenser une autre.

| Règle | Mesure | T1 | T2 | T3 | T4 | T5 | T6 |
|---|---|---|---|---|---|---|---|
| Passage | pente maximale sur 30 m | 10 % | 20 % | 25 % | 35 % | 45 % | 60 % |
| Mur court | pente maximale sur 10 m | | | 40 % | 50 % | 60 % | 75 % |
| Pente soutenue | 5 % de la piste au-dessus de 40 % sur 30 m | | | | oui | | |

Une piste sans aucun passage à 10 % est T0. Avec les seuils actuels, la règle de pente soutenue ne change jamais la note : une piste dont 5 % dépasse 40 % a forcément un passage au-dessus de 35 %, donc est déjà T4. Elle est gardée pour le jour où les seuils seront recalibrés. Les seuils sur 30 m sont des conventions de travail, inspirées des repères habituels pour les pistes damées ; ceux du mur court sont les mêmes relevés de 15 points, sans calibration. Ils s'appliquent à la pente de la piste estimée, pas au sol nu. Quand un seuil n'est dépassé que sur une portion plus courte que deux fois la longueur du passage, la note est signalée « pic à confirmer ». Un tracé sur lequel aucun passage ne descend, même sur sol nu, n'est pas noté : son orientation est à vérifier.

## La note R

R est la classe du dénivelé de la piste, mesuré entre ses deux extrémités.

| R0 | R1 | R2 | R3 | R4 | R5 |
|---|---|---|---|---|---|
| < 80 m | ≥ 80 m | ≥ 200 m | ≥ 400 m | ≥ 700 m | ≥ 1 100 m |

R ne tient pas compte de la longueur, des replats où il faut pousser, ni de l'altitude. Ces seuils sont aussi des conventions de travail.

## La neige du jour

La station relève la hauteur totale de neige en des points fixes, au moins un en bas et un en haut du domaine. En chaque point de la piste, la hauteur vaut :

$$h = \left[(1 - t)\,h_{\mathrm{bas}} + t\,h_{\mathrm{haut}}\right] f \qquad t = \frac{z - z_{\mathrm{bas}}}{z_{\mathrm{haut}} - z_{\mathrm{bas}}}$$

où t est la position en altitude entre les deux points de relevé qui encadrent le point (0 en bas, 1 en haut, sans aller au-delà), et f un facteur d'orientation : le rapport, dans la climatologie du massif et pour le mois du relevé, entre la neige à cette orientation et cette pente et la neige sur le plat, à la même altitude. f est borné entre 0 et 3. Le reste du calcul ne change pas. [L'abaque d'enneigement](ABAQUE.md) permet de faire ce calcul à la main pour un passage donné.

La hauteur relevée sur piste comprend la neige de culture et le tassement, alors que la climatologie ne décrit que la neige naturelle : celle-ci ne sert qu'à répartir la neige entre les orientations.

## Reproductibilité

Chaque calcul écrit dans un dossier neuf, avec ses paramètres et l'empreinte de toutes ses sources (extrait OpenStreetMap daté, réponses du service d'altitude, dalles du MNT, climatologie, règles). Un calcul interrompu reprend là où il s'était arrêté, avec les mêmes paramètres. Un second calcul, fait sans réseau à partir des seules données conservées, doit redonner des tables identiques : c'est vérifié à chaque fois.

## Limites connues

- Les seuils de T et de R, l'angle θ, L0 et k ne sont pas calibrés.
- La largeur réelle damée, le dévers, les obstacles, la glace et les bosses ne sont pas pris en compte.
- Les types de virages et le lien avec le rayon des skis reposent sur des rayons et des largeurs balayées supposés.
- La neige de culture et le damage réel ne sont pas représentés.
