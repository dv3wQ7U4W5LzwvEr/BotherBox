__author__ = 'root'

from enum import Enum

class LocalisationFr(Enum):

    WINDOW_PROGRAM_NAME = "The Crazy Archiver"

    TEXT_BROWSE = "Parcourir"

    PANEL_ARCHIVE = "Archivage"
    PANEL_ARCHIVE_FILE_NAME = "Nom de l'archive "
    PANEL_ARCHIVE_LOOP = "Nombre de boucle :"
    PANEL_ARCHIVE_BUTTON = "Archiver"

    PANEL_UNARCHIVE_BUTTON = "Désarchiver"
    PANEL_UNARCHIVE = "Désarchivage"

    PANEL_ABOUT = "A propos"
    PANEL_ABOUT_CONTENT = "Ce logiciel a été créé par Florian VAUTARD. Il est possible de l'utiliser mais en ancun cas de" \
                  " le modifier ou de le vendre sans son autorisation."

    MESSAGE_EMPTY_NAME = "Il est nécessaire de saisir le nom du fichier"
    MESSAGE_EMPTY_NAME_FILE_OR_LOOP = MESSAGE_EMPTY_NAME + " et un nombre de tour positif."
    MESSAGE_NB_LOOP_POSITIF = "Le nombre de tour de boucle doit être positif"
    MESSAGE_INFORMATION = "Information"
    MESSAGE_WARNING = "Attention"
    MESSAGE_ERROR = "Erreur"