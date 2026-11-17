---
title: Appliquer TxR à une station
description: "Appliquer TxR à une station de ski : données nécessaires, paramètres, contrôles et cas particuliers (pistes non damées, tracés incomplets)."
---

# Appliquer TxR à une station

La méthode est la même partout. Ce qui change d'une station à l'autre, ce sont les données d'entrée et quelques paramètres, rassemblés ici. Les constantes de la méthode (seuils, θ, L0, k, longueurs des passages) ne se règlent jamais sur une station : sinon, les notes de deux stations ne seraient plus comparables.

## Les paramètres d'une station

| Paramètre | À quoi il sert | Exemple : La Foux d'Allos | Comment le déterminer |
|---|---|---|---|
| Nom et emprise | en-têtes, extraction des données | La Foux d'Allos ; enveloppe des pistes | enveloppe des pistes du plan, plus 500 m |
| Projection de calcul | distances et pentes | Lambert-93 (EPSG:2154) | projection conforme nationale ou UTM ; jamais la projection « Web Mercator » des fonds de carte, qui fausse les distances ; le programme refuse une projection qui déforme les distances de plus de 0,5 % au centre du domaine |
| MNT de référence et MNT fin | profils en long | RGE ALTI 1 m ; LiDAR HD 50 cm | voir plus bas |
| Liste des pistes | unité de la note | 42 pistes du plan officiel | plan de la saison, rapproché des tracés OpenStreetMap |
| Système de couleurs | comparaison avec les couleurs (contrôle) | vert, bleu, rouge, noir | norme ou usage du pays |
| Climatologie de la neige | facteur d'orientation | S2M, massif Haut-Var/Haut-Verdon | massif ou massifs qui couvrent le domaine |
| Points de relevé de neige | neige du jour | 1 800 m et 2 600 m | points du relevé quotidien, avec leur altitude ; un couple par secteur si le domaine en a plusieurs |
| Largeur par défaut | pistes sans surface dessinée | 35 m (médiane mesurée) | médiane des largeurs mesurées dans la station |
| Largeur minimale de zigzag | pas de traversées en dessous | 10 m | constante conseillée, à ne changer qu'avec une raison |
| Tolérance d'orientation | tracés presque plats | 0,5 m | environ deux fois l'erreur verticale du MNT |
| Date des données | reproductibilité | extrait OpenStreetMap du 14/11/2026 | date de l'extraction |

## Le relief

Il faut un MNT de sol nu, sans arbres ni bâtiments. La finesse du MNT décide de ce qu'on peut calculer : un passage de longueur W demande un profil au moins trois fois plus fin que W. Le tableau donne ce minimum. En pratique, nous conseillons un MNT LiDAR d'un mètre ou mieux, car la maille annoncée surestime souvent la finesse réelle.

| Finesse du MNT | Ce qu'on peut calculer |
|---|---|
| jusqu'à 3 m | toutes les règles, y compris le mur court sur 10 m |
| de 3 à 10 m | passages de 30 m ; le mur court ne peut pas être évalué et T peut être sous-estimé |
| plus de 10 m | sections de 100 m seulement : pas de note T |

En France, le LiDAR HD de l'IGN couvre progressivement tout le territoire. Ailleurs, beaucoup de pays ou de régions diffusent un MNT LiDAR de 0,5 à 2 m (en Suisse, en Autriche, dans plusieurs régions italiennes et en Espagne, par exemple) ; il faut vérifier, pour chacun, qu'il s'agit bien d'un sol nu et connaître sa précision verticale. Les modèles mondiaux à 30 m, comme Copernicus, ne conviennent pas : ils sont trop grossiers, et la plupart décrivent la surface (forêts comprises) plutôt que le sol.

## Les tracés OpenStreetMap

Avant de calculer, on contrôle que la station est bien dessinée dans OpenStreetMap. Les seuils ci-dessous sont des propositions :

