__author__ = 'root'

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
import tarfile

from LocalisationFr import LocalisationFr
from exception.ExceptionMissingFile import ExceptionMissingFile
from exception.ExceptionMissingTar import ExceptionMissingTar
from exception.ExceptionExistingTar import ExceptionExistingTar
from exception.ExceptionExistingFile import ExceptionExistingFile
from ArchiveMotor import ArchiveMotor


class Interface(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title(LocalisationFr.WINDOW_PROGRAM_NAME.value)
        self.panel_hidify = self.create_panel_hidify()
        self.panel_about = self.create_panel_about()
        self.menu()
        self.resizable(width=FALSE, height=FALSE)
        self.show_panel_hidify()

    def menu(self):
        menubar = Menu(self, tearoff=0)
        menubar.add_command(label=LocalisationFr.PANEL_HIDIFY.value, command=self.show_panel_hidify)
        menubar.add_command(label=LocalisationFr.PANEL_ABOUT.value, command=self.show_panel_about)

        self.config(menu=menubar)

    def show_panel_about(self):
        self.panel_hidify.pack_forget()
        self.panel_about.pack()

    def show_panel_hidify(self):
        self.panel_hidify.pack()
        self.panel_about.pack_forget()

    def create_panel_hidify(self):
        p_hidify = PanedWindow(self, orient=VERTICAL)

        p_input_file = PanedWindow(p_hidify, orient=HORIZONTAL)
        p_input_file.add(Label(p_input_file, text=LocalisationFr.PANEL_ARCHIVE_FILE_NAME.value))
        self.input_file_path = Entry(p_input_file, textvariable=StringVar(), width=50)
        p_input_file.add(self.input_file_path)
        p_input_file.add(Button(p_hidify, text=LocalisationFr.TEXT_BROWSE.value, command=self.load_file))

        p_features = PanedWindow(p_hidify, orient=HORIZONTAL)
        p_archive = PanedWindow(self, orient=VERTICAL)
        p_count = PanedWindow(p_archive, orient=HORIZONTAL)
        p_count.add(Label(p_count, text=LocalisationFr.PANEL_ARCHIVE_LOOP.value))
        self.archive_input_loop = Entry(self, textvariable=StringVar(), width=4)
        p_count.add(self.archive_input_loop)

        p_archive.add(p_count)
        p_archive.add(Button(p_archive, text=LocalisationFr.PANEL_ARCHIVE_BUTTON.value, command=self.launchArchiving))

        p_unarchive = PanedWindow(self)
        b_unarchiving = Button(p_unarchive, text=LocalisationFr.PANEL_UNARCHIVE_BUTTON.value, command=self.launch_unarchiving)
        p_unarchive.add(b_unarchiving)

        p_hidify.add(p_input_file)
        p_hidify.add(p_features)
        p_features.add(p_archive)
        p_features.add(p_unarchive)

        return p_hidify

    def create_panel_about(self):
        p_about = PanedWindow(self, orient=HORIZONTAL)
        p_about.add(Label(p_about, text=LocalisationFr.PANEL_ABOUT_CONTENT.value))

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
            messagebox.showerror(LocalisationFr.MESSAGE_ERROR.value,
                                 LocalisationFr.MESSAGE_EMPTY_NAME_FILE_OR_LOOP.value)
        except IOError:
            messagebox.showerror(LocalisationFr.ExceptionFileMissing(input_file_path))
        except ExceptionMissingFile as e:
            messagebox.showerror(LocalisationFr.MESSAGE_ERROR.value, e.value)
        except ExceptionExistingTar as e:
            messagebox.showerror(LocalisationFr.MESSAGE_ERROR.value, e.value)

    def launch_unarchiving(self):
        try:
            input_file_path = str(self.input_file_path.get())
            ArchiveMotor.unarchive(input_file_path)
            message = "Félicitation ! Le fichier '" + input_file_path + "' a bien été désarchivé récursivement "
            messagebox.showinfo(LocalisationFr.MESSAGE_INFORMATION.value, message)
        except ValueError:
            messagebox.showerror(LocalisationFr.MESSAGE_WARNING.value,
                                 LocalisationFr.MESSAGE_EMPTY_NAME.value)
        except IOError:
                messagebox.showerror(LocalisationFr.MESSAGE_ERROR.value, ExceptionMissingFile(input_file_path))
        except ExceptionMissingFile as e:
            messagebox.showerror(LocalisationFr.MESSAGE_ERROR.value, e.value)
        except tarfile.ReadError:
            messagebox.showerror(LocalisationFr.MESSAGE_ERROR.value, ExceptionMissingTar(input_file_path))
        except ExceptionExistingFile as e:
            messagebox.showerror(LocalisationFr.MESSAGE_ERROR.value, e.value)

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