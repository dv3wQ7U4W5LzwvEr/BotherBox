__author__ = 'root'


class ExceptionNbLoop(Exception):

    def __init__(self):
        self.value = "Le nombre d'archivage récursif doit être positif"

    def __str__(self):
        return repr(self.value)
