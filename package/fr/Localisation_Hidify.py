__author__ = 'root'

from enum import Enum

class Localisation_Hidify(Enum):

    PANEL_NAME = "HIDIFY"

    PANEL_ARCHIVE = "Archivage"
    PANEL_ARCHIVE_FILE_NAME = "Nom de l'archive "
    PANEL_ARCHIVE_LOOP = "Nombre de boucle (limité à 19):"
    PANEL_ARCHIVE_BUTTON = "Archiver"

    PANEL_UNARCHIVE_BUTTON = "Désarchiver"
    PANEL_UNARCHIVE = "Désarchivage"

    MESSAGE_EMPTY_NAME = "Il est nécessaire de saisir le nom du fichier"
    MESSAGE_EMPTY_NAME_FILE_OR_LOOP = MESSAGE_EMPTY_NAME + " et un nombre de tour positif."
    MESSAGE_NB_LOOP_POSITIF = "Le nombre de tour de boucle doit être positif"