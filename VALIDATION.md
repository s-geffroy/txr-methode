---
title: Protocole de validation
---

# Protocole de validation proposé

Les couleurs du plan ne sont pas la référence de TxR, qui cherche justement à les dépasser ; l'accord avec elles ne valide donc rien. Les corrections réduisent toutes la pente, si bien que l'accord augmente avec leur ampleur, et les couleurs elles-mêmes ont été données en grande partie d'après la pente (voir [l'essai à La Foux d'Allos](PILOTE.md)). Pour savoir si les notes sont justes, il faut mesurer la pente là où l'on skie : sur la neige damée.

## Deux questions distinctes

1. La pente est-elle bien estimée ? On compare la pente prédite à la pente mesurée sur neige damée.
2. La note rend-elle compte de la difficulté ressentie ? On compare T au jugement de skieurs experts.

La première question se règle par des mesures, la seconde par un jury. On les analyse séparément.

## Ce qu'on mesure

Avant toute mesure, il faut fixer quelle pente sert de référence : la ligne de pente de la piste, ou la trajectoire d'un skieur. θ dépend sans doute du niveau ; si la trajectoire est retenue, on la décrit pour un niveau donné.

T est un maximum sur toute la piste. Mesurer seulement le passage prédit comme le plus raide ne permet pas de voir que le modèle s'est trompé d'endroit. Le mieux est donc de relever des profils complets de la surface damée : par les systèmes de mesure de hauteur de neige embarqués sur les dameuses (GNSS), ou par des levés de drone (photogrammétrie ou LiDAR). Ces levés donnent en même temps la pente, l'épaisseur réelle de neige et la largeur damée. Un levé GNSS à pied le long de lignes choisies vient en complément. Un inclinomètre ne mesure la pente que sur un mètre environ, et ne convient pas seul.

On estime aussi θ sur des traces GPS de skieurs de plusieurs niveaux, plutôt que de le supposer.

Sur une piste non damée, les mêmes levés de surface montrent ce que la neige naturelle laisse du relief, et la taille des bosses. C'est la seule façon de savoir si la note calculée sans dameuse est juste, et s'il faut un jour une règle pour les bosses.

## Échantillon

- Plusieurs stations, et pas seulement la station pilote : 8 à 12 au total, de pays, d'altitudes et d'enneigements différents, pour pouvoir estimer l'écart entre stations.
- Dans chaque station, des pistes choisies par couleur et par note prédite, en ajoutant des vertes et des noires, rares dans une station donnée.
- Des mesures répétées dans la saison, pour plusieurs niveaux d'enneigement : c'est aussi ce qui permet de vérifier l'abaque d'enneigement.

## Analyse

- Pour la pente, on compare pente prédite et pente mesurée par la méthode de Bland et Altman adaptée aux mesures répétées : biais moyen et limites d'accord. Objectifs proposés : biais de moins de 2 points de pente (en %), limites d'accord à moins de 5 points. C'est la dispersion, plus que le biais, qui fait changer de classe.
- Pour la note, on croise T prédit et T mesuré dans un tableau complet, puis on estime l'accord avec un kappa pondéré et un modèle ordinal (logit cumulatif) avec un effet aléatoire par piste et par station. Pour une station, avec une centaine de passages répartis sur une quarantaine de pistes, l'intervalle du kappa aura une demi-largeur d'environ 0,13 à 0,15.
- Le jury réunit au moins cinq moniteurs extérieurs aux stations étudiées, qui notent sur une échelle décrite à l'avance, sur place ou sur vidéo. Accord entre eux mesuré par l'α de Krippendorff ordinal.
- Pour l'abaque, on tient un journal des notes du jour prédites et de ce qui a été observé sur place.

## Enregistrer avant de mesurer

Avant la campagne, tout est figé et déposé publiquement (OSF) : version de la méthode et paramètres, pente de référence (la ligne de pente), critère principal unique, critères secondaires, nombre de pistes et sa règle de calcul, règles d'exclusion, aveugle du jury, et ce qu'on fera si le critère n'est pas atteint. Le projet de ce dépôt est rédigé : [Préenregistrement](PREENREGISTREMENT.md).

Les stations qui ont servi à régler la méthode ne servent pas à la valider : la confirmation se fait sur des stations nouvelles.
