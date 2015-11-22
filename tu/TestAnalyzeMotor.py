__author__ = 'root'
import unittest
import shutil
import os

from exception.ExceptionMissingDirectory import ExceptionMissingDirectory

from AnalyzeMotor import AnalyzeMotor


class TestArchiveMotor(unittest.TestCase):
    TMP_PATH = os.path.dirname(os.path.abspath(__file__)) + "\\tmp"

    def setUp(self):
        if os.path.isdir(self.TMP_PATH):
            shutil.rmtree(self.TMP_PATH)
        os.makedirs(self.TMP_PATH)
        os.rename("__init__.py", self.TMP_PATH + "/__init__.py")
        fichier = open("__init__.py", "w")
        fichier.close()

    def test_wrong_input(self):
        # input : a wrong directory path name
        with self.assertRaises(ExceptionMissingDirectory):
            AnalyzeMotor.analyze_from_directory("svsodoaae")

    def test_analyze(self):
        file_path = self.TMP_PATH
        # creation du fichier
        file = open(file_path + "\salameche", "w")
        file.close()
        file = open(file_path + "\carapuce", "w")
        file.close()

        directory_temp = self.TMP_PATH + "\directory"
        os.makedirs(directory_temp)
        file = open(directory_temp + "\pikachu", "w")
        file.close()
        file = open(directory_temp + "\mewtwo", "w")
        file.close()

        AnalyzeMotor.analyze_from_directory(self.TMP_PATH)
        file_generate = os.environ["TEMP"] + AnalyzeMotor.ANALYZE_FILE_NAME
        file = open(file_generate, "r")
        self.assertTrue(file.read().find("salameche"))
        self.assertTrue(file.read().find("carapuce"))
        self.assertTrue(file.read().find("mewtwo") == -1)
        file.close()

    def tearDown(self):
        if os.path.isdir(self.TMP_PATH):
            shutil.rmtree(self.TMP_PATH)