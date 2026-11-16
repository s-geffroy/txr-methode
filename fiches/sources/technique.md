# TxR : fiche technique
> Méthode de recherche · seuils et corrections non calibrés · version 0.5.0, programme de calcul non publié

## Principe
Deux notes qui ne se compensent pas. **T** (T0 à T6) est la plus haute des classes données par trois règles sur la pente. **R** (R0 à R5) est la classe du dénivelé net de la piste. L'exposition E et les conditions C restent à part et ne sont pas calculées.

## Données
Tracés OpenStreetMap (`piste:type=downhill`), assemblés seulement par points partagés, orientés par les altitudes des extrémités et comparés au sens de saisie. MNT de sol nu : référence au pas de 5 m, puis MNT fin aux pas de 5, 2 et 1 m s'il couvre 99 % des points (en France : RGE ALTI et LiDAR HD de l'IGN). Neige : climatologie par altitude, orientation, pente et mois (en France : réanalyse S2M). Projection conforme, distances à plat.

## Mesure
[[image:schemas]]
Pente descendante sur des passages de 10, 30 et 100 m mesurés à plat et glissés le long du tracé, admis si W ≥ 3 × max(pas, maille). On garde Gmax, P50, P90 et P95. Stabilité entre pas : tolérance de 400 · u / W points, u = erreur verticale maximale du MNT (inconnue par défaut ; 0,10 m en test pour le LiDAR HD).

Correction vers la piste damée : parallèles tous les 2 m dans la largeur skiable (surfaces OpenStreetMap, sinon médiane de la station), prises en face de l'axe, la moins raide retenue pour chaque passage ; lissage par moyenne glissante sur L = L0 + k · h (L0 = 5 m, k = 5, h en m) ; zigzag symétrique à θ = 30°, avance W · cos θ le long de chaque ligne, pente = dénivelé / W. Sur un plan, la pente est multipliée par cos θ : cela revient à diviser les seuils par cos θ. Pas de zigzag sous 10 m de largeur. Virages en arcs (godille 4 m, courts 8 m, moyens 15 m, grands 25 m ; virage coupé R = R_ski · cos 45°) : pente moyenne = pente · sin φ / φ, φ limité par la largeur. Deux conventions : trajectoire (θ = 30°), pour les essais, et ligne de pente (θ = 0), la plus prudente, pour l'affichage. Avec les seuils actuels, la règle P95 ne change jamais la note (P95 ≥ 40 % implique Gmax ≥ 35 %).

## Règles
| Règle | T1 | T2 | T3 | T4 | T5 | T6 |
|---|---|---|---|---|---|---|
| Gmax sur 30 m | 10 % | 20 % | 25 % | 35 % | 45 % | 60 % |
| Gmax sur 10 m (mur court) | | | 40 % | 50 % | 60 % | 75 % |
| P95 sur 30 m | | | | 40 % | | |

R : 80, 200, 400, 700 et 1 100 m de dénivelé donnent R1 à R5. Statuts : non déterminé, borne basse provisoire, définitif (jamais atteint aujourd'hui). Pic à confirmer : règle déclenchée sur moins de 2 W.

## Neige du jour
$$h = \left[(1 - t)\,h_{\mathrm{bas}} + t\,h_{\mathrm{haut}}\right] f \qquad L = L_0 + k\,h \qquad g_{\mathrm{trajet}} = g\,\frac{\sin\varphi}{\varphi}$$
t position en altitude entre les deux relevés encadrants, bornée à [0, 1], f = rapport climatologique orientation / plat à la même altitude, borné à [0, 3]. Abaque manuel pour un mur court : voir la fiche exploitants.

## Essai pilote (exploratoire)
42 pistes d'une station des Alpes du Sud. Pistes conformes à leur couleur : 8 sur sol nu, 10 en ligne de pente, 19 en trajectoire (14,3 attendues au hasard ; accord corrigé 0,17), 32 avec θ = 45°. τ-b de rang couleur / T : 0,75 [0,66 ; 0,82] en trajectoire, contre 0,59 pour la pente moyenne seule. θ, L0, k et la largeur par défaut ont été fixés pendant l'analyse : ces chiffres ne valident rien.

## Limites
Seuils, θ, L0, k et u non calibrés. Neige de culture, damage réel, dévers, obstacles, glace non modélisés. Types de virages et rayons supposés. Validation prévue : profils de neige damée (GNSS des dameuses, drone), plusieurs stations, paramètres figés et déposés avant la mesure.

<small>Relief : IGN (Licence Ouverte Etalab 2.0). Tracés : © contributeurs OpenStreetMap (ODbL 1.0). Neige : Météo-France, S2M (Licence Ouverte Etalab 2.0). https://s-geffroy.github.io/txr-methode/</small>
