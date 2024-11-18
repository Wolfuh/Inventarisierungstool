import tkinter as tk
from tkinter import ttk, messagebox
import os

import Einstellungen  # Should be a class instead of a module if instantiated
import Mainpages
import Overview_pages
import ThemeManager
import Profiles
import importlib.util

# login_DB
login_DB_path = './db/login_DB.py'

# Load and import module dynamically
spec = importlib.util.spec_from_file_location("login_DB", login_DB_path)
login_DB = importlib.util.module_from_spec(spec)
spec.loader.exec_module(login_DB)


class GuiTest(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Prototyp")
        self.resizable(False, False)
        self.geometry("1920x1080")

        # Main container for frames
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # Only attempt to instantiate Einstellungen if it's a class
        pages = [LogInWindow, Mainpages.MainPage, Mainpages.MainPageS2,
                 Overview_pages.Ubersicht, Overview_pages.Gerateansicht,
                 Profiles.Profil, Profiles.Admin, Profiles.Stats]

        if hasattr(Einstellungen, "Einstellungen"):
            pages.append(Einstellungen.Einstellungen)

        for Page in pages:
            frame = Page(container, self)
            self.frames[Page] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Mainpages.MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class LogInWindow(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(bg='white')

        header = ttk.Label(self, text="Login", anchor="center", style="Header.TLabel")
        bottom = ttk.Label(self, style="Footer.TLabel")

        style = ttk.Style()
        style.configure("Header.TLabel", foreground='white', background=ThemeManager.SRH_Orange,
                        font=("Inter", 50, 'bold'))
        style.configure("Footer.TLabel", background=ThemeManager.SRH_Grey)

        def login():
            if login_DB.login_lookup(username_entry.get(), password_entry.get()):
                controller.show_frame(Mainpages.MainPage)
                username_entry.delete(0, 'end')
                password_entry.delete(0, 'end')
            else:
                messagebox.showinfo(title="Fehler", message="Passwort oder Benutzername falsch")
                password_entry.delete(0, 'end')

        # Login Frame Elements
        login_frame = tk.Frame(self, bg='white')
        username_label = tk.Label(login_frame, text="Benutzername", bg='white', font=("Inter", 19))
        username_entry = tk.Entry(login_frame, bg='white', font=("Inter", 15))
        password_label = tk.Label(login_frame, text="Passwort", bg='white', font=("Inter", 19))
        password_entry = tk.Entry(login_frame, show="*", bg='white', font=("Inter", 15))
        login_button = tk.Button(login_frame, text="Login", bg='#081424', fg='white', font=("Inter", 20, 'bold'),
                                 command=login)

        username_label.grid(row=0, column=0, pady=10)
        username_entry.grid(row=1, column=0, pady=10)
        password_label.grid(row=2, column=0, pady=10)
        password_entry.grid(row=3, column=0, pady=10)
        login_button.grid(row=4, column=0, pady=20)

        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)
        bottom.place(relx=0, rely=0.85, relwidth=1, relheight=0.13)
        login_frame.place(relx=0.5, rely=0.5, anchor="center")


def load_image(image_path):
    if os.path.exists(image_path):
        return tk.PhotoImage(file=image_path)
    else:
        print(f"Warnung: Bild '{image_path}' nicht gefunden.")
        return None


app = GuiTest()
app.mainloop()
