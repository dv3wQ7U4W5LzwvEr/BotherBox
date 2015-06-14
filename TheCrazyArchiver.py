__author__ = 'root'

import tarfile
import os
import shutil
from tkinter import *



def crazyArchiving(fileName, nbArchives):
    path = os.path.abspath(os.path.dirname(sys.argv[0])) + "/tmp/"
    count = 0
    while(count < nbArchives):
        directoryName = "directory"
        os.makedirs(directoryName)
        os.rename(path + fileName, path + directoryName + "/" + fileName)
        tar = tarfile.TarFile(fileName, 'w')
        tar.add(directoryName, directoryName)
        tar.close()
        shutil.rmtree(path + directoryName)
        count = count + 1


# crazyArchiving("toto.tar", 30)

class Interface:

    def __init__(self):
        name = "The Crazy Archiver"
        self.fenetre = Tk()
        self.fenetre.title(name)
        self.fenetre.attributes("-type", 1)
        self.panelAbout = PanedWindow(self.fenetre, orient=HORIZONTAL)
        self.panelArchive = PanedWindow(self.fenetre, orient=HORIZONTAL)
        self.menu()
        self.manageEvent()

    def menu(self):
        menubar = Menu(self.fenetre, tearoff=0)
        menubar.add_command(label="Archive", postcommand=self.displayPanelArchive())
        menubar.add_command(label="About")
        self.fenetre.config(menu=menubar)


    def manageEvent(self):
        self.fenetre.bind("Archive", self.displayPanelArchive())
        self.fenetre.bind("About", self.displayPanelAbout())

    def displayPanelArchive(self):
        self.panelAbout.pack_forget()
        self.createPanelArchive()

    def createPanelArchive(self):
        pName = PanedWindow(self.panelArchive, orient=HORIZONTAL)
        pName.add(Label(pName, text="Nom de l'archive "))
        pName.add(Entry(pName, textvariable='string', width=20))
        pName.pack(side=TOP, fill=BOTH, padx=10)

        pCount = PanedWindow(self.panelArchive, orient=HORIZONTAL)
        pCount.add(Label(pCount, text="Nombre de boucle "))
        pCount.add(Entry(pCount, textvariable='string', width=4))
        pCount.pack(side=TOP, fill=BOTH, padx=10)

        Button(self.panelArchive, text="Archiver", command=self.fenetre.quit).pack(padx=10, pady=10)
        self.panelArchive.pack()

    def displayPanelAbout(self):
        self.panelArchive.pack_forget()
        self.createPanelAbout()

    def createPanelAbout(self):
        self.panelAbout.add(Label(self.panelAbout, text="Cet utilitaire a été créé par Florian Vautard"))
        self.panelAbout.pack(side=TOP, fill=BOTH, padx=10)

    def readInterface(self):
        self.fenetre.mainloop()


it = Interface()
it.readInterface()