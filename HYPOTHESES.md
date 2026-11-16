---
title: Hypothèses
---

# Principes et hypothèses

Cette page liste les principes de départ de TxR, puis les hypothèses de la correction vers la piste damée, avec la façon dont chacune a été fixée et les variantes essayées. La plupart de ces hypothèses ont été arrêtées pendant l'analyse de la station pilote, sans enregistrement préalable, et parfois après avoir vu l'accord avec les couleurs. Elles devront être confirmées sur des données nouvelles.

## Principes de départ

| | Principe | Ce qu'il implique |
|---|---|---|
| P1 | Un classement comparable d'une station à l'autre | La mesure est imposée et versionnée. Aucun seuil ni réglage n'est propre à une station ; seules les données d'entrée changent (voir [Appliquer TxR à une station](STATIONS.md)). |
| P2 | Deux notes, technique et résistance, plutôt qu'une couleur | T et R sont calculées séparément et ne se compensent pas. La couleur officielle est conservée à part, jamais déduite des notes. |
| P3 | Une mesure de la pente définie une fois pour toutes | Distances à plat ; passages de 10, 30 et 100 m glissés le long du tracé ; pente moyenne = dénivelé / longueur. |
| P4 | Pas de seuil présenté comme validé tant qu'il ne l'est pas | Les seuils sont des conventions de travail. Les notes sont des bornes provisoires. |
| P5 | Largeur et damage restent des informations à part | Ils servent à estimer la piste, mais ne forment pas une note. |
| P6 | Un relief mesuré finement, de sol nu | MNT d'un mètre ou mieux pour les murs courts (LiDAR). |

Le nom TxR vient de *Technical × Resistance* : la technique et la résistance physique, c'est-à-dire l'endurance.

## Hypothèses de la correction vers la piste damée

| | Hypothèse | Comment elle a été fixée | Variantes essayées |
|---|---|---|---|
| H1 | On peut choisir son passage dans la largeur : parallèles tous les 2 m, on retient la moins raide pour chaque passage | Choix de l'auteur. La parallèle retenue peut changer d'un passage à l'autre, ce qui suppose un skieur qui change de ligne librement | axe seul ; largeur de 20 m et de 40 m |
| H2 | Largeur : surfaces OpenStreetMap si au moins 5 mesures couvrent 30 % du tracé, sinon médiane de la station | Choix technique, sans source externe | aucune |
| H3 | La neige lisse le profil sur L = 5 m + 5 × h | Hypothèse de travail, sans mesure | pas de lissage ; L = 10 m + 10 × h ; neige de décembre faible et de mars forte |
| H4 | Zigzag symétrique à θ = 30° de l'axe | Choisi parmi 0°, 30° et 45°, après avoir vu l'accord avec les couleurs. θ joue le rôle d'un réglage des seuils | θ = 0° et 45°. Une première version, où le skieur finissait chaque passage plus haut sur le côté, donnait des pentes nulles ou négatives sur les vertes : abandonnée |
| H5 | Deux conventions publiées : trajectoire et ligne de pente | Choix de l'auteur, pour ne pas trancher avant les mesures | aucune |
| H6 | Mur court : 40, 50, 60 et 75 % sur 10 m donnent au moins T3, T4, T5 et T6 | Seuils sur 30 m relevés de 15 points, sans calibration | aucune |
| H7 | La neige du jour se répartit en ligne droite entre deux relevés, en bas et en haut du domaine, modulée par l'orientation | Choix de l'auteur ; le facteur d'orientation vient de la climatologie | aucune |
| H8 | Les parallèles sont prises en face du tracé, point par point | Correction d'un défaut : une version antérieure les faisait dériver dans les virages | rapport de longueur global (abandonné) |
| H9 | L'accord avec les couleurs se compte par piste, comparé au hasard | Révision méthodologique | comptage par morceau de tracé (abandonné) |
| H10 | Pas de zigzag sur une piste de moins de 10 m de large | Revue de la méthode | zigzag partout (abandonné) |
| H11 | Les virages sont des arcs de cercle : godille (4 m), courts (8 m), moyens (15 m), grands (25 m), avec une largeur balayée limitée par la piste | Demande de l'auteur ; rayons supposés, sans mesure | aucune |
| H13 | Une piste non damée est lissée par la neige seule, sur L = k h ; chaque pente retenue est la plus forte des calculs avec et sans dameuse | Demande de l'auteur : la note sert au skieur qui hésite à s'engager, elle ne doit pas promettre une piste plus douce que damée. Les bosses ne sont pas chiffrées, faute de source | une classe de plus d'office pour les bosses (écartée, sans source) |
| H12 | Un virage coupé a un rayon égal au rayon de cotes du ski multiplié par le cosinus de l'angle de carre, pris à 45° | Relation géométrique du ski taillé, flexion et dérapage négligés | 30° et 60° à calculer |

## Ce qui reste ouvert

- Les seuils de T et de R n'ont pas de source publiée. Ils reprennent des repères d'usage pour les pistes damées. À notre connaissance, aucune norme française ne fixe de pente pour chaque couleur, et les normes de certains pays voisins ne se mesurent pas de la même façon. Une revue des normes et de la littérature reste à faire.
- R ne tient compte que du dénivelé : ni la longueur, ni les replats, ni l'altitude.
- L'angle θ dépend sans doute du niveau du skieur. Il faudra décider si T décrit la pente de la piste ou celle d'un skieur type.
