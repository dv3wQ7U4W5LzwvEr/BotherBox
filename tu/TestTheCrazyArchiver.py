__author__ = 'root'
import unittest
import shutil
import os
import tarfile
import sys

from TheCrazyArchiver import TheCrazyArchiver
from exception.ExceptionNbLoop import ExceptionNbLoop
from exception.ExceptionFileMissing import ExceptionFileMissing

class TestTheCrazyArchiver(unittest.TestCase):


    def test_archive_wrong_input(self):
        # input : a loop number which is a word
        with self.assertRaises(ValueError):
            TheCrazyArchiver.archive("a", "a")

        # input : a loop number negative
        with self.assertRaises(ExceptionNbLoop):
            TheCrazyArchiver.archive("a", (-1))

        # input : a wrong file name
        with self.assertRaises(ExceptionFileMissing):
            TheCrazyArchiver.archive("svsodoaae", 1)

    def test_unarchive(self):

        # creation du fichier
        fichier = open("mario", "w")
        fichier.writelines("luigi")
        fichier.close()
        # creation de l'archive
        tar = tarfile.open("mario.tar", "w")
        tar.add("mario")
        tar.close()
        os.remove("mario")

        tar = tarfile.open("peach.tar", "w")
        tar.add("mario.tar")
        tar.close()
        os.remove("mario.tar")

        tar = tarfile.open("mario.tar", "w")
        tar.add("peach.tar")
        tar.close()
        os.remove("peach.tar")
        os.rename("mario.tar", "tmp/mario.tar")

        path = os.path.abspath(os.path.dirname(sys.argv[1])) + "/tmp/mario.tar"
        TheCrazyArchiver.unarchive_tar_file(path)

        self.assertTrue(os.path.exists("tmp/directory/directory/directory/mario"))
        shutil.rmtree('tmp/directory')
        os.remove("tmp/mario.tar")

    def test_archive(self):
        fichier = open("mario", "w")
        fichier.writelines("luigi")
        fichier.close()
        os.rename("mario", "tmp/mario")

        file = "/tmp/mario"
        path = os.path.abspath(os.path.dirname(sys.argv[1])) + file
        TheCrazyArchiver.archive(path, 3)
        file_tar = file + ".tar"
        os.rename(os.path.dirname(sys.argv[1]) + "/mario.tar", os.path.dirname(sys.argv[1]) + file_tar)
        path = os.path.abspath(os.path.dirname(sys.argv[1])) + file_tar
        TheCrazyArchiver.unarchive_tar_file(path)

        self.assertTrue(os.path.exists("tmp/directory/directory/directory/mario"))