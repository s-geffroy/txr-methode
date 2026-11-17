# TxR, méthode de classement des pistes de ski

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24280550.svg)](https://doi.org/10.5281/zenodo.24280550)

TxR note une piste de ski avec deux chiffres plutôt qu'une couleur : **T**, de T0 à T6, pour la difficulté technique du passage le plus raide, et **R**, de R0 à R5, pour l'effort que demande le dénivelé. La méthode vaut pour n'importe quelle station ; elle a été essayée pour la première fois à La Foux d'Allos (Alpes-de-Haute-Provence).

C'est un travail de recherche : les seuils et les corrections n'ont pas encore été vérifiés sur le terrain, et les notes ne remplacent pas le classement ni le balisage des stations.

Site : https://s-geffroy.github.io/txr-methode/

## Contenu

| Fichier | Contenu |
|---|---|
| [index.md](index.md) | page d'accueil du site |
| [METHODE.md](METHODE.md) | le calcul complet |
| [GRILLE.md](GRILLE.md) | la grille T × R, avec une description de piste par case |
| [ABAQUE.md](ABAQUE.md) | ajuster la note T à l'enneigement, à la main |
| [VIRAGES.md](VIRAGES.md) | types de virages et rayon des skis |
| [STATIONS.md](STATIONS.md) | appliquer TxR à une station : paramètres, données, contrôles |
| [HYPOTHESES.md](HYPOTHESES.md) | principes et hypothèses, avec les variantes essayées |
| [RESULTATS.md](RESULTATS.md) | résultats par station, chiffres agrégés par couleur |
| [PILOTE.md](PILOTE.md) | l'essai à La Foux d'Allos, chiffres agrégés |
| [VALIDATION.md](VALIDATION.md) | le protocole de validation proposé |
| [CHANGELOG.md](CHANGELOG.md) | historique des versions |
| [fiches/](fiches/) | fiches PDF : skieurs, services des pistes (avec l'abaque), technique, grille, panneau de bord de piste (A5) |
| [fiches/sources/](fiches/sources/) | textes des fiches |
| [outils/construire.py](outils/construire.py) | régénère les figures et les fiches (numpy, matplotlib, reportlab) |

## Citer

Geffroy, S. (2026). *TxR, méthode de classement des pistes de ski en technique et résistance*, version 0.7.0. Zenodo. https://doi.org/10.5281/zenodo.24280550

Le DOI 10.5281/zenodo.24280550 désigne toujours la dernière version ; chaque version a aussi le sien : 0.6.2, 10.5281/zenodo.24314766 ; 0.6.0, 10.5281/zenodo.24308019 ; 0.5.2, 10.5281/zenodo.24280769 ; 0.5.1, 10.5281/zenodo.24280551.

Le fichier [CITATION.cff](CITATION.cff) donne les mêmes informations sous forme lisible par les logiciels (bouton « Cite this repository » sur GitHub).

## Licences

Les textes, fiches et figures sont sous licence Creative Commons Attribution 4.0 International ([LICENSE](LICENSE)). Le script `outils/construire.py` est sous licence EUPL-1.2 ([outils/LICENSE-EUPL-1.2.txt](outils/LICENSE-EUPL-1.2.txt)). L'implémentation complète de TxR n'est pas publiée à ce jour.

Aucune base de données n'est diffusée ici. Les chiffres de l'essai sont des résultats agrégés calculés à partir de données © contributeurs OpenStreetMap (ODbL 1.0), de l'IGN et de Météo-France (Licence Ouverte Etalab 2.0). Ce travail est indépendant des exploitants des stations citées.
