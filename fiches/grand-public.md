# Comment TxR note une piste de ski
> La Foux d'Allos · TxR v{{version}} · classement provisoire, à vérifier sur le terrain · ne remplace pas le balisage

## Deux notes plutôt qu'une couleur
La couleur d'une piste mélange deux choses. TxR les sépare en **deux notes indépendantes** :
- **T, la technique** (de T0 à T6) : à quel point le passage le plus raide est difficile ;
- **R, la résistance** (de R0 à R5) : combien la descente est longue et fatigante, d'après le dénivelé.

Une piste courte mais raide peut être **T5·R1** ; une longue piste facile, **T1·R4**. Les deux notes ne se compensent pas : un long passage facile n'efface pas un mur. Repère : une **verte** correspond à T0–T1, une **bleue** à T1–T2, une **rouge** à T3–T4, une **noire** à T4–T6.

## Comment on mesure la pente
[[schemas]]
- **Le relief vient d'un laser aéroporté** (IGN LiDAR HD : un point tous les 50 cm), mesuré sans neige.
- **On suit le tracé de chaque piste** et l'on mesure la pente sur chaque passage de **30 m**, la longueur d'un passage qu'on ne peut pas éviter. La note T vient du passage le plus raide (schéma 1 : Δz est la différence d'altitude).
- **Sur la neige, la piste est plus douce que le sol nu**, pour trois raisons, qui sont des **hypothèses** encore à vérifier : la piste est large (largeur typique {{largeur}} m), on peut choisir son passage ; on suppose qu'on descend **en zigzag**, à environ 30° de l'axe (schéma 2) ; la neige **comble les creux et les bosses** (schéma 3).

## Et la neige du jour ?
La station relève chaque jour la hauteur de neige **en bas (1 800 m) et en haut (2 600 m)**. TxR en déduit la neige sur chaque piste, selon son altitude et son orientation, puis recalcule la note. La neige change surtout les **murs courts** (sur 10 m) ; sur 30 m, elle modifie peu la note.

## À savoir
- La note T est une **limite basse** : « T3 » veut dire « au moins T3 ». Les seuils viennent d'une proposition de travail inspirée des repères des pistes damées ; ils **n'ont pas encore été vérifiés sur le terrain**.
- Comparé aux couleurs officielles, **{{p_traj}} pistes sur {{p_n}}** tombent dans la classe attendue (on en attendrait {{hasard}} au hasard) ; pour les autres, TxR estime provisoirement une pente plus forte que leur couleur. Ce n'est **pas une validation** : ce chiffre dépend des hypothèses ci-dessus. Le résultat plus solide : l'ordre des notes suit celui des couleurs.
- TxR ne tient **pas compte** de la glace, de la visibilité ni de l'affluence.

## Sources
{{sources}}
