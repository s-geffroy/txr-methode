---
title: Préenregistrement de la validation
description: "Préenregistrement de la campagne de validation de TxR : critère principal, échantillon, règles d'analyse fixés avant toute mesure."
---

# Préenregistrement de la validation (projet)

Ce document fixe la campagne de validation **avant toute mesure**. Il complète le [protocole](VALIDATION.md) et doit être déposé tel quel, avec sa date, sur un registre public (OSF), puis cité par son identifiant. Une fois déposé, il ne change plus : un écart sera signalé comme tel dans le compte rendu.

État : projet, non déposé. Les valeurs marquées « hypothèse de travail » seront remplacées par celles de l'étude préliminaire (étape 1), suivant la règle donnée plus bas, avant le dépôt.

## 1. Ce qui est figé

- **Méthode** : TxR version 0.7.0, archivée sur Zenodo (DOI de version à reporter ici au dépôt). Le programme de calcul est celui de la même version, et chaque calcul garde l'empreinte de ses sources.
- **Paramètres** : L0 = 5 m, k = 5 (lissage L = L0 + k h ; piste non damée : L = k h, règle H13) ; largeur par défaut = médiane mesurée dans la station ; θ = 30° pour la trajectoire, qui n'est qu'une analyse secondaire ; règle « pas de zigzag sous 10 m de large ».
- **Seuils de T** (pente maximale sur 30 m) : T1 ≥ 10 %, T2 ≥ 20 %, T3 ≥ 25 %, T4 ≥ 35 %, T5 ≥ 45 %, T6 ≥ 60 % ; au moins T4 si P95₃₀ ≥ 40 % ; murs courts sur 10 m : 40, 50, 60, 75 % donnent au moins T3, T4, T5, T6. **Seuils de R** (dénivelé) : 80, 200, 400, 700, 1 100 m.
- **Convention de référence** : la **ligne de pente**, celle de la note affichée. La trajectoire est secondaire.
- **Neige** : la note prédite pour une mesure est celle de la cotation du jour, calculée à partir du relevé de la station le jour de la mesure.

## 2. Questions

- **Question principale (Q1)** : la pente maximale sur 30 m prédite pour une piste damée, en ligne de pente, est-elle celle qu'on mesure sur la neige damée ?
- **Questions secondaires** : la note T prédite est-elle celle que donne le profil mesuré (Q2) ? Le passage le plus raide est-il au bon endroit (Q3) ? La pente sur 10 m est-elle bien prédite (Q4) ? La note du jour suit-elle l'enneigement (Q5) ? La trajectoire, avec un θ mesuré sur des traces GPS, prédit-elle mieux que la ligne de pente (Q6) ? Les notes rendent-elles compte de la difficulté jugée par des moniteurs (Q7) ?

Les couleurs des pistes ne sont pas une référence et n'entrent dans aucun critère.

## 3. Stations et pistes

- **Stations** : 8 à 12 stations **nouvelles**. La Foux d'Allos, Pra-Loup, le Grand Tourmalet et Val d'Isère–Tignes, qui ont servi à mettre la méthode au point, sont exclues. On cherche des pays, des massifs, des altitudes et des enneigements différents.
- **Pistes** : dans chaque station, un tirage stratifié par couleur et par T prédit, qui surreprésente les vertes et les noires, rares dans une station. Le plan de tirage et ses probabilités sont publiés avec les données ; les résultats sont donnés sans pondération, puis pondérés par l'inverse de la probabilité de tirage.
- **Unité d'analyse** : la **piste**. La pente maximale sur 30 m est une valeur par piste ; les passages de 30 m servent à Q3 et aux analyses descriptives, avec un effet de grappe par piste et par station.

## 4. Mesures

