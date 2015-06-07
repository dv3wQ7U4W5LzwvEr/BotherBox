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

def interface():
    name = "The Crazy Archiver"
    fenetre = Tk()
    fenetre.title(name)
    fenetre.attributes("-type", 1)

    menu(fenetre)
    panelArchive(fenetre)
    fenetre.mainloop()

def menu(fenetre):
    menubar = Menu(fenetre)
    menu1 = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Archive", menu=menu1)
    menu2 = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="About", menu=menu2)
    fenetre.config(menu=menubar)

def panelArchive(fenetre):
    pName = PanedWindow(fenetre, orient=HORIZONTAL)
    pName.add(Label(pName, text="Nom de l'archive "))
    pName.add(Entry(pName, textvariable='string', width=20))
    pName.pack(side=TOP, expand=Y, fill=BOTH, padx=10)

    pCount = PanedWindow(fenetre, orient=HORIZONTAL)
    pCount.add(Label(pCount, text="Nombre de boucle "))
    pCount.add(Entry(pCount, textvariable='string', width=4))
    pCount.pack(side=TOP, expand=Y, fill=BOTH, padx=10)

    Button(fenetre, text="Archiver", command=fenetre.quit).pack(padx=10, pady=10)







interface()