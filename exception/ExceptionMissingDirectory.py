__author__ = 'root'


class ExceptionMissingDirectory(Exception):
    def __init__(self, directory_name):
        self.value = "Le répertoire '" + directory_name + "' n'a pas été trouvé."

    def __str__(self):
        return repr(self.value)
