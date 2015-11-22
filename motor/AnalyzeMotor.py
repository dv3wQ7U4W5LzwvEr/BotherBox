__author__ = 'florian'

import os
import datetime
import subprocess

from exception.ExceptionPermissionDenied import ExceptionPermissionDenied
from exception.ExceptionMissingDirectory import ExceptionMissingDirectory

class AnalyzeMotor:

    ANALYZE_FILE_NAME = "/analyze.txt"

    @staticmethod
    def analyze_from_directory(path_directory):
        if path_directory != "":
            try:
                file_name = os.environ["TEMP"] + AnalyzeMotor.ANALYZE_FILE_NAME
                file = open(file_name, "w", encoding='utf-8')
                file.write("Analyze of " + path_directory + "\n")
                AnalyzeMotor.__parse_directory(path_directory, file, "")
                file.close()
                subprocess.Popen([os.environ["WINDIR"] + "\system32\\notepad.exe", file_name])
            except PermissionError:
                raise ExceptionPermissionDenied(path_directory)
            except FileNotFoundError:
                raise ExceptionMissingDirectory(path_directory)
        else:
            raise ExceptionMissingDirectory(path_directory)

    @staticmethod
    def __parse_directory(path_directory, file, indent):
        path = path_directory
        try:
            list_all_dirs_files = os.listdir(path)
            list_all_dirs_files.sort()
            for f in list_all_dirs_files:
                path = path_directory + "/" + f
                if f != "__init__.py":
                    try:
                        if os.path.isfile(path):
                            file.write(indent + f + "\n")
                        if os.path.isdir(path):
                            file.write(indent + f + "\n")
                            AnalyzeMotor.__parse_directory(path, file, indent + "   ")
                    except IOError:
                        text = " Can't read " + path
                        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + text)
                        file.write(indent + text + "\n")
        except IOError:
            text = " Can't read " + path
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + text)
            file.write(indent + text + "\n")
