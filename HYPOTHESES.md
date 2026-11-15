---
title: Choix de méthode et hypothèses
---

# Choix de méthode et hypothèses

Ce document liste les choix de conception (F1–F7) et les hypothèses de la correction expérimentale (V3, V4), avec leur source et les variantes essayées. Les hypothèses V3 ont été fixées pendant l'analyse, sans préenregistrement : elles doivent être confirmées par des mesures sur neige damée.

## Choix explicites du fil d'origine (numérotation D non confirmée)

| Réf. | Choix dans le fil | Prise en compte |
|---|---|---|
| F1 | Classement **universel**, comparable entre stations (réponse à la question 1) | Méthode de mesure imposée et versionnée ; aucun seuil propre à La Foux. |
| F2 | Code **T×R** plutôt que 4 couleurs (question 2) | T et R séparés. La couleur officielle est conservée à part, jamais dérivée. |
| F3 | Le standard de mesure doit être imposé (axe, pas de 5 m, fenêtre de 30 m, Gmax30, G95) | Repris et étendu par D14-B (10/30/100 m). Écarts documentés : fenêtre glissante avant, pas de fenêtre centrée (mêmes valeurs, décalées de 15 m) ; distance horizontale (D14-B), pas « au sol » ; Ḡ = Δz/L, pas la moyenne des g30. G95 exporté en `p95_*`. |
| F4 | Seuils T0–T6 sur Gmax30, règle « G95 ≥ 40 % ⇒ T ≥ T4 », R sur le dénivelé V | **Non validés** (prompt : pas de seuils non validés en configuration réelle). Isolés dans `regles/proposition-fil.json`, marqués expérimentaux. Ne produisent que des bornes provisoires. |
| F5 | Largeur minimale et damage en **tags**, hors TxR | Balises OSM `width`, `piste:width`, `piste:grooming` reprises dans `txr.tags_osm`. Largeur utile consignée comme manque. |
| F6 | MNT maîtrisé : RGE ALTI ≥ 5 m, idéalement LiDAR HD | RGE ALTI 1 m échantillonné à 5 m, plus LiDAR HD 0,5 m échantillonné à 5/2/1 m. |
| F7 | Nom : TxR = *Technical × Resistance* (précisé le 14/11/2026 ; le fil disait « Technical–Range ») | R = exigence physique (résistance), conformément au prompt. |

## Hypothèses de la correction expérimentale (v0.3 et v0.4)

Ces choix ont été fixés **pendant l'analyse, sans préenregistrement** : les
conformités aux couleurs étaient déjà visibles quand certains ont été arrêtés.
Ils sont donc à confirmer par des mesures sur neige damée avant toute
validation. Les variantes essayées sont toutes listées.

| Réf. | Choix | Source et contexte | Variantes essayées |
|---|---|---|---|
| V3-1 | Couloir de la largeur de piste, parallèles tous les 2 m, ligne la moins raide par fenêtre | Utilisateur, 14/11 (« lissage + couloir ») | axe seul ; couloir de 20 m et de 40 m (sensibilité) |
| V3-2 | Largeur : polygones OSM si ≥ 5 mesures et 30 % couverts, sinon médiane des largeurs mesurées (35 m, 16 traces) | Choix technique, sans source externe | — |
| V3-3 | Lissage neige L = L0 + k·h, L0 = 5 m, k = 5 ; h de l'abaque S2M (février P50) ou du relevé | Hypothèse de travail, sans source externe | L0 = k = 0 ; L0 = k = 10 ; décembre P20 ; mars P80 |
| V3-4 | Descente en biais θ = 30° (zigzag symétrique, sans gain latéral) | Choisi parmi 0/30/45° proposés à l'utilisateur, qui a demandé les trois en scénarios ; 30° retenu en référence **après** avoir vu les conformités | θ = 0° et 45° (scénarios). Une première version qui laissait finir la fenêtre plus haut sur le côté (dévers exploité) a été **abandonnée** après avoir vu des pentes nulles ou négatives (vertes à 1,9 %). |
| V3-5 | Deux conventions publiées : trajectoire skiée (θ = 30°) et ligne de pente de la piste (θ = 0) | Utilisateur, 14/11 (« fais les deux ») | — |
| V3-6 | Règle « mur court » : Gmax10 ≥ 40/50/60/75 % ⇒ T ≥ 3/4/5/6 (seuils de Gmax30 + 15 points) | Utilisateur, 14/11 (accord pour une règle expérimentale) ; valeurs proposées sans calibration | — |
| V3-7 | Relevé de neige en bas (1 800 m) et en haut (2 600 m) de station | Altitudes confirmées par l'utilisateur, 14/11 | — |
| V4-1 | Parallèles prises en face de l'axe (projection locale) ; fenêtre = W m le long de chaque ligne | Correction d'un défaut géométrique relevé par la revue du 15/11 | rapport de longueur global (v0.3, abandonné) |
| V4-2 | Contrôle par les couleurs au niveau des pistes, comparé au hasard, avec τ-b de rang ; présenté comme contrôle | Revue du 15/11 (validité statistique) | comptage par traces (v0.3) |
