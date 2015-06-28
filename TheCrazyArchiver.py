__author__ = 'root'

import tarfile
import os
import shutil
import sys
from exception.ExceptionFileMissing import ExceptionFileMissing
from exception.ExceptionNbLoop import ExceptionNbLoop


class TheCrazyArchiver:

    @staticmethod
    def archive(file_name, nb_loop):
        # testing input
        file_name = str(file_name)
        nb_loop = int(nb_loop)
        if nb_loop <= 0:
            raise ExceptionNbLoop()

        path = os.path.abspath(os.path.dirname(sys.argv[0])) + "/"
        if os.path.exists(path + file_name):
            count = 0
            while count < nb_loop:
                directory_name = file_name
                i = 1
                while os.path.exists(directory_name):
                    directory_name = file_name + "_" + str(i)
                    i += 1
                os.makedirs(directory_name)
                os.rename(path + file_name, path + directory_name + "/" + file_name)
                tar = tarfile.TarFile(file_name, 'w')
                tar.add(directory_name, file_name)
                tar.close()
                shutil.rmtree(path + directory_name)
                count += 1
        else:
            raise ExceptionFileMissing(file_name)

    @staticmethod
    def unarchive_tar_file(file_name):
        path_file = os.path.abspath(os.path.dirname(sys.argv[0])) + "/"
        file = tarfile.open(path_file + file_name)
        path_directory = path_file + "extract/"
        # creation du répertoire d'accueil du fichier extrait
        exctract_file_path = path_directory + file_name
        while file.extractfile(exctract_file_path):
            # extraction du fichier
            file.close()

            # ouverture de l'archive extraite
            file = tarfile.open(exctract_file_path)
            # creation du repertoire d'accueil du futur fichier
            path_directory += "extract/s"
            # ouverture de l'archive extraite
            exctract_file_path = path_directory + file_name
