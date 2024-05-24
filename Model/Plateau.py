from Model.Constantes import *
from Model.Pion import *


#
# Le plateau représente la grille où sont placés les pions.
# Il constitue le coeur du jeu car c'est dans ce fichier
# où vont être programmées toutes les règles du jeu.
#
# Un plateau sera simplement une liste de liste.
# Ce sera en fait une liste de lignes.
# Les cases du plateau ne pourront contenir que None ou un pion
#
# Pour améliorer la "rapidité" du programme, il n'y aura aucun test sur les paramètres.
# (mais c'est peut-être déjà trop tard car les tests sont fait en amont, ce qui ralentit le programme...)
#

def type_plateau(plateau: list) -> bool:
    """
    Permet de vérifier que le paramètre correspond à un plateau.
    Renvoie True si c'est le cas, False sinon.

    :param plateau: Objet qu'on veut tester
    :return: True s'il correspond à un plateau, False sinon
    """
    if type(plateau) != list:
        return False
    if len(plateau) != const.NB_LINES:
        return False
    wrong = "Erreur !"
    if next((wrong for line in plateau if type(line) != list or len(line) != const.NB_COLUMNS), True) == wrong:
        return False
    if next((wrong for line in plateau for c in line if not (c is None) and not type_pion(c)), True) == wrong:
        return False
    return True


def construirePlateau() -> list:
    """
    Construit le plateau

    :return: Une liste de liste
    """
    lst = []
    for i in range(const.NB_LINES):
        temp = []
        lst.append(temp)
        for j in range(const.NB_COLUMNS):
            temp.append(None)
    return lst


def placerPionPlateau(plateau: list, pion: dict, num: int) -> int:
    '''
    Placer un pion dans le tableau

    :param plateau: plateau de jeu
    :param pion: le pion à placer
    :param num: le numéro de colonne du pion
    :return: le numéro de la ligne ou le pion doit être placé
    '''
    if type_plateau(plateau) == False:
        raise TypeError("placerPionPlateau : Le premier paramètre ne correspond pas à un plateau")
    if type_pion(pion) == False:
        raise TypeError("placerPionPlateau : Le second paramètre n’est pas un pion")
    if type(num) != int:
        raise TypeError("placerPionPlateau : Le troisième paramètre n’est pas un entier")
    if num < 0 or num > (const.NB_COLUMNS - 1):
        raise ValueError(f"placerPionPlateau : La valeur de la colonne {num} n’est pas correcte")
    res = -1
    i = const.NB_LINES - 1
    while res == -1 and i >= 0:
        if plateau[i][num] is None:
            plateau[i][num] = pion
            res = i
        i -= 1
    return res


def toStringPlateau(plateau: list) -> str:
    '''
    Creer un str representant le plateau

    :param plateau: plateau de jeu
    :return:
    '''
    strPlateau = ''
    for ligne in range(const.NB_LINES):
        temp = '|'
        for colonne in range(const.NB_COLUMNS):
            if plateau[ligne][colonne] == None:
                temp += ' |'
            elif plateau[ligne][colonne][const.COULEUR] == const.JAUNE:
                temp += '\x1B[43m \x1B[0m|'
            elif plateau[ligne][colonne][const.COULEUR] == const.ROUGE:
                temp += '\x1B[41m \x1B[0m|'
        temp += '\n'
        strPlateau += temp
    strPlateau += '-' * 15 + '\n 0 1 2 3 4 5 6'
    return strPlateau


