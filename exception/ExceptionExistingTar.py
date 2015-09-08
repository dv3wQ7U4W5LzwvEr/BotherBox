__author__ = 'root'

from exception.ExceptionExistingFile import ExceptionExistingFile

class ExceptionExistingTar(Exception):

    def __init__(self, file_name):
        self.value = ExceptionExistingFile(file_name)

    def __str__(self):
        return repr(self.value)
