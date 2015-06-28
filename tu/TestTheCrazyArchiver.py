__author__ = 'root'
import unittest

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
        TheCrazyArchiver.unarchive_tar_file("a.tar")
