# Для создания интерфейса (UI)  заметок  можно использовать библиотеку Python Tkinter

import tkinter as tk
from tkinter import messagebox

class NotesAppUI:
    def __init__(self, master):
        self.master = master
        self.master.title("NotesApp")
        
        self.label_title = tk.Label(master, text="Title:")
        self.label_title.grid(row=0, column=0, sticky="e")
        
        self.entry_title = tk.Entry(master)
        self.entry_title.grid(row=0, column=1, padx=5, pady=5, sticky="we")
        
        self.label_message = tk.Label(master, text="Message:")
        self.label_message.grid(row=1, column=0, sticky="e")
        
        self.entry_message = tk.Entry(master)
        self.entry_message.grid(row=1, column=1, padx=5, pady=5, sticky="we")
        
        self.button_add = tk.Button(master, text="Add Note", command=self.add_note)
        self.button_add.grid(row=2, column=0, columnspan=2, pady=5)
        
        self.list_notes = tk.Listbox(master, width=50)
        self.list_notes.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="we")

        self.button_delete = tk.Button(master, text="Delete Note", command=self.delete_note)
        self.button_delete.grid(row=4, column=0, columnspan=2, pady=5)
        
        self.load_notes()

    def load_notes(self):
        # Здесь можно загрузить список заметок из файла и отобразить их в list_notes
        pass

    def add_note(self):
        title = self.entry_title.get()
        message = self.entry_message.get()
        # Здесь можно вызвать метод добавления заметки из  класса NotesApp
        messagebox.showinfo( "Note added!")
        self.load_notes()
        self.clear_fields()

    def delete_note(self):
        # Здесь можно получить выбранный элемент из list_notes
        messagebox.showinfo( "Note deleted!")
        self.load_notes()

    def clear_fields(self):
        self.entry_title.delete(0, tk.END)
        self.entry_message.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = NotesAppUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()