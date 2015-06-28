__author__ = 'root'


class ExceptionFileMissing(Exception):

    def __init__(self, file_name):
        super(ExceptionFileMissing, self).__init__("Le fichier " + file_name + " n'a pas été trouvé.")

    def __str__(self):
        return repr(self)
