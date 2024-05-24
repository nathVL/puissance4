from Model.Constantes import *
from Model.Plateau import *
from Model.Pion import *
from random import randint, choice
from Model.Plateau import *


# test de la fonction toStringPlateau
p = construirePlateau()
p = [[None, None, {'Couleur': 1, 'Identifiant': 1}, None, None, None, None], [None, None, {'Couleur': 0, 'Identifiant': None}, {'Couleur': 1, 'Identifiant': 2}, None, None, None], [None, None, {'Couleur': 1, 'Identifiant': None}, {'Couleur': 0, 'Identifiant': None}, {'Couleur': 1, 'Identifiant': None}, None, {'Couleur': 0, 'Identifiant': None}], [None, None, {'Couleur': 1, 'Identifiant': None}, {'Couleur': 1, 'Identifiant': None}, {'Couleur': 1, 'Identifiant': None}, {'Couleur': 1, 'Identifiant': None}, {'Couleur': 0, 'Identifiant': None}], [None, {'Couleur': 1, 'Identifiant': None}, {'Couleur': 1, 'Identifiant': None}, {'Couleur': 1, 'Identifiant': None}, {'Couleur': 1, 'Identifiant': None}, {'Couleur': 1, 'Identifiant': None}, {'Couleur': 1, 'Identifiant': None}], [{'Couleur': 0, 'Identifiant': None}, {'Couleur': 1, 'Identifiant': None}, {'Couleur': 1, 'Identifiant': None}, {'Couleur': 0, 'Identifiant': None}, {'Couleur': 1, 'Identifiant': None}, {'Couleur': 1, 'Identifiant': None}, {'Couleur': 1, 'Identifiant': None}]]


#for _ in range(10):
#    placerPionPlateau(p, construirePion(choice(const.COULEURS)),randint(0, const.NB_COLUMNS - 1))

print(p)
print(toStringPlateau(p))

print(detecter4diagonaleDirectePlateau(p, const.ROUGE))
print(detecter4diagonaleIndirectePlateau(p, const.ROUGE))