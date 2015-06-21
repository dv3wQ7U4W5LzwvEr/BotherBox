__author__ = 'root'

import tarfile
import os
import shutil
from tkinter import *
from tkinter.messagebox import *


def crazy_archiving(file_name, nb_loop):
    path = os.path.abspath(os.path.dirname(sys.argv[0])) + "/tmp/"
    count = 0
    while count < nb_loop:
        directory_name= "directory"
        os.makedirs(directory_name)
        os.rename(path + file_name, path + directory_name + "/" + file_name)
        tar = tarfile.TarFile(file_name, 'w')
        tar.add(directory_name, directory_name)
        tar.close()
        shutil.rmtree(path + directory_name)
        count = count + 1


# crazyArchiving("toto.tar", 30)

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
        entry_file_name= Entry(p_name, textvariable=file_name, width=20)
        p_name.add(entry_file_name)
        p_name.pack(side=TOP, fill=BOTH, padx=10)

        p_count = PanedWindow(panel_archive, orient=HORIZONTAL)
        p_count.add(Label(p_count, text="Nombre de boucle "))
        nb_loop = StringVar()
        entry_nb_loop = Entry(p_count, textvariable=nb_loop, width=4)
        p_count.add(entry_nb_loop)
        p_count.pack(side=TOP, fill=BOTH, padx=10)

        button = Button(panel_archive, text="Archiver", command=self.archive(entry_file_name, entry_nb_loop))
        button.pack(padx=10, pady=10)
        panel_archive.pack()


    def archive(self, entry_file_name, entry_nb_loop):
        file_name = entry_file_name.get()
        showinfo('Archivage', file_name)

        print(entry_file_name.get())
        if entry_file_name.get() is not "":
            exit()



it = Interface()
it.mainloop()




class SampleApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.lol()

    def lol(self):
        self.entry = Entry(self)
        self.button = Button(self, text="Get", command=self.tata)
        self.entry.pack()
        self.button.pack()


    def tata(self):
        print(self.entry.get())
        showinfo('Archivage', "lol")

app = SampleApp()
app.mainloop()
