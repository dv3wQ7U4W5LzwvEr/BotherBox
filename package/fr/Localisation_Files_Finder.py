__author__ = 'root'

from enum import Enum


class Localisation_Files_Finder(Enum):

    PANEL_NAME = "FILES FINDER"
    PANEL_ANALYSE_CONTENT = "Analyser le répertoire"
    PANEL_ANALYSE_BUTTON = "Analyser"

    MESSAGE_EMPTY_NAME = "Il est nécessaire de saisir un nom du répertoire valide"
    MESSAGE_SUCCESS = "Félicitation, le répertoire a bien été analysé."

    MESSAGE_TYPE_INFORMATION = "Information"
    MESSAGE_TYPE_WARNING = "Attention"
    MESSAGE_TYPE_ERROR = "Erreur"

    LOG_ERROR = "Fucking error"