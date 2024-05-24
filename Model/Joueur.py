from Model.Constantes import *
from Model.Pion import *
from random import *
from Model.Plateau import *



#
# Ce fichier contient les fonctions gérant le joueur
#
# Un joueur sera un dictionnaire avec comme clé :
# - const.COULEUR : la couleur du joueur entre const.ROUGE et const.JAUNE
# - const.PLACER_PION : la fonction lui permettant de placer un pion, None par défaut,
#                       signifiant que le placement passe par l'interface graphique.
# - const.PLATEAU : référence sur le plateau de jeu, nécessaire pour l'IA, None par défaut
# - d'autres constantes nécessaires pour lui permettre de jouer à ajouter par la suite...
#

def type_joueur(joueur: dict) -> bool:
    """
    Détermine si le paramètre peut correspondre à un joueur.

    :param joueur: Paramètre à tester
    :return: True s'il peut correspondre à un joueur, False sinon.
    """
    if type(joueur) != dict:
        return False
    if const.COULEUR not in joueur or joueur[const.COULEUR] not in const.COULEURS:
        return False
    if const.PLACER_PION not in joueur or (joueur[const.PLACER_PION] is not None and not callable(joueur[const.PLACER_PION])):
        return False
    if const.PLATEAU not in joueur or (joueur[const.PLATEAU] is not None and not type_plateau(joueur[const.PLATEAU])):
        return False
    return True


def getCouleurJoueur(joueur: dict) -> int:
    '''
    Avoir la couleur du joueur

    :param joueur: dictionnaire representant le joueur
    :return: la couleur du joueur
    '''
    if type_joueur(joueur) == False:
        raise TypeError("getCouleurJoueur : Le paramètre ne correspond pas à un joueur")
    return joueur[const.COULEUR]

def getPlateauJoueur(joueur: dict) -> list:
    '''
    Avoir le plateau du joueur

    :param joueur: dictionnaire representant le joueur
    :return: le plateau du joueur
    '''
    if type_joueur(joueur) == False:
        raise TypeError("getPlateauJoueur : le paramètre ne correspond pas à un joueur")
    return joueur[const.PLATEAU]

def getPlacerPionJoueur(joueur: dict) -> list:
    '''
    Avoir la fonction du joueur

    :param joueur: dictionnaire representant le joueur
    :return: la fonction du joueur
    '''
    if type_joueur(joueur) == False:
        raise TypeError("getPlacerPionJoueur : le paramètre ne correspond pas à un joueur")
    return joueur[const.PLACER_PION]

def getPionJoueur(joueur: dict) -> dict:
    '''
    Creer un pion de la couleur du joueur

    :param joueur: dictionnaire representant le joueur
    :return: un pion sous forme de dictionnaire
    '''
    if type_joueur(joueur) == False:
        raise TypeError("getPionJoueur : le paramètre ne correspond pas à un joueur")
    return {const.COULEUR: joueur[const.COULEUR], const.ID: None}

def setPlateauJoueur(joueur: dict, plateau: list) -> None:
    '''
    Definir le plateau du joueur

    :param joueur: dictionnaire representant le joueur
    :param plateau: plateau de jeu
    :return: None
    '''
    if type_joueur(joueur) == False:
        raise TypeError("setPlateauJoueur : Le premier paramètre ne correspond pas à un joueur")
    if type_plateau(plateau) == False:
        raise TypeError("setPlateauJoueur : Le second paramètre ne correspond pas à un plateau")
    joueur[const.PLATEAU] = plateau
    return None

def setPlacerPionJoueur(joueur: dict, fonction: callable) -> None:
    '''
    Definir la fonction du joueur

    :param joueur: dictionnaire representant le joueur
    :param fonction: fonction
    :return: None
    '''
    if type_joueur(joueur) == False:
        raise TypeError("setPlacerPionJoueur : Le premier paramètre ne correspond pas à un joueur")
    if not callable(fonction):
        raise TypeError("setPlacerPionJoueur : le second paramètre n’est pas une fonction")

    joueur[const.PLACER_PION] = fonction
    return None

def _placerPionJoueur(joueur: dict) -> int:
    '''
    Choisir une colonne ou passer le pion

    :param joueur: dictionnaire representant le joueur
    :return: l'entier associé à la colonne
    '''
    if type_joueur(joueur) == False:
        raise TypeError("_placerPionJoueur : Le premier paramètre n’est pas un joueur")

    if getModeEtenduJoueur(joueur):
        n = randint(-const.NB_LINES, const.NB_COLUMNS + const.NB_LINES - 1)
        if n >= 0 and n < const.NB_COLUMNS - 1:
            while joueur[const.PLATEAU][0][n] is not None:
                n = randint(0, const.NB_COLUMNS - 1)
    else:
        n = randint(0, const.NB_COLUMNS - 1)
        while joueur[const.PLATEAU][0][n] is not None:
            n = randint(0, const.NB_COLUMNS - 1)
    return n

def initialiserIAJoueur(joueur: dict, boule: bool) -> None:
    '''
    Initialiser un joueur comme étant une IA

    :param joueur: dictionnaire representant le joueur
    :param boule: True si l'ia joue en première False sinon
    :return: None
    '''
    if type_joueur(joueur) == False:
        raise TypeError("initialiserIAJoueur : Le premier paramètre n’est pas un joueur")
    if type(boule) != bool:
        raise TypeError("initialiserIAJoueur : Le second paramètre n’est pas un booléen")
    setPlacerPionJoueur(joueur, _placerPionJoueur)
    return None


def getModeEtenduJoueur(joueur: dict) -> bool:
    """
    Savoir si le mode étendu est utilisé

    :param joueur: dictionnaire representant le joueur
    :return: True si le mode étendue si etendu est activé
    """
    if type_joueur(joueur) == False:
        raise TypeError("getModeEtenduJoueur : le paramètre ne correspond pas à un joueur")
    return const.MODE_ETENDU in joueur


def setModeEtenduJoueur(joueur: dict, boule: bool = True) -> None:
    """
    Mettre ou enlever le mode étendu

    :param joueur: dictionnaire representant le joueur
    :param boule: booléen initialisé a True qui décide si on enlève ou ajoute le mode étendu
    :return: None
    """
    if type_joueur(joueur) == False:
        raise TypeError("getModeEtenduJoueur : le paramètre ne correspond pas à un joueur")
    if type(boule) != bool:
        raise TypeError("setModeEtenduJoueur : le second paramètre ne correspond pas à un booléen")

    if getModeEtenduJoueur(joueur) is False and boule:
        joueur[const.MODE_ETENDU] = None
    elif getModeEtenduJoueur(joueur) is True:
        del joueur[const.MODE_ETENDU]
    return None