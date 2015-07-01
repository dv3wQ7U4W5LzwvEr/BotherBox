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
        exctract_native_directory_path = os.path.abspath(os.path.dirname(sys.argv[1])) + "/tmp/"
        tar = tarfile.open(exctract_native_directory_path + file_name)
        path = exctract_native_directory_path + "directory/"
        tar.extractall(path)
        tar.close()
        TheCrazyArchiver.unarchive(path)

    @staticmethod
    def unarchive(path_init):
        files_list = os.listdir(path_init)
        for file in files_list:
            try:
                tar = tarfile.open(path_init + file)
                path_after = path_init + "directory/"
                tar.extractall(path_after)
                tar.close()
                files_list = os.listdir(path_init)
                if files_list.__len__() > 1:
                    TheCrazyArchiver.unarchive(path_after)
            except tarfile.ReadError:
                print("ok")
