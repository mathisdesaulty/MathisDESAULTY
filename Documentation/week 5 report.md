# Week 5 report

8 hours this week.

## What I've learned

Cette semaine j'ai appris comment on été crée les distances D22 et D23 et à quoi elles servent. J'ai alors lu cette [article](https://www.researchgate.net/publication/290011464_Modifications_of_hausdorff_distance_for_object_matching), dans lequel l'on nous explique qu'il existe 6 distances et 4 fonctions composé de ces distances qui additionné entre elles peuvent nous aider à avoir des distances très précise. Les distances D22 et D23 utilise la fonction f3 et f4 sur la distance d6 qui est simplement la moyenne des minimums de distances de chaque point de l'image A dans l'image B.

## What I did this week

### Research for other distances

J'ai commencé la semaine par faire des petites recherches sur les distances que je pouvais utiliser. Dans le dernier weekly report j'ai parlé du fait que je ne savais pas comment améliorer les performances de mon algorithme, l'un des seuls moyens que j'avais trouvé était de changer mes méthodes de distances. Des méthodes plus adaptés, pourrait alors baissé le temps d'éxecution de mon algorithmes mais aussi améliorer les performances.
J'ai alors trouvé de nombreuses distances que je ne vais pas détailler ici, mais les plus interessantes m'ont l'air d'être D22 et D23, proposé par le professeur plus tôt.

### Upgrades

#### Numpy to list

Après avoir discuté avec le professeur, je me suis rendu compte que mon code était lent pour plusieurs choses. L'une des plus importantes était l'utilisation d'arraylist Numpy, alors que je pouvais simplement utiliser des Lists de Lists simple. J'ai du alors faire les changement dans la plupart de mes codes. Ce travail m'a pris un peu de temps car toutes mes données étaient sous la forme d'Arraylist Numpy et je devais alors changer plusieurs choses, comme par exemple: [Binarize the image](https://github.com/mathisdesaulty/MathisDESAULTY/blob/a31945060205931cf925a90a1cedf2749448470a/Object/image_user.py#L39-L45) qui était alors fais très simplement avec Numpy en une ligne.

#### Neighbors functions and performances acceleration

La deuxième observation était le fait que les images sont faites de 28 par 28 pixels. Chercher dans tout les pixels quand l'on veut chercher le plus proches, la plupart du temps, c'est cela qui rallonge le code. Depuis 2 semaines nous regardons d'abord les voisins avant de faire le tour de tout les points de l'autre images. Par voisins nous parlons seulement du premier cercle autour du point. Mais imaginons qu'on puisse changer ça pour regarder 4 cercles autours du point, on a alors beaucoup plus de points à check mais on est quasiment sur d'en trouver un dedans. J'ai alors modifié [neighbors_positive](https://github.com/mathisdesaulty/MathisDESAULTY/blob/a31945060205931cf925a90a1cedf2749448470a/Object/math_tool.py#L32-L57) pour que l'on puisse mettre en paramètre le nombre de cercle que l'on veut check autours de notre point, cette fonction renvoie maintenant un tuple, composé d'un booléen pour savoir si l'on a trouvé et d'un tuple des coordonnées du voisins le plus proches.

### Distance D22/23

Maintenant que j'ai un algorithme qui marche, je veux alors me pencher sur quel est la meilleur distances que je pourrais utiliser. J'ai alors mis en place cette semaine les distance D22 et D23, mais aussi la distance D6 (obligatoire pour faire ces deux distances). Vous pouvez trouver ces distances dans cette [article](https://www.researchgate.net/publication/290011464_Modifications_of_hausdorff_distance_for_object_matching). Vous pouvez revenir [there](https://github.com/mathisdesaulty/MathisDESAULTY/blob/a31945060205931cf925a90a1cedf2749448470a/Documentation/week%205%20report.md#L7) ou j'explique rapidement ce que sont ces distances sans rentrer dans les détails.

### Peer Review 
L'un des travaux de cette semaines a aussi été de faire une peer review d'une personnes. Le travail se concentré surtout sur la lecture du code et sur ce qui était bien mais aussi ce qui était a améliorer dans le code. 

## Issues

Cette semaine à surtout permis de régler des problèmes, pour le moment je n'en ai donc pas d'autre.

## What's next ?    

La prochaine étape est de tester les distance D22 et D23 en les adaptans dans la class K-NN et de faire pour les dernières semaines une interface utilisateur.