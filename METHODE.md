---
title: Méthode de calcul TxR (v0.4.0)
---

> Ce document décrit la méthode telle qu'elle est implémentée dans TxR v0.4.0 (code non publié à ce stade). Les noms de fonctions et de fichiers renvoient à cette implémentation.

# Méthode de calcul TxR (v0.4.0)

## Glossaire

- **Piste** : une entrée du plan officiel (nom + couleur), identifiant `piste_id`. Unité du contrôle par les couleurs.
- **Trace** (ou composante) : une ligne continue calculée pour une piste, `trace_id` ; une piste peut en avoir plusieurs, elle prend alors la classe la plus haute.
- **Tronçon** : un way OSM (`troncon_id = W<osm_id>`), brique d'une trace.
- **Fenêtre** : portion de W m (10, 30 ou 100) sur laquelle on mesure une pente.
- **Classe T « provisoire »** : borne inférieure (« T3 » = « au moins T3 »).
- **Convention trajectoire** : pente de la trajectoire skiée en zigzag à θ = 30° de l'axe (hypothèse).
- **Convention ligne de pente** : pente de la piste dans sa propre direction, sans zigzag. À ne pas confondre avec le drapeau `axe_ligne_de_pente` (affiché « axe face à la pente »), qui signale un pic où l'axe OSM suit la ligne de plus grande pente du **terrain**.


## Géométrie

- **Source.** OpenStreetMap, ways `piste:type=downhill`. Les lignes sont projetées en Lambert-93 (EPSG:2154) ; toutes les distances sont planimétriques.
- **Assemblage.** Deux ways d'une même entrée ne sont joints que s'ils partagent un **nœud OSM** de degré 2 dans cette entrée. Un nœud de degré supérieur à 2 (embranchement) coupe la chaîne. Des extrémités à moins de 5 m sans nœud commun sont consignées dans `raccords` et ne sont pas assemblées. Les composantes disjointes gardent des profils distincts.
- **Orientation.**
  - La trace est orientée vers l'aval d'après les altitudes de ses extrémités (IGN, ou MNT LiDAR à défaut).
  - Le sens de numérisation OSM (`sens_osm`) est comparé à ce résultat ; un désaccord est signalé par `desaccord_sens_osm`.
  - Égalité ou altitude manquante : orientation indéterminée, aucune pente calculée.

## Profils (D15-B)

