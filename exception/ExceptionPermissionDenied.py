__author__ = 'root'


class ExceptionPermissionDenied(Exception):
    def __init__(self, directory_path):
        self.value = "Impossible d'écrire le fichier d'analyse dans le répertoire : " + directory_path + \
                     ". Si vous souhaitez vraiment analyser ce dossier, il faut lancer le programme en mode administrateur."

    def __str__(self):
        return repr(self.value)