def detecter4horizontalPlateau(plateau: list, couleur: int) -> list:
    '''
    Permet de vérifier s'il y a des suites horizontales de 4 pions.

    :param plateau: plateau de jeu
    :param couleur: la couleur dont on veut détecter les suites
    :return: la liste contenant tout les pions impliqué dans une suite
    '''
    if type_plateau(plateau) == False:
        raise TypeError("detecter4horizontalPlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) != int:
        raise TypeError("detecter4horizontalPlateau : le second paramètre n’est pas un entier")
    if couleur != const.ROUGE and couleur != const.JAUNE:
        raise ValueError(f"détecter4horizontalPlateau : La valeur de la couleur {couleur} n’est pas correcte")

    res = []
    for ligne in range(const.NB_LINES):
        temp = []
        for nPion in range(const.NB_COLUMNS):
            if plateau[ligne][nPion] is not None and plateau[ligne][nPion][const.COULEUR] == couleur:
                temp.append(plateau[ligne][nPion])
            else:
                if len(temp) >= 4:
                    res += temp[:4]
                temp = []
        if len(temp) >= 4:
            res += temp[:4]
    return res


def detecter4verticalPlateau(plateau: list, couleur: int) -> list:
    '''
    Permet de vérifier s'il y a des suites verticales de 4 pions.

    :param plateau: plateau de jeu
    :param couleur: la couleur dont on veut détecter les suites
    :return: la liste contenant tout les pions impliqué dans une suite
    '''
    if type_plateau(plateau) == False:
        raise TypeError("detecter4verticalPlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) != int:
        raise TypeError("detecter4verticalPlateau : Le second paramètre n’est pas un entier")
    if couleur != const.ROUGE and couleur != const.JAUNE:
        raise ValueError(f"detecter4verticalPlateau : La valeur de la couleur {couleur} n’est pas correcte")

    res = []
    for colonne in range(const.NB_COLUMNS):
        temp = []
        for ligne in range(const.NB_LINES):
            if plateau[ligne][colonne] is not None and plateau[ligne][colonne][const.COULEUR] == couleur:
                temp.append(plateau[ligne][colonne])
            else:
                if len(temp) >= 4:
                    res += temp[:4]
                temp = []
        if len(temp) >= 4:
            res += temp[:4]
    return res


def detecter4diagonaleDirectePlateau(plateau: list, couleur: int) -> list:
    """
    Permet de vérifier s'il y a des suites de 4 pions dans les diagonales directes.

    :param plateau: plateau de jeu
    :param couleur: la couleur dont on veut détecter les suites
    :return: la liste contenant tout les pions impliqué dans une suite de diagonales directes
    """
    if type_plateau(plateau) == False:
        raise TypeError("detecter4diagonaleDirectePlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) != int:
        raise TypeError("detecter4diagonaleDirectePlateau : Le second paramètre n’est pas un entier")
    if couleur != const.ROUGE and couleur != const.JAUNE:
        raise ValueError(f"detecter4diagonaleDirectePlateau : La valeur de la couleur {couleur} n’est pas correcte")

    diagonales = [[0, 2], [0, 0], [0, 1], [0, 3], [1, 0], [2, 0]]
    res = []

    for diago in diagonales:
        i = diago[0]
        j = diago[1]
        temp = []
        while i < const.NB_LINES and j <  const.NB_COLUMNS:
            if plateau[i][j] is not None and plateau[i][j][const.COULEUR] == couleur:
                temp.append(plateau[i][j])
            else:
                if len(temp) >= 4:
                    res += temp[:4]
                temp = []
            i += 1
            j += 1
        if len(temp) >= 4:
            res += temp[:4]

    return res


def detecter4diagonaleIndirectePlateau(plateau: list, couleur: int) -> list:
    '''
    Permet de vérifier s'il y a des suites de 4 pions dans les diagonales indirectes.

    :param plateau: plateau de jeu
    :param couleur: la couleur dont on veut détecter les suites
    :return: la liste contenant tout les pions impliqué dans une suite de diagonales indirectes
    '''
    if type_plateau(plateau) == False:
        raise TypeError("detecter4diagonaleIndirectePlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) != int:
        raise TypeError("detecter4diagonaleIndirectePlateau : Le second paramètre n’est pas un entier")
    if couleur != const.ROUGE and couleur != const.JAUNE:
        raise ValueError(f"detecter4diagonaleIndirectePlateau : La valeur de la couleur {couleur} n’est pas correcte")


    diagonales = [[0, 3], [0, 4], [0, 5], [0, 6], [1, 6], [2, 6]]
    res = []
    for diago in diagonales:
        i = diago[0]
        j = diago[1]
        temp = []
        while i < const.NB_LINES and j >= 0:
            if plateau[i][j] is not None and plateau[i][j][const.COULEUR] == couleur:
                temp.append(plateau[i][j])
            else:
                if len(temp) >= 4:
                    res += temp[:4]
                temp = []
            i += 1
            j -= 1
        if len(temp) >= 4:
            res += temp[:4]
    return res


def getPionsGagnantsPlateau(plateau: list) -> list:
    '''
    Permet de vérifier toute les séries de pions gagnants

    :param plateau: plateau de jeu
    :return: liste contenant tous les pions gagnants
    '''
    if type_plateau(plateau) == False:
        raise TypeError("getPionsGagnantsPlateau : Le paramètre n’est pas un plateau ")
    fonctions = [detecter4horizontalPlateau, detecter4verticalPlateau, detecter4diagonaleDirectePlateau,
                 detecter4diagonaleIndirectePlateau]
    res = []
    for fonction in fonctions:
        for couleur in const.COULEURS:
            if fonction(plateau, couleur) != []:
                resultat = fonction(plateau, couleur)
                for pion in resultat:
                    res.append(pion)
    return res


def isRempliPlateau(plateau: list) -> bool:
    """
    Savoir si le plateau est plein

    :param plateau: plateau de jeu
    :return: True si le plateau est plein, False sinon
    """
    if type_plateau(plateau) == False:
        raise TypeError("isRempliPlateau : Le paramètre n’est pas un plateau")
    plein = True
    for i in plateau:
        for j in i:
            if j is None:
                plein = False
    return plein


def construireJoueur(couleur: int) -> dict:
    '''
    Permet de construire le dictionnaire correspondant au joueur

    :param couleur: la couleur du joueur
    :return: le dictionnaire correspondant au joueur
    '''
    if type(couleur) != int:
        raise TypeError("construireJoueur : Le paramètre n’est pas un entier")
    if couleur != const.ROUGE and couleur != const.JAUNE:
        raise ValueError(f"construireJoueur : L’entier donné {couleur} n’est pas une couleur")
    return {const.COULEUR: couleur, const.PLATEAU: None, const.PLACER_PION: None}


def placerPionLignePlateau(plateau: list, pion: dict, num_ligne: int, left: bool) -> tuple:
    '''
    Placer les pions pour le mode étendu

    :param plateau: plateau de jeu
    :param pion: le pion à placer
    :param num_ligne: numéro de la ligne ou placer le pion
    :param left: True si le pion est à gauche False sinon
    :return: un tuple avec la liste des pions poussés et un numéro de ligne
    '''
    if type_plateau(plateau) == False:
        raise TypeError("placerPionLignePlateau : Le premier paramètre n’est pas un plateau")
    if type_pion(pion) == False:
        raise TypeError("placerPionLignePlateau : Le second paramètre n’est pas un pion")
    if type(num_ligne) != int:
        raise TypeError("placerPionLignePlateau : le troisième paramètre n’est pas un entier")
    if num_ligne < 0 and num_ligne > const.NB_LINES - 1:
        raise ValueError(
            "placerPionLignePlateau : Le troisième paramètre (valeur_du_paramètre) ne désigne pas une ligne")
    if type(left) != bool:
        raise TypeError("placerPionLignePlateau : le quatrième paramètre n’est pas un booléen")

    res = [pion]
    ligne = None
    if left:
        i = 0
        while i < const.NB_COLUMNS and plateau[num_ligne][i] is not None:
            res.append(plateau[num_ligne][i])
            plateau[num_ligne][i] = res[i]
            i += 1
        if i == const.NB_COLUMNS:
            ligne = const.NB_LINES
        else:
            ligne = placerPionPlateau(plateau, res[i], i)
    else:
        i = const.NB_COLUMNS - 1
        while i > -1 and plateau[num_ligne][i] is not None:
            res.append(plateau[num_ligne][i])
            plateau[num_ligne][i] = res[const.NB_COLUMNS - i - 1]
            i -= 1
        if i == -1:
            ligne = const.NB_LINES
        else:
            ligne = placerPionPlateau(plateau, res[const.NB_COLUMNS - i - 1], i)
    return (res, ligne)


def encoderPlateau(plateau: list) -> str:
    '''
    Encoder un plateau

    :param plateau: plateau de jeu
    :return: un str du plateau encoder
    '''
    if type_plateau(plateau) == False:
        raise TypeError("encoderPlateau : le paramètre ne correspond pas à un plateau.")
    coder = ''
    for ligne in plateau:
        for pion in ligne:
            if pion == None:
                coder += '_'
            elif pion[const.COULEUR] == const.ROUGE:
                coder += 'R'
            elif pion[const.COULEUR] == const.JAUNE:
                coder += 'J'
    return coder


def isPatPlateau(plateau: list, histogramme: dict) -> bool:
    """
    Savoir si la partie est nulle

    :param plateau:  plateau de jeu
    :param histogramme: histogramme des plateaux de jeux
    :return: True si la partie est nulle False sinon
    """
    if type_plateau(plateau) == False:
        raise TypeError("isPatPlateau : Le premier paramètre n’est pas un plateau")
    if type(histogramme) != dict:
        raise TypeError("isPatPlateau : Le second paramètre n’est pas un dictionnaire")
    res = False
    coder = encoderPlateau(plateau)
    if coder in histogramme:
        histogramme[coder] += 1
        if histogramme[coder] >= 5:
            res = True
    else:
        histogramme[coder] = 1
    return res