- Profil complet de la surface damée, le long de la ligne de pente de la piste : systèmes de mesure de hauteur de neige des dameuses (GNSS), ou levé de drone (photogrammétrie ou LiDAR). Un levé GNSS à pied complète, sur des lignes choisies avant la mesure.
- Une piste est **retenue** si le profil mesuré couvre au moins 80 % de sa longueur, sans lacune de plus de 30 m ; sinon elle est exclue, et le compte rendu donne le nombre et les motifs des exclusions. Aucune valeur manquante n'est imputée.
- La pente mesurée se calcule avec les mêmes fenêtres que la prédiction (30 m et 10 m, au pas de 1 m) ; la note T mesurée applique les mêmes seuils au profil mesuré.
- Traces GPS de skieurs de trois niveaux (débutant, intermédiaire, confirmé) pour estimer θ (Q6).

## 5. Critères

**Critère principal (Q1)**, sur la différence d = pente prédite − pente mesurée, par piste, en points de pente (%), par la méthode de Bland et Altman avec effet aléatoire de station :

- l'intervalle de confiance à 95 % du biais moyen est entièrement compris entre −2 et +2 points ;
- **et** les limites d'accord à 95 % sont comprises entre −5 et +5 points.

Le critère est atteint si les deux conditions le sont. C'est le seul critère qui décide.

**Critères secondaires** (descriptifs, sans correction de multiplicité, présentés comme tels) :

- Q2 : κ pondéré quadratique entre T prédit et T mesuré ; on rapporte sa valeur et son intervalle ; repère : borne basse au-dessus de 0,6. Modèle ordinal (logit cumulatif) avec effets aléatoires de piste et de station.
- Q3 : part des pistes dont le maximum mesuré est à moins de 30 m du maximum prédit ; repère : au moins 70 %.
- Q4 : même analyse que Q1 sur 10 m.
- Q5 : journal des notes du jour prédites et observées, sur au moins trois niveaux d'enneigement par station.
- Q6 : comparaison des erreurs de Q1 entre ligne de pente et trajectoire (θ estimé).
- Q7 : jury d'au moins cinq moniteurs extérieurs aux stations étudiées, qui notent **sans connaître** ni la note TxR ni la couleur (vidéos sans panneau ni balisage visible), sur une échelle décrite avant la campagne. Le jugement du jury n'est utilisé que si l'accord entre ses membres atteint α de Krippendorff ordinal ≥ 0,67.

## 6. Nombre de pistes

On vise **environ 100 pistes** au total. Le nombre définitif se calcule après l'étape 1, par la règle suivante, fixée dès maintenant :

n = ⌈(1,96 σ / 1)² × (1 + (m − 1) ρ)⌉

où σ est l'écart type des différences d mesuré à l'étape 1, 1 point la demi-largeur visée pour l'intervalle du biais, m le nombre moyen de pistes par station et ρ la corrélation intra-station estimée. Hypothèse de travail : σ = 5 points, ρ = 0,05, m = 10, soit n ≈ 140. Avec 100 pistes et σ = 5, l'intervalle du biais a une demi-largeur d'environ 1 point et chaque limite d'accord est connue à environ ±1,7 point. Pour Q2, l'intervalle du κ aura une demi-largeur d'environ 0,1 : la borne basse ne dépasse 0,6 que si le κ observé dépasse environ 0,7.

## 7. Étapes

1. **Étude préliminaire** : 10 pistes dans une station nouvelle, pour estimer σ et ρ et éprouver la mesure. Ces pistes n'entrent pas dans l'analyse principale.
2. Calcul du nombre définitif (section 6), puis **dépôt** du présent document complété.
3. Campagne de mesure ; calcul des prédictions avec la version figée, **avant** de comparer aux mesures, par une personne qui n'a pas vu les mesures.
4. Analyse et compte rendu, que les critères soient atteints ou non.

## 8. Si les critères ne sont pas atteints

- Le résultat est publié tel quel, avec les données.
- Aucun paramètre n'est réajusté sur les stations de validation pour « faire passer » le critère. Une méthode corrigée devient une nouvelle version, qui demandera une nouvelle confirmation sur d'autres stations.
- Si le biais est hors bornes mais les limites d'accord bonnes, on publie la correction de biais comme une hypothèse à confirmer. Si les limites d'accord sont trop larges, la note T reste présentée comme une borne provisoire et l'on cherche d'où vient la dispersion (largeur, MNT, neige) avant toute nouvelle version.
