import tkinter as tk
from tkinter import ttk, messagebox, PhotoImage
import os
import customtkinter as ctk
from customtkinter import *
import configuration  # Should be a class instead of a module if instantiated
import Mainpages
import Overview_pages
import ThemeManager
import Profiles
import importlib.util
import sys

sys.path.append(os.path.join(os.path.dirname(__file__),'..'))

from db.SQLite_db import *


'''
root_path = os.path.dirname(os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir)))
# login_DB
login_DB_path = root_path+"/gui/assets/+'db/login_DB.py'"

# Load and import module dynamically
spec = importlib.util.spec_from_file_location("login_DB", login_DB_path)
# login_DB = importlib.util.module_from_spec(spec)
# spec.loader.exec_module(login_DB)
'''
#########################
#      Mainwindow       #
#########################

class GuiTest(tk.Tk):
    """
    Eine Erweiterung der `tk.Tk`-Klasse, die als Hauptfenster für eine Tkinter-Anwendung dient.

    Diese Klasse bietet eine Grundlage für die grafische Benutzeroberfläche, erweitert um
    benutzerdefinierte Widgets und Funktionen.

    **Hauptmerkmale:**
    - Integriert Widgets und Ereignisbindungen für spezifische Anforderungen.
    - Strukturiert und erleichtert die Wiederverwendbarkeit und Anpassung des GUI-Codes.

    **Vorteile:**
    - Ermöglicht klare Trennung der GUI-Logik.
    - Flexibel erweiterbar für zukünftige Anforderungen.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes an application window with specific configurations and manages
        different application frames within this window.

        The constructor sets up the window properties such as title, size, and icon,
        and initializes a main container for managing frames. It dynamically
        loads and stores multiple frames, which represent different pages
        within the application. The application begins by displaying the
        `Mainpages.MainPage` frame.

        :param args: Additional unnamed arguments passed to the parent class
            constructor.
        :type args: tuple
        :param kwargs: Additional keyword arguments passed to the parent class
            constructor.
        :type kwargs: dict
        """
        super().__init__(*args, **kwargs)
        root_path = os.path.dirname(os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir)))

        #Fensterkonfigurationen
        self.title("Prototyp")
        self.resizable(False, False)
        self.geometry("1920x1080")
        self.iconbitmap(root_path + "/gui/assets/prototyp_download.ico")

        # Main container für Frames
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # Only attempt to instantiate Einstellungen if it's a class
        pages = [LogInWindow, Mainpages.MainPage, Mainpages.MainPageS2, Mainpages.Mainpage_empty,
                 Overview_pages.Ubersicht, Overview_pages.Gerateansicht,
                 Profiles.Profil, Profiles.Admin, Profiles.Stats]

        if hasattr(configuration, "Einstellungen"):
            pages.append(configuration.Einstellungen)

        for Page in pages: # Die Schleife iteriert über alle Seitenklassen, die in der Liste 'pages' enthalten sind.
            frame = Page(container, self) # Für jede Seite wird ein neues Frame-Objekt erstellt, das als Instanz dieser Klasse gilt.
            self.frames[Page] = frame # Das erstellte Frame wird dem 'frames'-Dictionary des Hauptfensters hinzugefügt, wobei die Seitenklasse als Schlüssel dient.
            frame.grid(row=0, column=0, sticky="nsew") # Jedes Frame wird in einem übergeordneten Container platziert und mit 'grid' positioniert,
                                                        # wobei es den gesamten verfügbaren Platz ('nsew') einnimmt.
        self.show_frame(LogInWindow)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

