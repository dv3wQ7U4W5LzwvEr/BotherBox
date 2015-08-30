__author__ = 'root'

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror

from LocalisationFr import LocalisationFr
from exception.ExceptionFileMissing import ExceptionFileMissing
from TheCrazyArchiver import TheCrazyArchiver


class Interface(Tk):
    def __init__(self):
        Tk.__init__(self)
        name = LocalisationFr.WINDOW_PROGRAM_NAME.value
        self.title(name)
        self.panel_archive = self.panel_archive()
        self.panel_unarchive = self.panel_unarchive()
        self.menu()

    def menu(self):
        menubar = Menu(self, tearoff=0)
        menubar.add_command(label=LocalisationFr.PANEL_ARCHIVE_WINDOW_NAME.value, command=self.show_panel_archive)
        menubar.add_command(label=LocalisationFr.PANEL_UNARCHIVE.value, command=self.show_panel_unarchive)
        self.config(menu=menubar)

    def show_panel_archive(self):
        self.panel_unarchive.pack_forget()
        self.panel_archive.pack()

    def show_panel_unarchive(self):
        self.panel_archive.pack_forget()
        self.panel_unarchive.pack()

    def panel_archive(self):
        panel_archive = PanedWindow(self, orient=HORIZONTAL)
        p_name = PanedWindow(panel_archive, orient=HORIZONTAL)
        p_name.add(Label(p_name, text=LocalisationFr.PANEL_ARCHIVE_FILE_NAME.value))
        self.entry_file_name = Entry(p_name, textvariable=StringVar())
        p_name.add(self.entry_file_name)

        p_name.add(Button(panel_archive, text="Browse", command=self.load_file, width=5))
        p_name.pack(side=TOP, fill=BOTH, padx=5)


        p_count = PanedWindow(panel_archive, orient=HORIZONTAL)
        p_count.add(Label(p_count, text=LocalisationFr.PANEL_ARCHIVE_LOOP.value))
        self.entry_nb_loop = Entry(self, textvariable=StringVar(), width=4)
        p_count.add(self.entry_nb_loop)
        p_count.pack(side=TOP, padx=10)

        Button(panel_archive, text=LocalisationFr.PANEL_ARCHIVE_BUTTON.value, command=self.launchArchiving).pack(
            padx=10, pady=10)
        panel_archive.pack()
        return panel_archive

    def panel_unarchive(self):
        panel_unarchive = PanedWindow(self, orient=HORIZONTAL)
        p_name = PanedWindow(panel_unarchive, orient=HORIZONTAL)
        p_name.add(Label(p_name, text=LocalisationFr.PANEL_ARCHIVE_FILE_NAME.value))
        self.entry_file_name = Entry(p_name, textvariable=StringVar(), width=20)
        p_name.add(self.entry_file_name)

        p_name.pack(side=TOP, fill=BOTH, padx=10)

        Button(panel_unarchive, text=LocalisationFr.PANEL_UNARCHIVE_BUTTON.value, command=self.launchUnarchiving).pack(
            padx=10, pady=10)
        return panel_unarchive

    def launchArchiving(self):
        try:
            file_name = str(self.entry_file_name.get())
            nb_loop = int(self.entry_nb_loop.get())
            TheCrazyArchiver.archive(file_name, nb_loop)
            message = "Félicitation ! Le fichier '" + file_name + "' a bien été archivé récursivement " + str(
                nb_loop) + " fois."
            messagebox.showinfo("Information", message)
        except ValueError:
            messagebox.showerror(LocalisationFr.MESSAGE_TITLE_EMPTY_NAME_FILE_OR_LOOP,
                                 LocalisationFr.MESSAGE_EMPTY_NAME_FILE_OR_LOOP.value)
        except IOError:
            messagebox.showerror(LocalisationFr.EXCEPTION_FILE_MISSING)
        except ExceptionFileMissing as e:
            messagebox.showerror(LocalisationFr.MESSAGE_ERROR.value, e.value)

    def launchUnarchiving(self):
        try:
            file_name = str(self.entry_file_name.get())
            nb_loop = int(self.entry_nb_loop.get())
            TheCrazyArchiver.unarchive(file_name)
            message = "Félicitation ! Le fichier '" + file_name + "' a bien été désarchivé récursivement "
            messagebox.showinfo(LocalisationFr.MESSAGE_INFORMATION, message)
        except ValueError:
            messagebox.showerror(LocalisationFr.MESSAGE_WARNING.value,
                                 LocalisationFr.MESSAGE_EMPTY_NAME_FILE_OR_LOOP.value)
        except IOError:
            messagebox.showerror(LocalisationFr.EXCEPTION_FILE_MISSING)
        except ExceptionFileMissing as e:
            messagebox.showerror(LocalisationFr.MESSAGE_ERROR.value, e.value)

    def load_file(self):
        fname = askopenfilename()
        if fname:
            try:
                print("""here it comes: self.settings["template"].set(fname)""")
            except:  # <- naked except is a bad idea
                showerror("Open Source File", "Failed to read file\n'%s'" % fname)
            return


i = Interface()
i.mainloop()
