__author__ = 'root'


class ExceptionMissingTar(Exception):

    def __init__(self, file_name):
        self.value = "Le fichier '" + file_name + "' n'est pas une archive."

    def __str__(self):
        return repr(self.value)
