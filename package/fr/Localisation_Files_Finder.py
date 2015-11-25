__author__ = 'root'

from enum import Enum


class Localisation_Files_Finder(Enum):

    PANEL_NAME = "FILES FINDER"
    PANEL_ANALYSE_CONTENT = "Analyser le répertoire"
    PANEL_ANALYSE_BUTTON = "Analyser"

    MESSAGE_SUCCESS = "Félicitation, le répertoire a bien été analysé."

    LOG_ERROR = "Fucking error"