- au moins 95 % des pistes du plan sont retrouvées ;
- chaque piste forme un seul morceau, sauf variantes ;
- aucune extrémité proche d'une autre sans point commun ;
- moins de 10 % des tracés dessinés dans le sens de la montée ;
- des surfaces de piste couvrant au moins 30 % de la longueur pour au moins la moitié des pistes ; sinon la largeur par défaut s'applique et c'est signalé ;
- des géométries valides, sans boucle.

Quand un contrôle échoue, on corrige d'abord les données dans OpenStreetMap, ce qui profite à tout le monde. Les pistes saisies sous forme de relations, fréquentes dans certains pays, sont lues comme les autres : leurs lignes reprennent les étiquettes de la relation. Les surfaces de piste saisies en plusieurs morceaux (multipolygones) servent aussi à mesurer la largeur, toujours sur la surface de la piste concernée et non sur l'ensemble des surfaces voisines.

## Les pistes non damées

Une piste balisée et sécurisée mais non damée se déclare de deux façons : d'après le plan officiel, quand sa légende la distingue (à Tignes – Val d'Isère, les pistes « Naturide »), ou par une liste de pistes dans les paramètres de la station. Toute la piste est alors traitée comme non damée, variantes comprises, sauf si une variante est déclarée à part. Une piste non damée sur une partie seulement de son tracé n'est pas prévue.

OpenStreetMap indique parfois qu'une piste n'est pas damée (étiquette `piste:grooming`). Cette information, souvent posée sur un seul tronçon, est seulement signalée comme à vérifier : elle ne change pas la note.

## Les tracés incomplets

Il arrive qu'OpenStreetMap ne dessine qu'une partie d'une piste. Noter ce morceau comme s'il s'agissait de toute la piste fausserait la comparaison avec sa couleur. La station peut donc déclarer une piste « tracé incomplet » : elle reste notée sur le tronçon dessiné, avec cette mention, mais sort de l'accord avec les couleurs. Une longueur minimale automatique a été écartée, car de vraies liaisons ne font que 120 à 150 m. Une piste dont aucun passage ne descend (tronçon mal orienté) ne reçoit pas de note et sort elle aussi de l'accord.

## La neige

En France, la réanalyse S2M de Météo-France couvre les Alpes, les Pyrénées et la Corse, à notre connaissance. Ailleurs, et dans les massifs qu'elle ne couvre pas (Vosges, Jura, Massif central), on peut utiliser une autre climatologie de la neige par altitude et orientation, ou, à défaut, faire le calcul sans facteur d'orientation (f = 1). La climatologie doit couvrir toutes les altitudes du domaine. Un domaine sur plusieurs versants utilise un couple de points de relevé par secteur, avec la même climatologie ; un domaine à cheval sur deux massifs prend, à ce jour, la climatologie du massif principal.

## Les couleurs

La comparaison avec les couleurs, qui sert de contrôle, n'a de sens qu'à l'intérieur d'un même système. En France : verte, bleue, rouge, noire. En Suisse et en Autriche, il n'y a pas de verte, et il existe des itinéraires balisés autrement. En Amérique du Nord, les symboles sont différents. Pour chaque système, on écrit à l'avance quelles classes T on attend pour chaque couleur, avec la source.

## Dans quel ordre

1. Remplir les paramètres de la station.
2. Choisir le MNT et vérifier qu'il est de sol nu, assez fin, et qu'il couvre au moins 99 % des tracés.
3. Extraire les tracés OpenStreetMap et les contrôler.
4. Rapprocher les pistes du plan et leurs tracés, avec les secteurs et les liaisons vers les domaines voisins.
5. Choisir la climatologie de la neige et les points de relevé.
6. Calculer, puis refaire le calcul sans réseau et vérifier que les résultats sont identiques.
7. Examiner les contrôles de sortie : part des passages calculables, stabilité des mesures, tracés non orientés, passages signalés.
8. Ne publier les notes d'une piste qu'avec l'accord de la station.
