__author__ = 'root'

from enum import Enum

class Localisation(Enum):

    WINDOW_PROGRAM_NAME = "BotherBox"

    TEXT_BROWSE = "Parcourir"

    MESSAGE_INFORMATION = "Information"
    MESSAGE_WARNING = "Attention"
    MESSAGE_ERROR = "Erreur"

    MESSAGE_EMPTY_INPUT_FILE= "Il est nécessaire de saisir le nom du fichier"

    MESSAGE_EMPTY_INPUT_DIRECTORY = "Il est nécessaire de saisir un nom du répertoire valide"
