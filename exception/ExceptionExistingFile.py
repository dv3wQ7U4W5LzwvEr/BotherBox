__author__ = 'root'


class ExceptionExistingFile(Exception):

    def __init__(self, file_name):
        self.value = "Le fichier '" + file_name + "' existe déjà."

    def __str__(self):
        return repr(self.value)
