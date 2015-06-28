__author__ = 'root'

from tkinter import *
from tkinter import messagebox

from Message import Message
from exception import ExceptionFileMissing
from TheCrazyArchiver import TheCrazyArchiver


class Interface(Tk):

    def __init__(self):
        Tk.__init__(self)
        name = "The Crazy Archiver"
        self.title(name)
        self.panel_archive()
        self.menu()

    def menu(self):
        menubar = Menu(self, tearoff=0)
        menubar.add_command(label="Archive")
        self.config(menu=menubar)

    def panel_archive(self):
        panel_archive = PanedWindow(self, orient=HORIZONTAL)
        p_name = PanedWindow(panel_archive, orient=HORIZONTAL)
        p_name.add(Label(p_name, text="Nom de l'archive "))
        file_name = StringVar()
        self.entry_file_name = Entry(p_name, textvariable=file_name, width=20)
        p_name.add(self.entry_file_name)
        p_name.pack(side=TOP, fill=BOTH, padx=10)

        p_count = PanedWindow(panel_archive, orient=HORIZONTAL)
        p_count.add(Label(p_count, text="Nombre de boucle "))
        nb_loop = StringVar()
        self.entry_nb_loop = Entry(self, textvariable=nb_loop, width=4)
        p_count.add(self.entry_nb_loop)
        p_count.pack(side=TOP, fill=BOTH, padx=10)

        button = Button(panel_archive, text="Archiver", command=self.launchArchiving)
        button.pack(padx=10, pady=10)
        panel_archive.pack()

    def launchArchiving(self):
        try:
            file_name = str(self.entry_file_name.get())
            nb_loop = int(self.entry_nb_loop.get())
            TheCrazyArchiver.archive(file_name, nb_loop)
            message = "Félicitation ! Le fichier '" + file_name + "' a bien été archivé récursivement " + str(nb_loop) + " fois."
            messagebox.showinfo("Information", message)
        except ValueError:
            messagebox.showerror("Attention", Message.MESSAGE_VIDE.value)
        except IOError:
            messagebox.showerror(Message.EXCEPTION_FILE_MISSING)
        except ExceptionFileMissing as e:
            messagebox.showerror("Erreur", e.value)

