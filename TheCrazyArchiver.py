__author__ = 'root'

import tarfile
import os
import shutil
import ntpath
from exception.ExceptionFileMissing import ExceptionFileMissing
from exception.ExceptionNbLoop import ExceptionNbLoop


class TheCrazyArchiver:

    @staticmethod
    def archive(file, nb_loop):
        # testing input
        file = str(file)
        nb_loop = int(nb_loop)
        if nb_loop <= 0:
            raise ExceptionNbLoop()

        if os.path.exists(file):
            count = 0
            directory_name = os.path.dirname(os.path.realpath(file)) + "/directory/"
            file_tar = ntpath.basename(file) + ".tar"
            while count < nb_loop:
                i = 1
                while os.path.exists(directory_name):
                    directory_name = directory_name + "_" + str(i) + "/"
                    i += 1
                os.makedirs(directory_name)
                file_move = directory_name + ntpath.basename(file)
                os.rename(file, file_move)
                file = file_tar
                tar = tarfile.open(file, "w")
                tar.add(os.path.dirname(file_move), "", False)
                tar.close()
                shutil.rmtree(os.path.dirname(os.path.realpath(file_move)))
                count += 1
        else:
            raise ExceptionFileMissing(file)

    @staticmethod
    def unarchive_tar_file(file):
        tar = tarfile.open(file)
        path = os.path.dirname(os.path.realpath(file)) + "/directory/"
        tar.extractall(path)
        tar.close()
        TheCrazyArchiver.__unarchive(path)

    @staticmethod
    def __unarchive(path_init):
        files_list = os.listdir(path_init)
        for file in files_list:
            if os.path.isfile(file):
                try:
                    tar = tarfile.open(path_init + file)
                    path_after = path_init + "/directory/"
                    tar.extractall(path_after)
                    tar.close()
                    files_list = os.listdir(path_init)
                    if files_list.__len__() > 1:
                        TheCrazyArchiver.__unarchive(path_after)
                except tarfile.ReadError:
                    print("ok")