- **Pas de référence.** IGN RGE ALTI au pas de 5 m (lots de 120 points, cache par empreinte de l'URL exacte). Les deux extrémités sont toujours conservées.
- **Affinage.**
  - Il se fait sur le MNT LiDAR HD (dalles de 1 km à 0,5 m, WMS-R de la Géoplateforme), aux pas de 5, 2 et 1 m.
  - Il est déclenché si l'orientation est déterminée, si les dalles couvrent au moins 99 % des points et si la maille est inférieure ou égale au pas.
  - Les valeurs échantillonnées sont mises en cache par empreinte des points et des dalles : le rejeu hors ligne n'a pas besoin des dalles.
- **Altitude absente.** Elle reste nulle, avec son motif (`erreur`).

## Pentes (D14-B)

- **Définition.** La pente descendante signée sur la fenêtre [s, s+W] vaut 100 · (z(s) − z(s+W)) / W. L'altitude en s+W est interpolée linéairement entre deux échantillons valides.
- **Fenêtres écartées** :
  - celles qui dépassent l'extrémité du tracé ;
  - celles qui contiennent une altitude nulle ;
  - celles qui ne respectent pas le **critère de résolution** : W ≥ 3 × max(pas, maille nominale).

  La maille nominale (1 m pour RGE ALTI, 0,5 m pour le LiDAR) n'est **pas** une précision locale. La v0.1.0 n'appliquait le critère qu'à la maille, ce qui laissait passer des fenêtres de 10 m au pas de 5 m.
- **Statistiques par profil et par échelle** : n, Gmax, P50, P90, P95. S'y ajoutent la position du Gmax et la pente maximale du terrain au même endroit (gradient du MNT sur W, en x et en y).

  `axe_ligne_de_pente` est vrai si la pente de l'axe atteint au moins 90 % de cette pente maximale. C'est une condition d'artefact possible (axe imprécis, talus), **pas une preuve** : le maximum se trouve naturellement là où l'axe s'aligne sur la pente.

## Convergence

- **Principe.** Pour une même source, les indicateurs Gmax, P90 et P95 sont comparés entre pas successifs (5 → 2 → 1 m).
- **Tolérance.** Elle vaut 400 · u / W points, pour une borne verticale déterministe u.
- **Sans borne u.** Si aucune source primaire ne documente u, le statut est « incertitude inconnue ».
- **Hypothèse de sensibilité.** La colonne `statut_hypothese` applique u = 0,10 m au LiDAR HD. Cette valeur cible du programme n'a été relevée que dans des sources secondaires.
- **Comparaison inter-sources.** IGN 5 m contre LiDAR 5 m, à titre informatif.
- **Limites.** Ce contrôle ne couvre ni l'erreur de position de l'axe, ni l'effet de la méthode d'échantillonnage, ni la surface sous la neige.

## Indicateurs retenus

- **Choix du profil.** Pour chaque échelle, on retient le pas le plus fin de la meilleure source (LiDAR si son profil est complet) qui donne au moins une fenêtre.
- **Indicateurs de la trace** :
  - `longueur_m` (horizontale) ;
  - `denivele_m` (différence d'altitude des extrémités) ;
  - `pente_moyenne_pct` = 100 · Δz / L ;
  - `longueur_3d_m` ;
  - longueurs, fractions et continuités au-dessus des seuils `seuils_effort_pct` ;
  - `histogramme_30m` (classes de 5 %).
- **Fiabilité.** Chaque indicateur porte sa source, son pas et sa fiabilité (table `indicateurs`).

## Classement (D13-C, D12-B)

- **T.** Deux familles de règles, critiques et soutenues, combinées par `T = max(T_critique, T_soutenu)` : une règle déclenchée ne peut pas être compensée.
  - `définitif` exige toutes les règles évaluables, des indicateurs convergés, aucune règle expérimentale, aucun pic à confirmer, et une largeur, un dévers et des obstacles connus. **Aucune trace ne peut l'atteindre aujourd'hui.**
  - Sinon : `borne_provisoire` (T ≥ borne) ou `non_déterminé`.
  - Pic à confirmer : une règle critique déclenchée sur une étendue inférieure à 2 × W.
- **R.** Somme de composantes `poids × valeur / échelle`. Une composante manquante rend le score non déterminé.
- **Configuration réelle** (`regles/regles-0.2.0.json`) : aucun seuil, aucun poids. Les seuils du fil sont isolés dans `regles/proposition-fil.json` (expérimental).
- **E et C** restent nuls, avec leur motif.

## Reproductibilité

- **Une exécution par répertoire.** Chaque exécution écrit dans un nouveau répertoire, avec `config.json` et `provenance.json` (empreintes des sources, de l'inventaire et des règles, lots de cache utilisés, dalles).
- **Reprise.** Une exécution interrompue (`EN_COURS`) reprend trace par trace avec la même configuration. Une exécution terminée (`TERMINE`) n'est jamais réécrite.
- **Rejeu hors ligne.** Il relit uniquement les caches et doit redonner des tables identiques : contrôle `comparaison_execution.json`.
- **Rejeu compatible v0.1.0** (`python -m txr compat`). Il reproduit les chiffres publiés et les valeurs de la v0.1.0 : contrôle `controle_v010.json`.

## Pente skiable estimée (expérimental, v0.3.0, corrigée en v0.4.0)

`python -m txr correction` (étapes 5 et 6 du pilote). Elle ramène la mesure faite sur le sol nu vers la pente de la piste damée, pour lui appliquer les repères des normes (`regles/normes-damees-corrige.json`, échelle T du fil). Les seuils ne sont **pas** calés sur les couleurs : celles-ci ne servent qu'au contrôle (`validation.json`).

- **Couloir.** Largeur mesurée perpendiculairement à l'axe sur les polygones de surface de piste OSM (`piste:type=downhill`, `area=yes`, hors freeride). Il faut au moins 5 mesures et 30 % de la trace couverte ; sinon, on prend la médiane des largeurs mesurées.
  - Des lignes parallèles sont tracées tous les 2 m, jusqu'à 1 m du bord, puis échantillonnées au pas de 1 m sur le LiDAR.
  - Chaque point d'une parallèle est pris **en face** du point de l'axe, par projection perpendiculaire locale (v0.4). La v0.3 appliquait un rapport de longueur global, qui faisait dériver les parallèles dans les virages (15 m en médiane à ±16 m).
  - Une fenêtre fait W m **le long de chaque ligne** ; elle est écartée si elle dépasse la fin de la ligne ou contient une lacune (pas d'extrapolation).
  - Pour chaque fenêtre, on retient la ligne la moins raide.
  - Ces lignes parallèles corrigent la position de l'axe, pas sa direction.
  - Publié : `largeur_m` (largeur retenue), `largeur_effective_m` (couloir réellement échantillonné, au plus 40 m) et `paralleles_ecartees` (lignes vides, en plusieurs morceaux ou de longueur hors de [0,7 ; 1,3] × axe).
  - Une trace dont aucune fenêtre ne descend sur sol nu (Gmax30 ≤ 0) n'est pas classée : statut « orientation à confirmer ».
- **Descente en biais.** La trajectoire skiée s'écarte de l'axe d'un angle θ, en zigzag symétrique, sans sortir du couloir. La référence est θ = 30°, avec 0° et 45° en sensibilité.
  - Sur une fenêtre de W m de trajectoire (longueur horizontale), le skieur avance de W·cos θ le long de l'axe et revient à son décalage de départ.
  - Pente = (z départ − z arrivée)/W sur une même ligne parallèle ; on garde la plus faible du couloir. Pour θ = 0, on retrouve les lignes parallèles.
  - Sur un plan, la pente est multipliée par cos θ (0,87 à 30°, 0,71 à 45°). Un mur court pèse davantage, car l'avance sur l'axe est plus courte.
  - Le dévers n'est pas exploité. Un premier essai laissait la trajectoire finir chaque fenêtre plus haut sur le côté ; il donnait des pentes nulles ou négatives (médiane des vertes 1,9 %), ce qui revenait à traverser à plat d'une fenêtre à l'autre. Il a été abandonné.
- **Deux conventions de mesure**, calculées côte à côte (choix de l'utilisateur du 14/11/2026 : « les deux ») :
  - **trajectoire** (`t_borne`) : pente de la trajectoire skiée, avec un biais de 30° ;
  - **ligne de pente** (`t_borne_ligne_pente`) : pente de la piste dans sa direction, sans biais. Ce sont les lignes parallèles lissées, indicateurs `*_paralleles`.
  - La ligne de pente suit la direction de la piste, pas la ligne de plus grande pente du terrain : celle-ci classerait un chemin tracé en travers d'un versant comme le versant lui-même.
- **Règle expérimentale « mur court »** (`nd-M10-*`) : Gmax10 skiable ≥ 40 / 50 / 60 / 75 % ⇒ T ≥ 3 / 4 / 5 / 6.
  - Ce sont les seuils de Gmax30 relevés de 15 points, pour un passage de 10 m. Ils sont proposés sans calibration.
  - C'est par cette règle que l'enneigement agit sur T, car le lissage (5 à 15 m) est du même ordre que la fenêtre.
- **Neige.** L'abaque `data/neige/abaque-s2m-massif22.json` est construite avec `python -m txr abaque` sur la réanalyse S2M de Météo-France (massif 22, saisons 1996–2026). Elle donne les centiles P20/P50/P80 de la hauteur de neige naturelle par mois, altitude (pas de 300 m), exposition et pente.
  - Au point considéré, h est interpolée en altitude ; l'exposition et la pente du terrain sont calculées sur le LiDAR à ±5 m.
  - Le profil est lissé par une moyenne glissante de longueur L = L0 + k·h, où L0 représente le pontage de la dameuse et k le comblement par la neige. Près d'une extrémité ou d'une lacune, la fenêtre rétrécit pour rester centrée : une pente constante n'est pas aplatie aux bords.
  - Une épaisseur uniforme ne change pas la pente.
  - La neige de culture et le tassement ne sont pas représentés.
- **Scénarios de sensibilité** :

  | Paramètre | Valeur de référence | Variantes testées |
  |---|---|---|
  | Saison et centile | février P50 | décembre P20, mars P80 |
  | Lissage (L0, k) | (5, 5) | sans neige, (10, 10) |
  | Couloir | largeur OSM | axe seul, 20 m, 40 m |
  | Biais θ | 30° | 0°, 45° |
- **Indicateurs** : `gmax{10,30,100}_{brut,neige,couloir,paralleles,skiable}` et `p95_*` correspondants.
  - `brut` est identique à la mesure du pipeline principal (contrôle).
  - `couloir` : lignes parallèles sur sol nu.
  - `paralleles` : lignes parallèles lissées par la neige (θ = 0).
  - `skiable` : couloir lissé, avec descente en biais.

## Abaque fonction du relevé de neige (expérimental, v0.3.0)

Le relevé à fournir est la **hauteur totale** de neige en bas et en haut de station, comme dans les bulletins quotidiens. Les deux points sont à 1 800 m et 2 600 m (`STATION` dans `correction.py`), altitudes confirmées par l'utilisateur le 14/11/2026.

- **Hauteur en chaque point de l'axe** : h = [(1 − t)·h_bas + t·h_haut] × f.
  - t est la position en altitude entre les deux points, bornée à [0, 1].
  - f vaut S2M(z, exposition, pente, mois) / S2M(z, plat, mois), borné à [0, 3]. Il reporte l'effet de l'exposition et de la pente vu dans la climatologie.
  - Le mois est celui de la date du relevé.
- **Suite du calcul** : identique à la référence (L = 5 + 5·h, couloir), pour les deux conventions. T se déduit de Gmax30, P95₃₀ et Gmax10 par `regles/normes-damees-corrige.json`.
- **Sorties** :
  - `abaque_releve_1d` : par trace, T selon h_bas de 0 à 150 cm par pas de 10 cm, avec h_haut = h_bas × gradient S2M de février. Le rapport en tire, pour chaque piste, le seuil en cm où la classe change.
  - `abaque_releve_2d` : grille complète h_bas (0–300 cm, pas de 50) × h_haut (0–500 cm, pas de 50). La page visuelle l'interpole.
  - `python -m txr cotation --bas CM --haut CM [--date AAAA-MM-JJ]` : calcul exact pour un relevé, sans réseau, à partir du cache d'échantillonnage. Il écrit `/state/cotations/<date>-bas<b>-haut<h>/cotation.{json,parquet}`.
- **Limites** :
  - La hauteur relevée sur piste comprend la neige de culture et le tassement ; S2M ne sert qu'aux rapports entre points.
  - Sur des fenêtres de 30 m, la neige agit peu, car le lissage reste plus court que la fenêtre. L'abaque varie donc surtout sur les pistes proches d'un seuil.

## Contrôle par les couleurs du plan (v0.4.0)

Ce n'est **pas une validation**. Les corrections réduisent toutes la pente et, sur sol nu, aucune piste n'est « plus facile » que sa couleur : la conformité augmente donc mécaniquement avec l'ampleur de la correction (θ, largeur). Les hypothèses V3-1 à V3-6 ([hypothèses](HYPOTHESES.html)) ont été fixées pendant l'analyse.

- Unité : la **piste** (classe la plus haute de ses composantes) ; variantes sans couleur exclues ; classes attendues verte T0–1, bleue T1–2, rouge T3–4, noire T4–6 (les noires sont conformes par construction dès T4).
- Publié dans `validation.json` (`pistes`, `scenarios`) et au §8 bis du rapport :
  - conformité observée et **attendue au hasard** (même répartition des classes, indépendante de la couleur), accord corrigé du hasard, intervalle bootstrap à 95 % ;
  - **τ-b de Kendall** entre le rang des couleurs et la classe : concordance d'ordre, indépendante du niveau absolu des seuils ;
  - conformité pour chaque scénario de sensibilité, dans les deux conventions.
- Validation à faire : mesures de pente sur neige damée (GNSS RTK ou inclinomètre), 100 à 120 fenêtres stratifiées par couleur et par T prédit, accord par Bland-Altman et κ pondéré, θ estimé sur des traces GPS de skieurs, paramètres figés avant la mesure (voir le [protocole de validation](VALIDATION.html)).
