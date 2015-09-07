__author__ = 'root'


class ExceptionMissingFile(Exception):

    def __init__(self, file_name):
        self.value = "Le fichier '" + file_name + "' n'a pas été trouvé."

    def __str__(self):
        return repr(self.value)
