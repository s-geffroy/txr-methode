# Protocole de validation proposé

Le contrôle par les couleurs du plan n'est **pas** une validation : toutes les
corrections réduisent la pente et, sur sol nu, aucune piste n'est « plus
facile » que sa couleur, donc la conformité augmente mécaniquement avec
l'ampleur de la correction (angle de zigzag θ, largeur). À La Foux d'Allos,
42 pistes : 10, 20 puis 32 pistes conformes pour θ = 0°, 30° et 45°. Le
résultat robuste est la concordance de **rang** entre couleur et classe
(τ-b de Kendall ≈ 0,74), pas le niveau absolu des classes.

## Référence

Mesurer la pente **sur neige damée**, pas sur les couleurs.

- Unité : la fenêtre de 30 m (et de 10 m pour les murs courts), regroupée par piste.
- Instruments : GNSS RTK le long de la ligne de pente et de trajectoires
  réelles, ou inclinomètre étalonné.
- θ empirique : estimer l'angle de zigzag sur des traces GPS de skieurs de
  différents niveaux, plutôt que le supposer.

## Échantillonnage

- Stratifié par couleur et par classe T prédite, en surreprésentant les vertes
  et les noires (peu nombreuses).
- Environ 100 à 120 fenêtres : 2 à 3 par piste, dont la fenêtre critique
  prédite et une fenêtre tirée au hasard.
- Analyse par modèle mixte (effet aléatoire par piste).

## Métriques

- Pente : Bland-Altman (biais et limites d'accord) entre pente prédite et
  pente mesurée ; objectif |biais| < 2 points.
- Classe : kappa pondéré quadratique entre T prédit et T mesuré ; avec
  ~110 fenêtres, demi-largeur de l'intervalle ≈ 0,1.
- Appréciation : jury d'au moins trois moniteurs, notation en aveugle, accord
  mesuré par l'α de Krippendorff.

## Préenregistrement

Figer θ, L0, k, la largeur par défaut et les seuils **avant** la mesure, puis
valider sur une seconde station.
