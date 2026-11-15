# TxR : méthode (fiche technique)
> La Foux d'Allos · TxR v{{version}} · pilote {{empreinte}} · résultats provisoires, seuils non calibrés

## Principe
Deux axes non compensatoires : **T** (technique, T0–T6) = max(T critique, T soutenu) ; **R** (résistance physique, R0–R5) sur le dénivelé net. Exposition E et conditions C sont des indicateurs séparés (non renseignés).

## Données
- Axes : OpenStreetMap (ODbL), instantané du 14/11/2026, continuité par nœuds partagés, sens contrôlé par les altitudes et la numérisation.
- MNT : RGE ALTI 5 m (API IGN) puis **LiDAR HD 0,5 m** (WMS-R Géoplateforme, 26 dalles) ; profils au pas de 5, 2 et 1 m.
- Neige : réanalyse **S2M** Météo-France (massif 22, 1996–2026), centiles par mois, altitude, exposition et pente.

## Mesure
[[schemas]]
- Pente descendante sur fenêtres horizontales de 10, 30 et 100 m, glissées au pas ; une fenêtre n'est admise que si **W ≥ 3 × max(pas, maille)**. Convergence entre pas avec tolérance 400·u/W (u = 0,10 m, hypothèse).
- **Correction vers la piste damée** (expérimentale ; parallèles recalées par projection sur l'axe) : couloir de largeur OSM ({{n_osm}} traces) ou médiane {{largeur}} m, parallèles tous les 2 m ; lissage par moyenne glissante L = 5 + 5·h (h issu de l'abaque ou du relevé bas/haut, modulé par le rapport S2M exposition/plat) ; **trajectoire** : zigzag symétrique à θ = 30°, pente = Δz(W·cos θ)/W, sans gain latéral (dévers non exploité) ; **ligne de pente** : θ = 0.
- Indicateurs : Gmax10, Gmax30, P95₃₀, Gmax100, Ḡ = Δz/L, longueur 3D.

## Règles (regles/normes-damees-corrige.json)
T critique sur Gmax30 : 10 / 20 / 25 / 35 / 45 / 60 % ⇒ T1–T6 ; mur court Gmax10 : 40 / 50 / 60 / 75 % ⇒ T3–T6 ; T soutenu : P95₃₀ ≥ 40 % ⇒ T4. R sur Δz : 80 / 200 / 400 / 700 / 1 100 m ⇒ R1–R5. Statuts : non déterminé, borne provisoire, définitif (jamais atteint ici).

## Contrôle par les couleurs (pas une validation)
Unité : la piste (classe max des composantes). Classes attendues : verte T0–1, bleue T1–2, rouge T3–4, noire T4–6 (noires conformes par construction dès T4). Toutes les corrections réduisent la pente : la conformité croît avec θ et la largeur (θ = 0/30/45° : {{c_th0}}/{{c_th30}}/{{c_th45}} pistes). Hasard : {{hasard}} ; accord corrigé {{kappa}} ; τ-b de rang {{tau}}. θ, L0, k et la largeur médiane ont été fixés pendant l'analyse (DECISIONS V3). Tracés conformes : sol nu {{conf_sol}}/{{n}}, trajectoire {{conf_traj}}/{{n}}, ligne de pente {{conf_lp}}/{{n}} ; par piste (classe max des composantes) : {{p_sol}}, {{p_traj}} et {{p_lp}}/{{p_n}}. Gmax30 médian des bleues : {{bleue_sol}} % (sol nu) → {{bleue_traj}} % (trajectoire). Rejeu hors ligne identique ; rejeu v0.1.0 exact.

## Limites
Seuils et poids non calibrés ; hypothèses L0, k, θ, u ; neige de culture et damage non modélisés ; largeur, dévers, obstacles, E et C absents ; validation terrain sur neige damée à faire.

## Sources
{{sources}}
