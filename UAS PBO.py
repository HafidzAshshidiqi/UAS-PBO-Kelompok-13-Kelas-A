from tkinter import *
from tkinter import messagebox as msg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
#mengimport tkinter untuk membuat Gui pada python
class Notepad(Tk):
    def __init__(self):
        super().__init__()
        self.minsize(600,600)
        self.title("Notepad")
        self.wm_iconbitmap('notepad.ico')
        self.file = None
        self._textArea()
        self._menu()
#Membuat Kelas Notepad pada tkinter python

    def about_notepad(self):
        msg.showinfo('About Notepad', 'This is created by Keisya and Hafidz')
#Membuat Fungsi About_notepad merupakan tools yang berisikan tentang di dalam notepad 

    def copy(self):
        self.textbox.event_generate('<<Copy>>')
#Membuat Fungsi Copy untuk menyalin teks pada notepad

    def paste(self):
        self.textbox.event_generate('<<Paste>>')
#Membuat Fungsi Paste untuk menempel teks yang sudah disalin ke tempat notepad/baris yang dituju atau tempat dipindahkan

    def cut(self):
        self.textbox.event_generate('<<Cut>>')
#Membuat Fungsi Cut untuk memotong teks ke baris atau tempat lain

    def exit(self):
        self.destroy()
#Membuat Fungsi exit untuk keluar dari Notepad

    def open_file(self):
        if self.textbox.get(1.0, END) != '\n':  # Memeriksa apakah teks ada di dalam textbox
            answer = msg.askyesnocancel("Save", "Do you want to save the current file?")
            if answer:
                self.save_file()
            elif answer is None:
                return

        self.file = askopenfilename(filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')])
        if self.file == '':
            self.file = None
        else:
            self.title(os.path.basename(self.file) + ' - Notepad')
            with open(self.file, 'r') as f:
                self.textbox.delete(1.0, END)  # Menghapus teks sebelumnya sebelum membuka file baru
                self.textbox.insert(1.0, f.read())
#Fungsi untuk membuka file notepad yang sudah ada

    def new_file(self):
        if self.textbox.get(1.0, END) != '\n':  # Memeriksa apakah teks ada di dalam textbox
            answer = msg.askyesnocancel("Save", "Do you want to save the current file?")
            if answer:
                self.save_file()
            elif answer is None:
                return

        self.textbox.delete(1.0, END)
        self.title('Untitled - Notepad')
        self.file = None
#Fungsi untuk membuat file teks baru pada notepad

    def save_file(self):
        if self.file is None:
            self.file = asksaveasfilename(initialfile='Untitled.txt', defaultextension='.txt', filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')])
            if self.file == '':
                self.file = None
            else:
                with open(self.file, 'w') as f:
                    f.write(self.textbox.get(1.0, END))
                self.title(os.path.basename(self.file) + ' - Notepad')

        else:
            with open(self.file, 'w') as f:
                f.write(self.textbox.get(1.0, END))
#Fungsi untuk menyimpan file notepad ke folder komputer

    def _textArea(self):
        self.textbox = Text(self, font='lucida 12')
        self.textbox.pack(fill = BOTH, expand = 1)
        self.scrollbar = Scrollbar(self.textbox)
        self.scrollbar.pack(side = RIGHT, fill = Y)
        self.scrollbar.config(command = self.textbox.yview)
        self.textbox.config(yscrollcommand = self.scrollbar.set)
#Membuat tempat atau kolom teks pada notepad dan membuat scrollbar

    def _menu(self):
        self.menubar = Menu(self)
        self.config(menu = self.menubar)
        self.file_menu = Menu(self.menubar, tearoff = 0)
        self.menubar.add_cascade(label = 'File', menu = self.file_menu)
        self.file_menu.add_command(label = 'New File', command = self.new_file)
        self.file_menu.add_command(label = 'Open File', command = self.open_file)
        self.file_menu.add_command(label = 'Save File', command = self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label = 'Exit', command = self.exit)

        self.edit_menu = Menu(self.menubar, tearoff = 0)
        self.menubar.add_cascade(label = 'Edit', menu = self.edit_menu)
        self.edit_menu.add_command(label = 'Copy', command = self.copy)
        self.edit_menu.add_command(label = 'Cut', command = self.cut)
        self.edit_menu.add_command(label = 'Paste', command = self.paste)

        self.about_menu = Menu(self.menubar, tearoff = 0)
        self.menubar.add_cascade(label = 'About', menu = self.about_menu)
        self.about_menu.add_command(label = 'About Notepad', command = self.about_notepad)

#membuat bagian menu bar pada Notepad yang berisikan 3 tools yaitu File, Edit, dan About

window = Notepad()
window.mainloop()
        
