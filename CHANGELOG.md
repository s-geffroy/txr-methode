---
title: Versions
description: "Versions successives de la méthode TxR et ce qui a changé."
---

# Versions

## 0.6.2 (17/11/2026)

- Les couleurs ne sont plus la référence : TxR cherche à les dépasser. La comparaison avec elles est présentée comme un contrôle (erreurs grossières, réglage déguisé), avec un vocabulaire neutre (« dans la plage », « au-dessus ») au lieu de « conforme ». Les résultats disent d'abord ce que TxR dit des pistes : la plupart des bleues ont au moins un passage de niveau rouge. Nouvelle section « Les couleurs des pistes » dans la méthode.

## 0.6.1 (17/11/2026)

- Résultats : l'accord avec les couleurs est donné pour la note affichée (ligne de pente), comparé au hasard, avec l'intervalle de confiance de l'accord corrigé du hasard (κ). Avec cette note, l'accord ne dépasse le hasard dans aucune station ; la note avec zigzag est donnée pour comparaison. La Foux est signalée comme station de réglage ; la pente moyenne sert de référence pour l'ordre des couleurs.
- Le programme de calcul affiche désormais partout la note de la ligne de pente, comme l'annonçait la méthode.
- Tracés incomplets : une piste dont OpenStreetMap ne dessine qu'une partie sort de l'accord avec les couleurs (Appliquer TxR à une station).
- Corrections de cohérence : version du programme, nombre de fiches, ordre des hypothèses, climatologie par secteur.

## 0.6.0 (16/11/2026)

- Pistes non damées : lissage par la neige seule (L = k h), pente la plus forte des calculs avec et sans dameuse, mention « non damée » (hypothèse H13). Déclaration par le plan ou par la station ; l'étiquette OpenStreetMap est seulement signalée.
- Résultats par station : Pra-Loup, Grand Tourmalet, Val d'Isère–Tignes.

## 0.5.2 (16/11/2026)

- DOI Zenodo dans le pied de page de chaque fiche, du panneau de bord de piste et dans les métadonnées des PDF.
- Citation et DOI sur la page d'accueil, dans le README et dans `CITATION.cff`.
- Indices écrits proprement dans le texte courant (h<sub>bas</sub>, p<sub>mur</sub>…).

## 0.5.1 (16/11/2026)

- Formules en notation mathématique, sur le site et dans les fiches.
- Bornes des tableaux en symboles (< 20 %, ≥ 45 %, < 200 m…).
- Panneau de bord de piste : demi-page A4 à afficher au départ des pistes.

## 0.5.0 (16/11/2026)

- Types de virages (godille, courts, moyens, grands) et lien avec le rayon des skis.
- Méthode du calcul 0.5 : relief interpolé, relations OpenStreetMap lues, pas de zigzag sous 10 m de largeur, tolérance d'orientation, paramètres de station.

## 0.4.1 (16/11/2026)

- Méthode valable pour toutes les stations, grille T × R, abaque d'enneigement, protocole de validation revu, fiches génériques.

## 0.4.0 (15/11/2026)

- Première publication.
