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
            count = 1
            file_path = file
            while count <= nb_loop:
                file_tar = os.path.realpath(file_path) + "_" + str(count) + ".tar"
                tar = tarfile.open(file_tar, "w")
                tar.add(file, ntpath.basename(file))
                tar.close()
                os.remove(file)
                file = file_tar
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
    def unarchive(path_init):
        files_list = os.listdir(path_init)
        for file in files_list:
            if os.path.isfile(path_init + file):
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
