from tkinter import *
from tkinter import messagebox as msg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

class Window(Tk):
    def __init__(self):
        super().__init__()
        self.minsize(600, 600)
        self.title("Notepad")
        self.wm_iconbitmap('notepad.ico')
        self.file = None
        self._textArea()
        self._menu()
        self.textbox.insert(END, "Tulis catatan anda di sini...")
        self.textbox.configure(font=("Arial", 12))
        self.textbox.bind("<Button-1>", self.clear_placeholder)

    def clear_placeholder(self, event):
        if self.textbox.get("1.0", "end-1c") == "Tulis catatan anda di sini...":
            self.textbox.delete("1.0", END)

    def about_notepad(self):
        msg.showinfo('About Notepad', 'This is created by Keisya and Hafidz')

    def copy(self):
        self.textbox.event_generate('<<Copy>>')

    def paste(self):
        self.textbox.event_generate('<<Paste>>')

    def cut(self):
        self.textbox.event_generate('<<Cut>>')

    def exit(self):
        self.destroy()

    def open_file(self):
        if self.textbox.get("1.0", END) != '\n':  # Memeriksa apakah teks ada di dalam textbox
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
                self.textbox.delete("1.0", END)  # Menghapus teks sebelumnya sebelum membuka file baru
                self.textbox.insert("1.0", f.read())

    def new_file(self):
        if self.textbox.get("1.0", END) != '\n':  # Memeriksa apakah teks ada di dalam textbox
            answer = msg.askyesnocancel("Save", "Do you want to save the current file?")
            if answer:
                self.save_file()
            elif answer is None:
                return

        self.textbox.delete("1.0", END)
        self.title('Untitled - Notepad')
        self.file = None

    def save_file(self):
        if self.file is None:
            self.file = asksaveasfilename(initialfile='Untitled.txt', defaultextension='.txt',
                                          filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')])
            if self.file == '':
                self.file = None
            else:
                with open(self.file, 'w') as f:
                    f.write(self.textbox.get("1.0", END))
                self.title(os.path.basename(self.file) + ' - Notepad')

        else:
            with open(self.file, 'w') as f:
                f.write(self.textbox.get("1.0", END))
    
    def _textArea(self):
        self.textbox = Text(self, font='lucida 12')
        self.textbox.pack(fill = BOTH, expand = 1)
        self.scrollbar = Scrollbar(self.textbox)
        self.scrollbar.pack(side = RIGHT, fill = Y)
        self.scrollbar.config(command = self.textbox.yview)
        self.textbox.config(yscrollcommand = self.scrollbar.set)
    
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

window = Window()
window.mainloop()
        