#########################
#      Loginwindow      #
#########################
class LogInWindow(tk.Frame):
    """
    Initialisiert ein Login-Fenster als Tkinter-Frame und konfiguriert dessen Layout und Ereignisse.

    **Args:**
    parent (tk.Widget): Das übergeordnete Widget, in das dieser Frame eingebettet wird.
    controller (object): Ein Steuerungsobjekt, das den Wechsel zwischen verschiedenen Anwendungsfenstern steuert.

    **Attributes:**

    - *parent* (tk.Widget): Referenz auf das übergeordnete Widget, zur Einbettung in die GUI.
    - *controller* (object): Referenz auf das Steuerungsobjekt zur Steuerung des Fensters.
    - *header* (ttk.Label): Beschriftungs-Widget für die Kopfzeile mit Anwendungsstil.
    - *bottom* (ttk.Label): Beschriftungs-Widget für die Fußzeile mit Anwendungsstil.
    - *login_frame* (tk.Frame): Enthält die Eingabefelder und den Login-Button für den Benutzer.
    - *username_entry* (ctk.CTkEntry): Eingabefeld für den Benutzernamen, angepasst für stilistische Konsistenz.
    - *password_entry* (ctk.CTkEntry): Eingabefeld für das Passwort, mit verstecktem Eingabetext für Sicherheit.

    **Methods:**
    login(): Überprüft die Anmeldedaten und zeigt das Hauptanwendungsfenster an, falls die Anmeldung erfolgreich ist.
    """
    def __init__(self, parent, controller):
        super().__init__(parent)
        from ThemeManager import ThemeManager
        self.configure(bg='white')

        #Style Konfigurationen
        header = ttk.Label(self, text="Login", anchor="center", style="Header.TLabel")
        bottom = ttk.Label(self, style="Footer.TLabel")

        style = ttk.Style()
        style.configure("Header.TLabel", foreground='white', background=ThemeManager.SRH_Orange,
                        font=("Inter", 50, 'bold'))
        style.configure("Footer.TLabel", background=ThemeManager.SRH_Grey)

        def login():
            """
            Überprüft Anmeldeinformationen und navigiert bei Erfolg zur Hauptseite.

            Diese Funktion validiert die Eingaben aus den Feldern `username_entry` und `password_entry`.
            Bei korrekter Eingabe wird die Hauptseite angezeigt, andernfalls erscheint eine Fehlermeldung.

            **Args:**

            Keine direkten Argumente. Nutzereingaben stammen aus `username_entry` und `password_entry`.

            **Attributes:**

            - username_entry (ctk.CTkEntry): Eingabe für den Benutzernamen.
            - password_entry (ctk.CTkEntry): Maskiertes Eingabefeld für das Passwort.
            - controller (object): Steuert den Wechsel zwischen Seiten.

            **Returns:**

            None: Führt Aktionen je nach Ergebnis der Validierung aus.

            **Seiteneffekte:**

            - Wechselt zur Hauptseite bei korrekter Anmeldung.
            - Zeigt Fehlermeldung und leert das Passwortfeld bei falscher Eingabe.
            """

            if login_lookup(username_entry.get(), password_entry.get()):
                controller.show_frame(Mainpages.MainPage)
                username_entry.delete(0, 'end')
                password_entry.delete(0, 'end')
            else:
                messagebox.showinfo(title="Fehler", message="Passwort oder Benutzername falsch")
                password_entry.delete(0, 'end')

        def on_enter(event=None):
            """Führt Login aus, wenn die Enter-Taste gedrückt wird."""
            login()

        # Login Frame Elements
        login_frame = tk.Frame(self, bg='white')
        username_label = tk.Label(login_frame, text="Benutzername", bg='white', font=("Inter", 19))
        username_entry = ctk.CTkEntry(login_frame, text_color='black', font=("Inter", 20), border_width=1, corner_radius=8,
                                       fg_color='white', width=200)
        password_label = tk.Label(login_frame, text="Passwort", bg='white', font=("Inter", 19))
        password_entry = ctk.CTkEntry(login_frame, text_color='black', font=("Inter", 20), border_width=1, corner_radius=8,
                     fg_color='white', width=200, show = "*") #Zeig Passwort mit ******
        login_button = ctk.CTkButton(login_frame, text="Login", fg_color='#081424', text_color='white', font=("Inter", 20, 'bold'), corner_radius=8,
                                     command=login, width=200, height=30, hover_color=ThemeManager.SRH_Orange)

###### Plazierung #######
        # Bindet die Enter-Taste an die Funktion "on_enter"
        self.bind("<Return>", on_enter)
        username_entry.bind("<Return>", on_enter)
        password_entry.bind("<Return>", on_enter)

        username_label.grid(row=0, column=0, pady=10)
        username_entry.grid(row=1, column=0, pady=10)
        password_label.grid(row=2, column=0, pady=10)
        password_entry.grid(row=3, column=0, pady=10)
        login_button.grid(row=4, column=0, pady=20)

        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)
        bottom.place(relx=0, rely=0.85, relwidth=1, relheight=0.13)
        login_frame.place(relx=0.5, rely=0.5, anchor="center")

# Funktion, wenn Bild nicht geladen werden kann
def load_image(image_path):
    if os.path.exists(image_path):
        return tk.PhotoImage(file=image_path)
    else:
        print(f"Warnung: Bild '{image_path}' nicht gefunden.")
        return None

try:
    app = GuiTest()
    app.mainloop()
except Exception as e:
    print(f"Fehler beim Starten des Programms: {e}")