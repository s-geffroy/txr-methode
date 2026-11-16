---
title: Accueil
---

# TxR, noter une piste de ski avec deux chiffres

[![DOI 10.5281/zenodo.24280550](https://zenodo.org/badge/DOI/10.5281/zenodo.24280550.svg)](https://doi.org/10.5281/zenodo.24280550)

Une couleur de piste mélange deux choses : la difficulté du passage le plus raide et la longueur de la descente. TxR les sépare. La note **T**, de T0 à T6, dit à quel point le passage le plus raide est technique. La note **R**, de R0 à R5, dit l'effort que demande la descente, d'après son dénivelé. Une piste courte avec un mur peut ainsi valoir T5·R1, et une longue piste facile T1·R4. Un long tronçon facile ne rattrape pas un mur, et un mur ne rend pas une piste longue.

TxR est un travail de recherche. Ses seuils n'ont pas encore été vérifiés sur le terrain et ses notes ne remplacent pas le classement d'une station : sur les pistes, seul le balisage fait foi.

![Trois schémas : la pente d'un passage de 30 m, le zigzag dans la largeur de la piste, la neige qui comble les creux](figures/schemas-mesure.png)

## Ce que veulent dire T et R

Le tableau se lit en choisissant d'abord sa colonne (ce qu'on sait skier), puis sa ligne (la forme du jour). Les descriptions sont des repères provisoires. [La grille complète](GRILLE.md) détaille les sept colonnes et les six lignes.

| | T0–T1, < 20 % | T2, 20 à 25 % | T3–T4, 25 à 45 % | T5–T6, ≥ 45 % |
|---|---|---|---|---|
| **R0–R1**, < 200 m de dénivelé | Pente d'apprentissage, liaison | Bleue courte | Rouge courte, passage raide | Mur court |
| **R2–R3**, 200 à 700 m | Verte de retour, longue verte | Bleue classique, longue bleue | Rouge classique, noire soutenue | Noire avec un mur |
| **R4–R5**, ≥ 700 m | Route de vallée (rare) | Grande bleue de vallée | Grande descente sportive | Noire longue et engagée (rare) |

Les pourcentages sont ceux de la pente sur un passage de 30 m. Une pente de 25 % fait environ 14°, une pente de 45 % environ 24°.

## Comment on obtient les notes

On part du relief sans neige, mesuré par laser aéroporté avec un point au moins tous les mètres, et du tracé des pistes dans OpenStreetMap. On calcule la pente de chaque passage de 30 m, et de 10 m pour repérer les murs courts. On estime ensuite la piste réelle : on peut choisir son passage dans la largeur, et la neige comble les creux. T vient du passage le plus raide de cette piste estimée, R de son dénivelé. On calcule aussi la note d'un skieur qui descend en zigzag, mais la note affichée reste celle, plus prudente, de la descente dans l'axe.

La hauteur de neige change un peu la note, surtout sur les murs courts. Avec deux relevés, en bas et en haut du domaine, une station peut recalculer T à la main grâce à [l'abaque d'enneigement](ABAQUE.md). La façon de tourner et le rayon des skis changent aussi la pente que l'on suit réellement : la page [Virages et rayon des skis](VIRAGES.md) l'explique.

## Où en est-on

La méthode a été essayée sur les 42 pistes de La Foux d'Allos. Les pistes y sortent dans un ordre proche de celui de leurs couleurs. C'est encourageant, mais la pente moyenne seule donne déjà un ordre assez proche, et le niveau des notes dépend de nos hypothèses : selon l'angle de zigzag supposé, de 10 à 32 pistes tombent dans la classe de leur couleur. Le [compte rendu de l'essai](PILOTE.md) donne le détail. La même méthode, sans aucun réglage nouveau, a ensuite été appliquée à Pra-Loup, avec des résultats proches ([résultats par station](RESULTATS.md)). Le [protocole de validation](VALIDATION.md) décrit les mesures sur neige damée qui permettront de trancher.

## Documents

| Pour qui | Document |
|---|---|
| Skieurs, moniteurs | [Fiche skieurs (PDF, 3 pages)](fiches/grand-public.pdf) · [Grille T × R (PDF, 1 page)](fiches/grille.pdf) · [Virages et rayon des skis](VIRAGES.md) |
| Services des pistes | [Fiche exploitants (PDF, 3 pages, avec l'abaque)](fiches/exploitants.pdf) · [Abaque d'enneigement](ABAQUE.md) · [Panneau de bord de piste (PDF, demi-page A4)](fiches/panneau.pdf) |
| Spécialistes | [Fiche technique (PDF)](fiches/technique.pdf) · [Méthode complète](METHODE.md) · [Hypothèses](HYPOTHESES.md) |
| Autres stations | [Appliquer TxR à une station](STATIONS.md) |
| Tous | [Résultats par station](RESULTATS.md) · [Essai à La Foux d'Allos](PILOTE.md) · [Protocole de validation](VALIDATION.md) · [Versions](CHANGELOG.md) |

## Citer, réutiliser

Les textes, fiches et figures sont sous licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/deed.fr) : on peut les reprendre librement en citant la source. Pour citer : Geffroy, S. (2026). *TxR, méthode de classement des pistes de ski en technique et résistance*, version 0.5.2. Zenodo. [https://doi.org/10.5281/zenodo.24280550](https://doi.org/10.5281/zenodo.24280550)

Archive et DOI : [Zenodo](https://doi.org/10.5281/zenodo.24280550) (toutes versions) · [version 0.5.2](https://doi.org/10.5281/zenodo.24280769) · [version 0.5.1](https://doi.org/10.5281/zenodo.24280551).

Les chiffres de l'essai sont des résultats agrégés, calculés à partir de données © contributeurs [OpenStreetMap](https://www.openstreetmap.org/copyright) (ODbL 1.0), de l'IGN et de Météo-France (Licence Ouverte Etalab 2.0). Aucune base de données n'est diffusée ici. Ce travail est indépendant des exploitants des stations citées.

[Sources sur GitHub](https://github.com/s-geffroy/txr-methode)
