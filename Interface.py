__author__ = 'root'

import datetime
import tarfile
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror

from motor.AnalyzeMotor import AnalyzeMotor
from motor.ArchiveMotor import ArchiveMotor

from exception.ExceptionExistingFile import ExceptionExistingFile
from exception.ExceptionExistingTar import ExceptionExistingTar
from exception.ExceptionMissingDirectory import ExceptionMissingDirectory
from exception.ExceptionMissingFile import ExceptionMissingFile
from exception.ExceptionMissingTar import ExceptionMissingTar
from exception.ExceptionPermissionDenied import ExceptionPermissionDenied
from motor.ArchiveMotor import ArchiveMotor
from package.fr.Localisation import Localisation
from package.fr.Localisation_About import Localisation_About
from package.fr.Localisation_Files_Finder import Localisation_Files_Finder
from package.fr.Localisation_Hidify import Localisation_Hidify


class Interface(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title(Localisation.WINDOW_PROGRAM_NAME.value)
        self.panel_hidify = self.create_panel_hidify()
        self.files_finder = self.create_panel_files_finder()
        self.panel_about = self.create_panel_about()
        self.menu()
        self.resizable(width=FALSE, height=FALSE)
        self.show_panel_hidify()

    def menu(self):
        menubar = Menu(self, tearoff=0)
        menubar.add_command(label=Localisation_Hidify.PANEL_NAME.value, command=self.show_panel_hidify)
        menubar.add_command(label=Localisation_Files_Finder.PANEL_NAME.value, command=self.show_panel_finder)
        menubar.add_command(label=Localisation_Hidify.PANEL_ABOUT.value, command=self.show_panel_about)

        self.config(menu=menubar)

    def show_panel_about(self):
        self.panel_hidify.pack_forget()
        self.files_finder.pack_forget()
        self.panel_about.pack()

    def show_panel_hidify(self):
        self.panel_hidify.pack()
        self.files_finder.pack_forget()
        self.panel_about.pack_forget()

    def show_panel_finder(self):
        self.panel_hidify.pack_forget()
        self.files_finder.pack()
        self.panel_about.pack_forget()


    def create_panel_hidify(self):
        p_hidify = PanedWindow(self, orient=VERTICAL)

        p_input_file = PanedWindow(p_hidify, orient=HORIZONTAL)
        p_input_file.add(Label(p_input_file, text=Localisation_Hidify.PANEL_ARCHIVE_FILE_NAME.value))
        self.input_file_path = Entry(p_input_file, textvariable=StringVar(), width=50)
        p_input_file.add(self.input_file_path)
        p_input_file.add(Button(p_hidify, text=Localisation.TEXT_BROWSE.value, command=self.load_file))

        p_features = PanedWindow(p_hidify, orient=HORIZONTAL)
        p_archive = PanedWindow(self, orient=VERTICAL)
        p_count = PanedWindow(p_archive, orient=HORIZONTAL)
        p_count.add(Label(p_count, text=Localisation_Hidify.PANEL_ARCHIVE_LOOP.value))
        self.archive_input_loop = Entry(self, textvariable=StringVar(), width=4)
        p_count.add(self.archive_input_loop)

        p_archive.add(p_count)
        p_archive.add(Button(p_archive, text=Localisation_Hidify.PANEL_ARCHIVE_BUTTON.value, command=self.launchArchiving))

        p_unarchive = PanedWindow(self)
        b_unarchiving = Button(p_unarchive, text=Localisation_Hidify.PANEL_UNARCHIVE_BUTTON.value, command=self.launch_unarchiving)
        p_unarchive.add(b_unarchiving)

        p_hidify.add(p_input_file)
        p_hidify.add(p_features)
        p_features.add(p_archive)
        p_features.add(p_unarchive)

        return p_hidify

    def create_panel_files_finder(self):
        p_analyze = PanedWindow(self)
        p_analyze_content = PanedWindow(p_analyze, orient=HORIZONTAL)
        p_analyze_content.add(Label(p_analyze_content, text=Localisation_Files_Finder.PANEL_ANALYSE_CONTENT.value))
        p_analyze.add(p_analyze_content)

        self.analyze_input_directory_path = Entry(p_analyze_content, textvariable=StringVar(), width=50)
        p_analyze_content.add(self.analyze_input_directory_path)
        p_analyze_content.add(Button(p_analyze_content, text=Localisation.TEXT_BROWSE.value, command=self.load_directory))

        b_analyze = Button(p_analyze, text=Localisation_Files_Finder.PANEL_ANALYSE_BUTTON.value, command=self.launch_analyze)
        p_analyze.add(b_analyze)

        return p_analyze

    def create_panel_about(self):
        p_about = PanedWindow(self, orient=HORIZONTAL)
        p_about.add(Label(p_about, text=Localisation_About.PANEL_ABOUT_CONTENT.value))

        return p_about

    def launchArchiving(self):
        try:
            input_file_path = str(self.input_file_path.get())
            nb_loop = int(self.archive_input_loop.get())
            ArchiveMotor.archive(input_file_path, nb_loop)
            message = "Félicitation ! Le fichier '" + input_file_path + "' a bien été archivé récursivement " + str(
                nb_loop) + " fois."
            messagebox.showinfo("Information", message)
        except ValueError:
            messagebox.showerror(Localisation_Hidify.MESSAGE_ERROR.value,
                                 Localisation_Hidify.MESSAGE_EMPTY_NAME_FILE_OR_LOOP.value)
        except IOError:
            messagebox.showerror(Localisation_Hidify.ExceptionFileMissing(input_file_path))
        except ExceptionMissingFile as e:
            messagebox.showerror(Localisation_Hidify.MESSAGE_ERROR.value, e.value)
        except ExceptionExistingTar as e:
            messagebox.showerror(Localisation_Hidify.MESSAGE_ERROR.value, e.value)

    def launch_unarchiving(self):
        try:
            input_file_path = str(self.input_file_path.get())
            ArchiveMotor.unarchive(input_file_path)
            message = "Félicitation ! Le fichier '" + input_file_path + "' a bien été désarchivé récursivement "
            messagebox.showinfo(Localisation_Hidify.MESSAGE_INFORMATION.value, message)
        except ValueError:
            messagebox.showerror(Localisation_Hidify.MESSAGE_WARNING.value,
                                 Localisation_Hidify.MESSAGE_EMPTY_NAME.value)
        except IOError:
                messagebox.showerror(Localisation_Hidify.MESSAGE_ERROR.value, ExceptionMissingFile(input_file_path))
        except ExceptionMissingFile as e:
            messagebox.showerror(Localisation_Hidify.MESSAGE_ERROR.value, e.value)
        except tarfile.ReadError:
            messagebox.showerror(Localisation_Hidify.MESSAGE_ERROR.value, ExceptionMissingTar(input_file_path))
        except ExceptionExistingFile as e:
            messagebox.showerror(Localisation_Hidify.MESSAGE_ERROR.value, e.value)

    def load_file(self):
        fname = askopenfilename()
        if fname:
            try:
                self.reset_input_file()
                self.input_file_path.insert(0, fname)
            except:
                showerror("Ouverture du fichier", "Impossible de lire le fichier\n'%s'" % fname)


    def reset_input_file(self):
        self.input_file_path.delete(0, 10000)

    def load_directory(self):
        directory_path = askdirectory()
        if directory_path:
            try:
                self.analyze_input_directory_path.delete(0, 10000)
                self.analyze_input_directory_path.insert(0, directory_path)
            except IOError:
                showerror("Ouverture du fichier", "Impossible de lire le fichier\n'%s'" % directory_path)

    def launch_analyze(self):
        directory_path = self.analyze_input_directory_path.get()
        try:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " Analyze begin of " + directory_path)
            AnalyzeMotor.analyze_from_directory(directory_path)
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " Analyze completed of " + directory_path)
            messagebox.showinfo(Localisation_Files_Finder.MESSAGE_TYPE_INFORMATION.value, Localisation_Files_Finder.MESSAGE_SUCCESS.value)
        except ValueError:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + Localisation_Files_Finder.LOG_ERROR.value)
            messagebox.showerror(Localisation_Files_Finder.MESSAGE_TYPE_ERROR.value, Localisation_Files_Finder.LOG_ERROR.value)
        except ExceptionMissingDirectory:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " " + str(Localisation_Files_Finder(directory_path)))
            messagebox.showerror(Localisation_Files_Finder.MESSAGE_TYPE_ERROR.value, Localisation_Files_Finder(directory_path))
        except ExceptionPermissionDenied:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " " +  str(Localisation_Files_Finder(directory_path)))
            messagebox.showerror(Localisation_Files_Finder.MESSAGE_TYPE_ERROR.value, ExceptionPermissionDenied(directory_path))