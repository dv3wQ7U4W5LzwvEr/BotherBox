__author__ = 'root'

import tarfile
import os
import ntpath
import shutil
from exception.ExceptionMissingFile import ExceptionMissingFile
from exception.ExceptionNbLoop import ExceptionNbLoop
from exception.ExceptionExistingFile import ExceptionExistingFile
from exception.ExceptionExistingTar import ExceptionExistingTar


class ArchiveMotor:

    @staticmethod
    def archive(file, nb_loop):
        # testing input
        file_path = str(file)
        nb_loop = int(nb_loop)
        if nb_loop <= 0:
            raise ExceptionNbLoop()

        if nb_loop > 19:
            nb_loop = 19

        if os.path.exists(file_path):
            file_name = os.path.basename(file_path)
            file_path_dir = os.path.dirname(file_path)
            tar_name = file_name + ".tar"
            tar_path = file_path_dir + "\\" + tar_name
            if os.path.exists(tar_path):
                raise ExceptionExistingTar(tar_path)
            count = 1
            while count <= nb_loop:
                tar_path = file_path_dir + "\\" + tar_name + "_1"
                tar = tarfile.open(tar_path, "w")
                tar.add(file_path, ntpath.basename(file_path))
                tar.close()

                if count is not 1:  # to avoid to delete original file
                    os.remove(file_path)
                tar_path_2 = file_path_dir + "\\" + tar_name
                os.rename(tar_path, tar_path_2)
                file_path = tar_path_2
                count += 1
        else:
            raise ExceptionMissingFile(file_path)

    @staticmethod
    def unarchive(file):
        file_path = os.path.realpath(file)
        tar = tarfile.open(file)
        path_tmp = os.path.dirname(os.path.realpath(file))
        tar.close()
        file_hide_path = ArchiveMotor.__unarchive(path_tmp)
        path_tmp += "\\directory"
        file_hide_path_2 = os.path.dirname(file_path) + "\\" + os.path.basename(file_hide_path)
        if os.path.exists(file_hide_path_2):
            if os.path.exists(path_tmp):
                shutil.rmtree(path_tmp)
            raise ExceptionExistingFile(file_hide_path_2)
        os.rename(file_hide_path, file_hide_path_2)
        shutil.rmtree(path_tmp)

    @staticmethod
    def __unarchive(path_dir_init):
        files_list = os.listdir(path_dir_init)
        path_before = path_dir_init + "\\"
        file_hide_path = ""
        for file in files_list:
            if os.path.isfile(path_before + file):
                try:
                    print("path init : " + path_before + " -- file : " + file)
                    tar = tarfile.open(path_before + file)
                    path_after = path_before + "directory\\"
                    tar.extractall(path_after)
                    tar.close()
                    files_list = os.listdir(path_before)
                    for f in files_list:
                        if f.endswith('.tar'):
                            file_hide_path = ArchiveMotor.__unarchive(path_after)
                except tarfile.ReadError:
                    if file_hide_path is "":
                        print("Fin de l'extraction du fichier : " + file)
                        file_hide_path = os.path.realpath(path_before + file)
                    return file_hide_path
        return file_hide_path