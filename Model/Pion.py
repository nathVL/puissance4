# Model/Pion.py

from Model.Constantes import *

#
# Ce fichier implémente les données/fonctions concernant le pion
# dans le jeu du Puissance 4
#
# Un pion est caractérisé par :
# - sa couleur (const.ROUGE ou const.JAUNE)
# - un identifiant de type int (pour l'interface graphique)
#
# L'identifiant sera initialisé par défaut à None
#

def type_pion(pion: dict) -> bool:
    """
    Détermine si le paramètre peut être ou non un Pion

    :param pion: Paramètre dont on veut savoir si c'est un Pion ou non
    :return: True si le paramètre correspond à un Pion, False sinon.
    """
    return type(pion) == dict and len(pion) == 2 and const.COULEUR in pion.keys() \
        and const.ID in pion.keys() \
        and pion[const.COULEUR] in const.COULEURS \
        and (pion[const.ID] is None or type(pion[const.ID]) == int)


def construirePion(couleur: int) -> dict:
    """
    Créer un pion

    :param couleur: Paramètre dont on veut que le pion ait cette couleur
    :return: le dictionnaire du du pion
    """
    if type(couleur) != int :
        raise TypeError("construirePion : Le paramètre n’est pas de type entier")
    if couleur != const.ROUGE and couleur != const.JAUNE :
        raise ValueError(f" construirePion : la couleur {couleur} n’est pas correcte")

    return {const.COULEUR : couleur, const.ID : None}


def getCouleurPion(pion: dict) -> int:
    """
    Donne la couleur du pion

    :param pion: Paramètre dont on veut connaitre la couleur du pion
    :return: la couleur du pion
    """
    if type_pion(pion) == False:
        raise TypeError("getCouleurPion : Le paramètre n’est pas un pion")
    return pion[const.COULEUR]

def setCouleurPion(pion: dict, couleur:int) -> None:
    """
    Change la couleur du pion

    :param pion: Paramètre qui donne quelle pion vas etre modifié
    :param couleur:  Paramètre qui donne la nouvelle couleur du pion
    :return: None
    """
    if type_pion(pion) == False:
        raise TypeError("setCouleurPion : Le premier paramètre n’est pas un pion")
    if type(couleur)!=int :
        raise TypeError("setCouleurPion : Le second paramètre n’est pas un entier.")
    if couleur!=const.ROUGE and couleur!=const.JAUNE :
        raise ValueError(f"setCouleurPion : Le second paramètre {couleur} n’est pas une couleur ")

    pion[const.COULEUR]=couleur

    return None

def getIdPion(pion: dict) -> int:
    """
    Connaitre l'id du pion

    :param pion:  Paramètre qui donne le pion dont on veut l'id
    :return: l'id du pion
    """
    if type_pion(pion) == False:
        raise TypeError("getIdPion : Le paramètre n’est pas un pion")
    return pion[const.ID]

def setIdPion(pion: dict, id: int) -> None:
    """
    Change l'id du pion

    :param pion: Paramètre qui donne le pion dont veut changer l'id
    :param id: Paramètre qui donne le nouvel id du pion
    :return: None
    """
    if type_pion(pion) == False:
        raise TypeError("setIdPion : Le premier paramètre n’est pas un pion")
    if type(id)!=int :
        raise TypeError("setIdPion : Le second paramètre n’est pas un entier.")
    pion[const.ID]=id
    return None