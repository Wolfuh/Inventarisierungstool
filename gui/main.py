import time
import threading
import tkinter as tk
from tkinter import ttk, messagebox, PhotoImage, simpledialog, filedialog
import customtkinter as ctk
from customtkinter import *
from datetime import datetime
from ThemeManager import ThemeManager
import cache

current_group = ""

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from db.SQLite_db import *
import logging, loggerStyleAnsiEscSgr

loggerStyleAnsiEscSgr.logger

'''
root_path = os.path.dirname(os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir)))
# login_DB
login_DB_path = root_path+"/gui/assets/+'db/login_DB.py'"

# Load and import module dynamically
spec = importlib.util.spec_from_file_location("login_DB", login_DB_path)
# login_DB = importlib.util.module_from_spec(spec)
# spec.loader.exec_module(login_DB)
'''


# TreeLogger
class TreeLogFormatter(logging.Formatter):
    grey = "\33[38;20m"
    yellow = "\33[33;20m"
    red = "\33[31;20m"
    bold_red = "\33[31;1m"
    reset = "\33[0m"
    format = "%(name)s %(filename)s:%(lineno)d:\n%(message)s"

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


TreeLogger = logging.getLogger("Tree")
TreeLogger.setLevel(logging.INFO)  # <- auf "DEBUG" setzten, um die Log-Ausgaben des Trees einzublenden

TreeLoggerch = logging.StreamHandler()
TreeLoggerch.setFormatter(TreeLogFormatter())

TreeLogger.addHandler(TreeLoggerch)
TreeLogger.propagate = False


###################################
# ୧‿̩͙ ˖︵ ꕀ⠀ ♱ Main ♱⠀ ꕀ ︵˖ ‿̩͙୨#R
###################################

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

        # Fensterkonfigurationen
        self.title("Prototyp")
        self.resizable(True, True)
        self.geometry("1920x1080")
        self.iconbitmap(root_path + "/gui/assets/prototyp_download.ico")

        # Main container für Frames
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # Only attempt to instantiate Einstellungen if it's a class
        pages = [LogInWindow, MainPage, MainPageS2, Mainpage_empty,
                 Ubersicht, Gerateansicht, Einstellungen,
                 Profil, Admin, Stats, Help]

        if hasattr(Einstellungen, "Einstellungen"):
            pages.append(Einstellungen)

        for Page in pages:  # Die Schleife iteriert über alle Seitenklassen, die in der Liste 'pages' enthalten sind.
            frame = Page(container,
                         self)  # Für jede Seite wird ein neues Frame-Objekt erstellt, das als Instanz dieser Klasse gilt.
            self.frames[
                Page] = frame  # Das erstellte Frame wird dem 'frames'-Dictionary des Hauptfensters hinzugefügt, wobei die Seitenklasse als Schlüssel dient.
            frame.grid(row=0, column=0,
                       sticky="nsew")  # Jedes Frame wird in einem übergeordneten Container platziert und mit 'grid' positioniert,
            # wobei es den gesamten verfügbaren Platz ('nsew') einnimmt.
        self.show_frame(LogInWindow)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


####################################
# ୧‿̩͙ ˖︵ ꕀ⠀ ♱ LogIn ♱⠀ ꕀ ︵˖ ‿̩͙୨#
####################################
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

        self.configure(bg='white')

        # Style Konfigurationen
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
                controller.show_frame(MainPage)
                username_entry.delete(0, 'end')
                password_entry.delete(0, 'end')
                logging.info(f"'{username_global}' hat sich erfolgreich angemeldet.")
            else:
                messagebox.showinfo(title="Fehler", message="Passwort oder Benutzername falsch")
                password_entry.delete(0, 'end')

        def on_enter(event=None):
            """Führt Login aus, wenn die Enter-Taste gedrückt wird."""
            login()

        # Login Frame Elements
        login_frame = tk.Frame(self, bg='white')
        username_label = tk.Label(login_frame, text="Benutzername", bg='white', font=("Inter", 19))
        username_entry = ctk.CTkEntry(login_frame, text_color='black', font=("Inter", 20), border_width=1,
                                      corner_radius=8,
                                      fg_color='white', width=200)
        password_label = tk.Label(login_frame, text="Passwort", bg='white', font=("Inter", 19))
        password_entry = ctk.CTkEntry(login_frame, text_color='black', font=("Inter", 20), border_width=1,
                                      corner_radius=8,
                                      fg_color='white', width=200, show="*")  # Zeig Passwort mit ******
        login_button = ctk.CTkButton(login_frame, text="Login", fg_color='#081424', text_color='white',
                                     font=("Inter", 20, 'bold'), corner_radius=8,
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


#######################################
# ୧‿̩͙ ˖︵ ꕀ⠀ ♱ Mainpage ♱⠀ ꕀ ︵˖ ‿̩͙୨#
#######################################

class MainPage(tk.Frame):
    """
    Repräsentiert die Hauptseite einer grafischen Benutzeroberfläche (GUI) mit Kopf- und Fußbereich,
    Hauptanzeigebereich und verschiedenen Bedienelementen. Diese Seite ermöglicht die Navigation
    zwischen anderen Rahmen der Anwendung, einschließlich Login, Profil und spezifischer Gruppenseiten.

    Die Klasse ist erweiterbar als Frame-Komponente innerhalb eines größeren Fenstercontainers.

    :ivar main_frame: Der Hauptanzeigebereich der Startseite mit weißem Hintergrund.
    :type main_frame: tk.Frame
    :ivar imglogin: Bild für den Login-Button.
    :type imglogin: PhotoImage
    :ivar imgprofil: Bild für den Profil-Button.
    :type imgprofil: PhotoImage
    :ivar imghelp: Bild für den Hilfe-Button.
    :type imghelp: PhotoImage
    :ivar imgbildgr1: Bild für den Button der Gruppe 1.
    :type imgbildgr1: PhotoImage
    :ivar imgbildgr2: Bild für den Button der Gruppe 2.
    :type imgbildgr2: PhotoImage
    :ivar imgbildgr3: Bild für den Button der Gruppe 3.
    :type imgbildgr3: PhotoImage
    :ivar imgbildgr4: Bild für den Button der Gruppe 4.
    :type imgbildgr4: PhotoImage
    :ivar imgbildgr5: Bild für den Button der Gruppe 5.
    :type imgbildgr5: PhotoImage
    :ivar imgbildgr6: Bild für den Button der Gruppe 6.
    :type imgbildgr6: PhotoImage
    :ivar imgbildgr7: Bild für den Button der Gruppe 7.
    :type imgbildgr7: PhotoImage
    :ivar imgbildgr8: Bild für den Button der Gruppe 8.
    :type imgbildgr8: PhotoImage
    :ivar imgseitevor: Bild für den Button zur nächsten Seite.
    :type imgseitevor: PhotoImage
    """

    def __init__(self, parent, controller):
        root_path = os.path.dirname(os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir)))
        tk.Frame.__init__(self, parent)

        self.configure(bg='white')

        # Konfiguration des Kopf- und Fußbereich
        header = ttk.Label(self, text="Startseite", anchor="center", style="Header.TLabel")
        bottom = ttk.Label(self, style="Footer.TLabel")
        self.main_frame = tk.Frame(self, bg='white')
        self.main_frame.place(relx=0.21, rely=0.15, relwidth=1, relheight=0.65)

        # Layout Festlegung der flexiblen Skalierung der Mainpage
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)

        # laden der Bilder für die Buttons und der Gruppen
        self.imglogin = load_image(root_path + "/gui/assets/Closeicon.png")
        self.imgprofil = load_image(root_path + "/gui/assets/profileicon.png")
        self.imghelp = tk.PhotoImage(file=root_path + "/gui/assets/helpicon.png")

        self.imgseitevor = tk.PhotoImage(file=root_path + "/gui/assets/pageforward_icon.png")

        # Platzierung der Buttons
        login = ctk.CTkButton(header, image=self.imglogin, fg_color=ThemeManager.SRH_Orange,
                              bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                              hover=True, hover_color='#e25a1f', text="",
                              command=lambda: controller.show_frame(LogInWindow))
        profil = ctk.CTkButton(header, image=self.imgprofil, fg_color=ThemeManager.SRH_Orange,
                               bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                               hover=True, hover_color='#e25a1f', text="",
                               command=lambda: controller.show_frame(Profil))
        help = ctk.CTkButton(header, image=self.imghelp, fg_color=ThemeManager.SRH_Orange,
                             bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                             hover=True, hover_color='#e25a1f', text="",
                             command=lambda: controller.show_frame(Help))

        all = ctk.CTkButton(self, text="Alle Anzeigen", fg_color='white', text_color=ThemeManager.SRH_Blau,
                            font=("Inter", 20), corner_radius=8, hover=False,
                            command=lambda: controller.show_frame(Ubersicht))

        # global current_group
        # current_group = group

        def handle_group_click(controller, group):
            global current_group
            current_group = group
            obj1 = Ubersicht(parent, controller)
            logging.info(f"Gruppe {group} wurde geklickt!")

            controller.show_frame(Ubersicht)

        i = 1
        place = 0
        self.images = []  # Liste, um Bildreferenzen zu speichern

        while i < 9:
            # Bild für den Button laden
            img = tk.PhotoImage(file=root_path + f"/gui/assets/Gruppe{i}.png")
            self.images.append(img)  # Bildreferenz speichern, damit es nicht gelöscht wird

            # Button erstellen
            bildgr = tk.Button(self, image=img, bd=0, bg='white',
                               command=lambda group=i: handle_group_click(controller, group))

            # Position bestimmen
            if i > 4:
                hight = 0.55
                if i == 5:
                    place = 0  # Zurücksetzen der horizontalen Position
            else:
                hight = 0.25

            place = place + 0.2
            bildgr.place(relx=place, rely=hight, anchor='n')

            i += 1

        seitevor = ctk.CTkButton(self, image=self.imgseitevor, text="", fg_color='white', text_color='black',
                                 font=("Inter", 20, 'bold'),
                                 corner_radius=8, hover=False,
                                 command=lambda: controller.show_frame(MainPageS2), width=200, height=30,
                                 hover_color=ThemeManager.SRH_Orange)

        # Festlegung des Styles für Header- und Footer Labels, Positionierung der Navigationsbuttons im Header, die
        # Anordnung der Bildgruppen-Buttons in einem Rasterlayout, sowie Platzierungen.
        style = ttk.Style()
        style.configure("Header.TLabel", foreground='white', background='#DF4807', font=("Inter", 55, 'bold'))
        style.configure("Footer.TLabel", background=ThemeManager.SRH_Grey)

        ###### Plazierung #######
        login.place(relx=0.95, rely=0.5, anchor="center")
        profil.place(relx=0.90, rely=0.5, anchor="center")
        help.place(relx=0.85, rely=0.5, anchor="center")

        all.place(relx=0.01, rely=0.18, anchor='w')
        seitevor.place(relx=0.51, rely=0.80, anchor='n')
        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)
        bottom.place(relx=0, rely=0.85, relwidth=1, relheight=0.13)

    def get_current_group(self):  # gibt die aktuelle Gruppe zurück
        logging.debug(
            f"{loggerStyleAnsiEscSgr.foregroundColor.brightyellow}get_current_group{loggerStyleAnsiEscSgr.foregroundColor.yellow}(){loggerStyleAnsiEscSgr.foregroundColor.reset} returned '{current_group}' (type: '{type(current_group)}')")
        return current_group


##########################################
# ୧‿̩͙ ˖︵ ꕀ⠀ ♱ Mainpage S2 ♱⠀ ꕀ ︵˖ ‿̩͙୨#
##########################################

class MainPageS2(tk.Frame):
    """
    Zusammenfassung, was die Klasse macht.

    Diese Klasse stellt eine grafische Oberfläche für die Startseite eines GUI-Frameworks bereit. Sie erbt von `tk.Frame` und
    wird verwendet, um verschiedene Elemente wie Header, Footer, Hauptbereich sowie Navigations- und Inhaltsbuttons
    anzuzeigen. Die Klasse unterstützt Layout-Anpassungen, das Laden von Bildressourcen und die Navigation zwischen
    verschiedenen Seiten.

    :ivar main2_frame: Das zentrale Hauptanzeigefenster, das den Hauptinhalt der Seite aufnimmt.
    :type main2_frame: tk.Frame
    :ivar imglogin: Bildressource für den Login-Button.
    :type imglogin: tk.PhotoImage
    :ivar imgprofil: Bildressource für den Profil-Button.
    :type imgprofil: tk.PhotoImage
    :ivar imghelp: Bildressource für den Hilfe-Button.
    :type imghelp: tk.PhotoImage
    :ivar imgbildgr1: Bildressource für die erste Bildergruppe.
    :type imgbildgr1: tk.PhotoImage
    :ivar imgbildgr2: Bildressource für die zweite Bildergruppe.
    :type imgbildgr2: tk.PhotoImage
    :ivar imgbildgr3: Bildressource für die dritte Bildergruppe.
    :type imgbildgr3: tk.PhotoImage
    :ivar imgbildgr4: Bildressource für die vierte Bildergruppe.
    :type imgbildgr4: tk.PhotoImage
    :ivar imgbildgr5: Bildressource für die fünfte Bildergruppe.
    :type imgbildgr5: tk.PhotoImage
    :ivar imgbildgr6: Bildressource für die sechste Bildergruppe.
    :type imgbildgr6: tk.PhotoImage
    :ivar imgbildgr7: Bildressource für die siebte Bildergruppe.
    :type imgbildgr7: tk.PhotoImage
    :ivar imgseitevor: Bildressource für den Vorwärts-Navigationsbutton.
    :type imgseitevor: tk.PhotoImage
    :ivar imgseiteback: Bildressource für den Rückwärts-Navigationsbutton.
    :type imgseiteback: tk.PhotoImage
    """

    def __init__(self, parent, controller):
        root_path = os.path.dirname(os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir)))
        tk.Frame.__init__(self, parent)

        self.configure(bg='white')

        # Erstellung vom header und Footer und Konfiguration des Hauptanzeigenbereiches
        header = ttk.Label(self, text="Startseite", anchor="center", style="Header.TLabel")
        bottom = ttk.Label(self, style="Footer.TLabel")
        self.main2_frame = tk.Frame(self, bg='white')
        self.main2_frame.place(relx=0.21, rely=0.15, relwidth=1, relheight=0.65)

        # Layout Festlegung der flexiblen Skalierung der Mainpage2
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)

        # laden der Bilder für Buttons und Gruppen, Buttons für die Navigation (Login, Profil und Bildgruppen)
        self.imglogin = load_image(root_path + "/gui/assets/Closeicon.png")
        self.imgprofil = load_image(root_path + "/gui/assets/profileicon.png")
        self.imghelp = tk.PhotoImage(file=root_path + "/gui/assets/helpicon.png")
        self.imgbildgr1 = tk.PhotoImage(file=root_path + "/gui/assets/Gruppe1.png")
        self.imgbildgr2 = tk.PhotoImage(file=root_path + "/gui/assets/Gruppe2.png")
        self.imgbildgr3 = tk.PhotoImage(file=root_path + "/gui/assets/Gruppe3.png")
        self.imgbildgr4 = tk.PhotoImage(file=root_path + "/gui/assets/Gruppe4.png")
        self.imgbildgr5 = tk.PhotoImage(file=root_path + "/gui/assets/Gruppe5.png")
        self.imgbildgr6 = tk.PhotoImage(file=root_path + "/gui/assets/Gruppe6.png")
        self.imgbildgr7 = tk.PhotoImage(file=root_path + "/gui/assets/Gruppe7.png")
        # self.imgbildgr8 = tk.PhotoImage(file=root_path+"/gui/assets/Gruppe8.png")
        self.imgseitevor = tk.PhotoImage(file=root_path + "/gui/assets/pageforward_icon.png")
        self.imgseiteback = tk.PhotoImage(file=root_path + "/gui/assets/pageback_icon.png")
        login = ctk.CTkButton(header, image=self.imglogin, fg_color=ThemeManager.SRH_Orange,
                              bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                              hover=True, hover_color='#e25a1f', text="",
                              command=lambda: controller.show_frame(LogInWindow))

        profil = ctk.CTkButton(header, image=self.imgprofil, fg_color=ThemeManager.SRH_Orange,
                               bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                               hover=True, hover_color='#e25a1f', text="",
                               command=lambda: controller.show_frame(Profil))
        help = ctk.CTkButton(header, image=self.imghelp, fg_color=ThemeManager.SRH_Orange,
                             bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                             hover=True, hover_color='#e25a1f', text="",
                             command=lambda: controller.show_frame(Help))

        # Buttons zum Wechseln zwischen den Hauptseiten und "Alle anzeigen" Button für die Übersichtsseite
        all = ctk.CTkButton(self, text="Alle Anzeigen", fg_color='white', text_color=ThemeManager.SRH_Blau,
                            font=("Inter", 20), corner_radius=8, hover=False,
                            command=lambda: controller.show_frame(Ubersicht))

        bildgr1 = tk.Button(self, image=self.imgbildgr1, bd=0, bg='white',
                            command=lambda: controller.show_frame(Ubersicht))
        bildgr2 = tk.Button(self, image=self.imgbildgr2, bd=0, bg='white',
                            command=lambda: controller.show_frame(Ubersicht))
        bildgr3 = tk.Button(self, image=self.imgbildgr3, bd=0, bg='white',
                            command=lambda: controller.show_frame(Ubersicht))
        bildgr4 = tk.Button(self, image=self.imgbildgr4, bd=0, bg='white',
                            command=lambda: controller.show_frame(Ubersicht))
        bildgr5 = tk.Button(self, image=self.imgbildgr5, bd=0, bg='white',
                            command=lambda: controller.show_frame(Ubersicht))
        bildgr6 = tk.Button(self, image=self.imgbildgr6, bd=0, bg='white',
                            command=lambda: controller.show_frame(Ubersicht))
        bildgr7 = tk.Button(self, image=self.imgbildgr7, bd=0, bg='white',
                            command=lambda: controller.show_frame(Ubersicht))
        # bildgr8 = tk.Button(self, image=self.imgbildgr8, bd=0, bg='white',
        # command=lambda: controller.show_frame(Ubersicht))

        seitevor = ctk.CTkButton(self, image=self.imgseitevor, text="", fg_color='white', text_color='black',
                                 font=("Inter", 20, 'bold'),
                                 corner_radius=8, hover=False,
                                 command=lambda: controller.show_frame(Mainpage_empty), width=10, height=30,
                                 hover_color=ThemeManager.SRH_Orange)
        seiteback = ctk.CTkButton(self, image=self.imgseiteback, text="", fg_color='white', text_color='black',
                                  font=("Inter", 20, 'bold'),
                                  corner_radius=8, hover=False,
                                  command=lambda: controller.show_frame(MainPage), width=10, height=30,
                                  hover_color=ThemeManager.SRH_Orange)

        # Style Konfiguration für Header und Footer, Platzierung der Buttons, Header und Footer
        style = ttk.Style()
        style.configure("Header.TLabel", foreground='white', background=ThemeManager.SRH_Orange,
                        font=("Inter", 55, 'bold'))
        style.configure("Footer.TLabel", background=ThemeManager.SRH_Grey)

        ###### Plazierung #######
        login.place(relx=0.95, rely=0.5, anchor="center")
        profil.place(relx=0.90, rely=0.5, anchor="center")
        help.place(relx=0.85, rely=0.5, anchor="center")

        bildgr1.place(relx=0.20, rely=0.25, anchor='n')
        bildgr2.place(relx=0.40, rely=0.25, anchor='n')
        bildgr3.place(relx=0.60, rely=0.25, anchor='n')
        bildgr4.place(relx=0.80, rely=0.25, anchor='n')

        bildgr5.place(relx=0.20, rely=0.55, anchor='n')
        bildgr6.place(relx=0.40, rely=0.55, anchor='n')
        bildgr7.place(relx=0.60, rely=0.55, anchor='n')

        all.place(relx=0.01, rely=0.18, anchor='w')
        seitevor.place(relx=0.51, rely=0.80, anchor='n')
        seiteback.place(relx=0.49, rely=0.80, anchor='n')
        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)
        bottom.place(relx=0, rely=0.85, relwidth=1, relheight=0.13)


#############################################
# ୧‿̩͙ ˖︵ ꕀ⠀ ♱ Mainpage empty ♱⠀ ꕀ ︵˖ ‿̩͙୨#
#############################################

class Mainpage_empty(tk.Frame):

    def __init__(self, parent, controller):
        root_path = os.path.dirname(os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir)))
        tk.Frame.__init__(self, parent)

        self.configure(bg='white')

        # Erstellung vom header und Footer und Konfiguration des Hauptanzeigenbereiches
        # self.main_empty_frame = tk.Frame(self, bg='black')
        header = ttk.Label(self, text="Startseite", anchor="center", style="Header.TLabel")
        bottom = ttk.Label(self, style="Footer.TLabel")

        # Layout Festlegung der flexiblen Skalierung der Mainpage2
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)

        # laden der Bilder für Buttons und Gruppen, Buttons für die Navigation (Login, Profil und Bildgruppen)
        self.imglogin = load_image(root_path + "/gui/assets/Closeicon.png")
        self.imgprofil = load_image(root_path + "/gui/assets/profileicon.png")
        self.imghelp = tk.PhotoImage(file=root_path + "/gui/assets/helpicon.png")
        # self.imgbildgr1 = tk.PhotoImage(file=root_path+"/gui/assets/Gruppe_1.png")
        # self.imgbildgr2 = tk.PhotoImage(file=root_path+"/gui/assets/Gruppe2.png")
        # self.imgbildgr3 = tk.PhotoImage(file=root_path+"/gui/assets/Gruppe3.png")
        # self.imgbildgr4 = tk.PhotoImage(file=root_path+"/gui/assets/Gruppe4.png")
        # self.imgbildgr5 = tk.PhotoImage(file=root_path+"/gui/assets/Gruppe5.png")
        # self.imgbildgr6 = tk.PhotoImage(file=root_path+"/gui/assets/Gruppe6.png")
        # self.imgbildgr7 = tk.PhotoImage(file=root_path+"/gui/assets/Gruppe7.png")
        # #self.imgbildgr8 = tk.PhotoImage(file=root_path+"/gui/assets/Gruppe8.png")
        self.imgseitevor = tk.PhotoImage(file=root_path + "/gui/assets/pageforward_icon.png")
        self.imgseiteback = tk.PhotoImage(file=root_path + "/gui/assets/pageback_icon.png")

        login = ctk.CTkButton(header, image=self.imglogin, fg_color=ThemeManager.SRH_Orange,
                              bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                              hover=True, hover_color='#e25a1f', text="",
                              command=lambda: controller.show_frame(LogInWindow))

        profil = ctk.CTkButton(header, image=self.imgprofil, fg_color=ThemeManager.SRH_Orange,
                               bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                               hover=True, hover_color='#e25a1f', text="",
                               command=lambda: controller.show_frame(Profil))
        help = ctk.CTkButton(header, image=self.imghelp, fg_color=ThemeManager.SRH_Orange,
                             bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                             hover=True, hover_color='#e25a1f', text="",
                             command=lambda: controller.show_frame(Help))

        # Buttons zum Wechseln zwischen den Hauptseiten und "Alle anzeigen" Button für die Übersichtsseite
        all = ctk.CTkButton(self, text="Alle Anzeigen", fg_color='white', text_color=ThemeManager.SRH_Blau,
                            font=("Inter", 20), corner_radius=8, hover=False,
                            command=lambda: controller.show_frame(Ubersicht))

        seitevor = ctk.CTkButton(self, image=self.imgseitevor, text="", fg_color='white', text_color='black',
                                 font=("Inter", 20, 'bold'),
                                 corner_radius=8, hover=False,
                                 command=lambda: controller.show_frame(MainPageS2), width=10, height=30,
                                 hover_color=ThemeManager.SRH_Orange)
        seiteback = ctk.CTkButton(self, image=self.imgseiteback, text="", fg_color='white', text_color='black',
                                  font=("Inter", 20, 'bold'),
                                  corner_radius=8, hover=False,
                                  command=lambda: controller.show_frame(MainPageS2), width=10, height=30,
                                  hover_color=ThemeManager.SRH_Orange)

        # Style Konfiguration für Header und Footer, Platzierung der Buttons, Header und Footer
        style = ttk.Style()
        style.configure("Header.TLabel", foreground='white', background=ThemeManager.SRH_Orange,
                        font=("Inter", 55, 'bold'))
        style.configure("Footer.TLabel", background=ThemeManager.SRH_Grey)

        ###### Plazierung #######
        # self.main_empty_frame.place(relx=0, rely=0.15, relwidth=1, relheight=0.7)
        login.place(relx=0.95, rely=0.5, anchor="center")
        profil.place(relx=0.90, rely=0.5, anchor="center")
        help.place(relx=0.85, rely=0.5, anchor="center")

        # Frames für die Gruppen
        frame_for_group = tk.Frame(self, bg='#FBFBFB')

        x_pos = 0.2;
        y_pos = 0.25
        for _ in range(8):
            frame_for_group.place(relx=x_pos, rely=y_pos, width=244, height=244, anchor='n')
            x_pos += 0.2
            if x_pos == 0.8:
                x_pos = 0.2;
                y_pos = 0.55

        all.place(relx=0.01, rely=0.18, anchor='w')
        seitevor.place(relx=0.51, rely=0.80, anchor='n')
        seiteback.place(relx=0.49, rely=0.80, anchor='n')
        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)
        bottom.place(relx=0, rely=0.85, relwidth=1, relheight=0.13)


##############################################
# ୧‿̩͙ ˖︵ ꕀ⠀ ♱ Geräteübersicht ♱⠀ ꕀ ︵˖ ‿̩͙୨#
##############################################

class Ubersicht(tk.Frame):
    """
    Zusammenfassung der Funktionalität und des Zwecks der Klasse.

    Die Klasse `Ubersicht` stellt ein GUI für die Geräteübersicht bereit. Sie bietet mehrere
    Frames und Komponenten, um verschiedene Funktionen anzuzeigen und darzustellen. Die Klasse
    verwendet unterschiedliche Layout-Elemente, Widgets und Stilkonfigurationen, um eine
    benutzerfreundliche Navigation und Darstellung von Geräten und Gruppeninformationen zu gewährleisten.

    :ivar imglogin: Bildreferenz für das Login-Symbol.
    :ivar imgprofil: Bildreferenz für das Profil-Symbol.
    :ivar imghelp: Bildreferenz für das Hilfe-Symbol.
    :ivar imgmainpage: Bildreferenz für das Icon zur Hauptseite.
    :ivar ubersicht_frame: Frame für die Hauptanzeige der Übersichtsseite.
    :ivar tabelle_frame: Frame, der die Tabelle für Datendarstellung enthält.
    :ivar mainpage_frame: Frame für die Navigationsbutton, um zur Hauptseite zurückzukehren.
    :ivar tree: Baumstruktur für die tabellarische Darstellung von Daten.
    """

    def __init__(self, parent, controller):
        root_path = os.path.dirname(os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir)))
        tk.Frame.__init__(self, parent)

        self.configure(bg='white')

        # Stilkonfiguration für Header und Footer, Erstellung vom Header und des Überschriftbereiches.
        style = ttk.Style()
        style.configure("Header.TLabel", foreground='white',
                        background=ThemeManager.SRH_Orange, font=("Inter", 55, 'bold'))
        style.configure("Footer.TLabel", background=ThemeManager.SRH_Grey)
        header = ttk.Label(self, text="Geräteübersicht", anchor="center", style="Header.TLabel")
        verzeichniss = tk.Frame(self, bg=ThemeManager.SRH_Grey)
        self.ubersicht_frame = tk.Frame(self, bg='white')
        self.tabelle_frame = tk.Frame(self, bg='white')
        self.mainpage_frame = tk.Frame(self, bg='white')
        self.mainpage_frame.place(relx=0.15, rely=0.15, relwidth=0.06, relheight=0.15)
        self.ubersicht_frame.place(relx=0.21, rely=0.15, relwidth=1, relheight=0.85)

        # Layout Festlegung der flexiblen Skalierung der Übersichtsseite
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)

        # Laden der Bilder für die Navigation und Header Buttons
        self.imglogin = load_image(root_path + "/gui/assets/Closeicon.png")
        self.imgprofil = load_image(root_path + "/gui/assets/profileicon.png")
        self.imghelp = tk.PhotoImage(file=root_path + "/gui/assets/helpicon.png")
        self.imgmainpage = tk.PhotoImage(file=root_path + "/gui/assets/backtosite_icon_grey.png")

        # Login und Profil Buttons im Header-Bereich, Platzierung der Buttons, Header und Sidebar
        login = ctk.CTkButton(header, image=self.imglogin, fg_color=ThemeManager.SRH_Orange,
                              bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                              hover=True, hover_color='#e25a1f', text="",
                              command=lambda: controller.show_frame(LogInWindow))

        profil = ctk.CTkButton(header, image=self.imgprofil, fg_color=ThemeManager.SRH_Orange,
                               bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                               hover=True, hover_color='#e25a1f', text="",
                               command=lambda: controller.show_frame(Profil))
        help = ctk.CTkButton(header, image=self.imghelp, fg_color=ThemeManager.SRH_Orange,
                             bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                             hover=True, hover_color='#e25a1f', text="",
                             command=lambda: controller.show_frame(Help))

        login.place(relx=0.95, rely=0.5, anchor="center")
        profil.place(relx=0.90, rely=0.5, anchor="center")
        help.place(relx=0.85, rely=0.5, anchor="center")

        mainpage = ctk.CTkButton(self.mainpage_frame, text="↩", fg_color='white', text_color=ThemeManager.SRH_Grey,
                                 width=5,
                                 font=("Inter", 50, 'bold'), corner_radius=8, hover=False,
                                 command=lambda: controller.show_frame(MainPage))
        mainpage.place(relx=0, rely=0)

        # "Alle Anzeigen" Button in der Seitenleiste
        all_button = ctk.CTkButton(verzeichniss, text="Alle Anzeigen", fg_color=ThemeManager.SRH_Grey,
                                   text_color='black',
                                   font=("Inter", 20), corner_radius=8, hover=False,
                                   command=lambda: starting_table())  # controller.show_frame(Ubersicht))

        all_button.pack(pady=10, anchor='w')

        overview_table_tree = ttk.Treeview(self.tabelle_frame, columns=("c1", "c2", "c3", "c4", "c5"), show="headings",
                                           height=5)
        overview_table_tree.place(x=120, y=0, width=1280, height=650)
        TreeLogger.debug(f"'{overview_table_tree.get_children()}' - wurde gerade definiert")

        print(type(overview_table_tree))
        print(overview_table_tree)

        def show_right_table(item_position: int, suchgruppe, search_word):
            # item_position benötigt Zahl, für den gesuchten Ort
            # Spaltennamen aus der Datenbank holen
            logging.debug(f"{loggerStyleAnsiEscSgr.foregroundColor.brightyellow}show_right_table{loggerStyleAnsiEscSgr.foregroundColor.yellow}({loggerStyleAnsiEscSgr.foregroundColor.reset}item_position='{item_position}' (type: '{type(item_position)}'), suchgruppe='{suchgruppe}' (type: '{type(suchgruppe)}'), search_word='{search_word}' (type: '{type(search_word)}'){loggerStyleAnsiEscSgr.foregroundColor.yellow}){loggerStyleAnsiEscSgr.foregroundColor.reset}")

            items_uberschrift = fetch_headers("items", ["image"])

            # Überschriften konfigurieren

            overview_table_tree["columns"] = items_uberschrift
            for up in items_uberschrift:
                overview_table_tree.column(up, anchor=CENTER, width=100)
                overview_table_tree.heading(up, text=up)
            TreeLogger.debug(f"'{overview_table_tree.get_children()}'")

            items_data = fetch_tables("items", ["image"])
            overview_table_tree.delete(*overview_table_tree.get_children())
            TreeLogger.debug(f"'{overview_table_tree.get_children()}'")

            type_sort = ["Hardwawre", "Software", "Peripherie"]

            # Daten aus DB einfügen
            i = 0
            for item in items_data:
                if (item[2] and str(item[2]) == suchgruppe) and search_word == "ANDERE" and not str(
                        item[item_position]) in type_sort:
                    formatted_row = [value if value is not None else "-" for value in
                                     item]  # Leere Felder durch "-" ersetzen
                    overview_table_tree.insert("", "end", values=formatted_row, tags=("even" if i % 2 == 0 else "odd"))
                    TreeLogger.debug(f"'{overview_table_tree.get_children()}'")
                    i += 1

                elif (item[2] and str(item[2]) == suchgruppe) and (
                        not search_word or str(item[item_position]) == search_word):
                    formatted_row = [value if value is not None else "-" for value in
                                     item]  # Leere Felder durch "-" ersetzen
                    overview_table_tree.insert("", "end", values=formatted_row, tags=("even" if i % 2 == 0 else "odd"))
                    TreeLogger.debug(f"'{overview_table_tree.get_children()}'")
                    i += 1
            TreeLogger.debug(f"'{overview_table_tree.get_children()}'")
            logging.debug(
                f"{loggerStyleAnsiEscSgr.foregroundColor.brightyellow}show_right_table{loggerStyleAnsiEscSgr.foregroundColor.yellow}(){loggerStyleAnsiEscSgr.foregroundColor.reset} wurde ausgeführt")

        # current_group = Mainpages.MainPage.get_current_group()

        def show_the_active_group():
            current_group = MainPage.get_current_group(self)
            if current_group:
                show_right_table(8, "3", "")
                logging.debug(
                    f"{loggerStyleAnsiEscSgr.foregroundColor.brightyellow}show_the_active_group{loggerStyleAnsiEscSgr.foregroundColor.yellow}(){loggerStyleAnsiEscSgr.foregroundColor.reset} mit Wert '{current_group}' (type: '{type(current_group)}') für current_group aufgerufen")
            else:
                starting_table()
                logging.debug(
                    f"{loggerStyleAnsiEscSgr.foregroundColor.brightyellow}show_the_active_group{loggerStyleAnsiEscSgr.foregroundColor.yellow}(){loggerStyleAnsiEscSgr.foregroundColor.reset} ohne Wert für current_group aufgerufen, \
starte {loggerStyleAnsiEscSgr.foregroundColor.brightyellow}starting_table{loggerStyleAnsiEscSgr.foregroundColor.yellow}(){loggerStyleAnsiEscSgr.foregroundColor.reset}!")

        # Gruppe 1
        def show_dropdown_grp1():
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg=ThemeManager.SRH_Grey, fg='black')
            dropdown_menu.add_command(label="→ Alles Anzeigen", command=lambda: show_right_table(2, "1",
                                                                                                 ""))  # Alle Objekte mit der Gruppe x werden angezeigt
            dropdown_menu.add_command(label="→ Hardware", command=lambda: show_right_table(8, "1",
                                                                                           "Hardwawre"))  # nur Hardware Objekte mit der Gruppe x werden angezeigt
            dropdown_menu.add_command(label="→ Software", command=lambda: show_right_table(8, "1",
                                                                                           "Software"))  # nur Software Produkte mit der Gruppe x werden angezeigt
            dropdown_menu.add_command(label="→ Peripherie", command=lambda: show_right_table(8, "1",

                                                                                             "Peripherie"))  # nur Peripherie mit der Gruppe x werden angezeigt
            dropdown_menu.add_command(label="→ Andere", command=lambda: show_right_table(8, "1",
                                                                                         "ANDERE"))  # Andere Objekte mit der Gruppe x werden angezeigt (z.B.: Bücher)
            dropdown_menu.add_command(label="TEST", command=lambda: show_the_active_group())
            dropdown_menu.post(grp1_button.winfo_rootx(), grp1_button.winfo_rooty() + grp1_button.winfo_height())

        grp1_button = tk.Button(verzeichniss, text="Gruppe 1   ", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=show_dropdown_grp1)
        grp1_button.pack(pady=10, anchor='w')

        # Gruppe 2
        def show_dropdown_grp2():
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg=ThemeManager.SRH_Grey, fg='black')
            dropdown_menu.add_command(label="→ Alles Anzeigen", command=lambda: show_right_table(2, "2",
                                                                                                 ""))  # Alle Objekte mit der Gruppe x werden angezeigt
            dropdown_menu.add_command(label="→ Hardware", command=lambda: show_right_table(8, "2",
                                                                                           "Hardwawre"))  # nur Hardware Objekte mit der Gruppe x werden angezeigt
            dropdown_menu.add_command(label="→ Software", command=lambda: show_right_table(8, "2",
                                                                                           "Software"))  # nur Software Produkte mit der Gruppe x werden angezeigt
            dropdown_menu.add_command(label="→ Peripherie", command=lambda: show_right_table(8, "2",
                                                                                             "Peripherie"))  # nur Peripherie mit der Gruppe x werden angezeigt
            dropdown_menu.add_command(label="→ Andere", command=lambda: show_right_table(8, "2",
                                                                                         "ANDERE"))  # Andere Objekte mit der Gruppe x werden angezeigt (z.B.: Bücher)
            dropdown_menu.post(grp2_button.winfo_rootx(), grp2_button.winfo_rooty() + grp2_button.winfo_height())

        grp2_button = tk.Button(verzeichniss, text="Gruppe 2   ", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=show_dropdown_grp2)
        grp2_button.pack(pady=10, anchor='w')

        # Gruppe 3
        def show_dropdown_grp3():
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg=ThemeManager.SRH_Grey, fg='black')
            dropdown_menu.add_command(label="→ Alles Anzeigen", command=lambda: show_right_table(2, "3",
                                                                                                 ""))  # Alle Objekte mit der Gruppe x werden angezeigt
            dropdown_menu.add_command(label="→ Hardware", command=lambda: show_right_table(8, "3",
                                                                                           "Hardwawre"))  # nur Hardware Objekte mit der Gruppe x werden angezeigt
            dropdown_menu.add_command(label="→ Software", command=lambda: show_right_table(8, "3",
                                                                                           "Software"))  # nur Software Produkte mit der Gruppe x werden angezeigt
            dropdown_menu.add_command(label="→ Peripherie", command=lambda: show_right_table(8, "3",
                                                                                             "Peripherie"))  # nur Peripherie mit der Gruppe x werden angezeigt
            dropdown_menu.add_command(label="→ Andere", command=lambda: show_right_table(8, "3",
                                                                                         "ANDERE"))  # Andere Objekte mit der Gruppe x werden angezeigt (z.B.: Bücher)
            dropdown_menu.post(grp3_button.winfo_rootx(), grp3_button.winfo_rooty() + grp3_button.winfo_height())

        grp3_button = tk.Button(verzeichniss, text="Gruppe 3   ", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=show_dropdown_grp3)
        grp3_button.pack(pady=10, anchor='w')

        # Gruppe 4
        def show_dropdown_grp4():
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg=ThemeManager.SRH_Grey, fg='black')
            dropdown_menu.add_command(label="→ Alles Anzeigen", command=lambda: show_right_table(2, "4",
                                                                                                 ""))  # Alle Objekte mit der Gruppe x werden angezeigt
            dropdown_menu.add_command(label="→ Hardware", command=lambda: show_right_table(8, "4",
                                                                                           "Hardwawre"))  # nur Hardware Objekte mit der Gruppe x werden angezeigt
            dropdown_menu.add_command(label="→ Software", command=lambda: show_right_table(8, "4",
                                                                                           "Sorftware"))  # nur Software Produkte mit der Gruppe x werden angezeigt
            dropdown_menu.add_command(label="→ Peripherie", command=lambda: show_right_table(8, "4",
                                                                                             "Peripherie"))  # nur Peripherie mit der Gruppe x werden angezeigt
            dropdown_menu.add_command(label="→ Andere", command=lambda: show_right_table(8, "4",
                                                                                         "ANDERE"))  # Andere Objekte mit der Gruppe x werden angezeigt (z.B.: Bücher)
            dropdown_menu.post(grp4_button.winfo_rootx(), grp4_button.winfo_rooty() + grp4_button.winfo_height())

        grp4_button = tk.Button(verzeichniss, text="Gruppe 4   ", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=show_dropdown_grp4)
        grp4_button.pack(pady=10, anchor='w')

        # Gruppe 5
        def show_dropdown_grp5():
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg=ThemeManager.SRH_Grey, fg='black')
            dropdown_menu.add_command(label="→ Alles Anzeigen", command=lambda: show_right_table(2, "5",
                                                                                                 ""))  # Alle Objekte mit der Gruppe x werden angezeigt
            dropdown_menu.add_command(label="→ Hardware", command=lambda: show_right_table(8, "5",
                                                                                           "Hardwawre"))  # nur Hardware Objekte mit der Gruppe x werden angezeigt
            dropdown_menu.add_command(label="→ Software", command=lambda: show_right_table(8, "5",
                                                                                           "Software"))  # nur Software Produkte mit der Gruppe x werden angezeigt
            dropdown_menu.add_command(label="→ Peripherie", command=lambda: show_right_table(8, "5",
                                                                                             "Peripherie"))  # nur Peripherie mit der Gruppe x werden angezeigt
            dropdown_menu.add_command(label="→ Andere", command=lambda: show_right_table(8, "5",
                                                                                         "ANDERE"))  # Andere Objekte mit der Gruppe x werden angezeigt (z.B.: Bücher)
            dropdown_menu.post(grp5_button.winfo_rootx(), grp5_button.winfo_rooty() + grp5_button.winfo_height())

        grp5_button = tk.Button(verzeichniss, text="Gruppe 5   ", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=show_dropdown_grp5)
        grp5_button.pack(pady=10, anchor='w')

        # Gruppe 6
        def show_dropdown_grp6():
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg=ThemeManager.SRH_Grey, fg='black')
            dropdown_menu.add_command(label="→ Alles Anzeigen", command=lambda: show_right_table(2, "6",
                                                                                                 ""))  # Alle Objekte mit der Gruppe x werden angezeigt
            dropdown_menu.add_command(label="→ Hardware", command=lambda: show_right_table(8, "6",
                                                                                           "Hardwawre"))  # nur Hardware Objekte mit der Gruppe x werden angezeigt
            dropdown_menu.add_command(label="→ Software", command=lambda: show_right_table(8, "6",
                                                                                           "Software"))  # nur Software Produkte mit der Gruppe x werden angezeigt
            dropdown_menu.add_command(label="→ Peripherie", command=lambda: show_right_table(8, "6",
                                                                                             "Peripherie"))  # nur Peripherie mit der Gruppe x werden angezeigt
            dropdown_menu.add_command(label="→ Andere", command=lambda: show_right_table(8, "6",
                                                                                         "ANDERE"))  # Andere Objekte mit der Gruppe x werden angezeigt (z.B.: Bücher)
            dropdown_menu.post(grp6_button.winfo_rootx(), grp6_button.winfo_rooty() + grp6_button.winfo_height())

        grp6_button = tk.Button(verzeichniss, text="Gruppe 6   ", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=show_dropdown_grp6)
        grp6_button.pack(pady=10, anchor='w')

        # Gruppe 7
        def show_dropdown_grp7():
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg=ThemeManager.SRH_Grey, fg='black')
            dropdown_menu.add_command(label="→ Alles Anzeigen", command=lambda: show_right_table(2, "7",
                                                                                                 ""))  # Alle Objekte mit der Gruppe x werden angezeigt
            dropdown_menu.add_command(label="→ Hardware", command=lambda: show_right_table(8, "7",
                                                                                           "Hardwawre"))  # nur Hardware Objekte mit der Gruppe x werden angezeigt
            dropdown_menu.add_command(label="→ Software", command=lambda: show_right_table(8, "7",
                                                                                           "Software"))  # nur Software Produkte mit der Gruppe x werden angezeigt
            dropdown_menu.add_command(label="→ Peripherie", command=lambda: show_right_table(8, "7",
                                                                                             "Peripherie"))  # nur Peripherie mit der Gruppe x werden angezeigt
            dropdown_menu.add_command(label="→ Andere", command=lambda: show_right_table(8, "7",
                                                                                         "ANDERE"))  # Andere Objekte mit der Gruppe x werden angezeigt (z.B.: Bücher)
            dropdown_menu.post(grp7_button.winfo_rootx(), grp7_button.winfo_rooty() + grp7_button.winfo_height())

        grp7_button = tk.Button(verzeichniss, text="Gruppe 7   ", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=show_dropdown_grp7)
        grp7_button.pack(pady=10, anchor='w')

        # Gruppe 8
        def show_dropdown_grp8():
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg=ThemeManager.SRH_Grey, fg='black')
            dropdown_menu.add_command(label="→ Alles Anzeigen", command=lambda: show_right_table(2, "8",
                                                                                                 ""))  # Alle Objekte mit der Gruppe x werden angezeigt
            dropdown_menu.add_command(label="→ Hardware", command=lambda: show_right_table(8, "8",
                                                                                           "Hardwawre"))  # nur Hardware Objekte mit der Gruppe x werden angezeigt
            dropdown_menu.add_command(label="→ Software", command=lambda: show_right_table(8, "8",
                                                                                           "Software"))  # nur Software Produkte mit der Gruppe x werden angezeigt
            dropdown_menu.add_command(label="→ Peripherie", command=lambda: show_right_table(8, "8",
                                                                                             "Peripherie"))  # nur Peripherie mit der Gruppe x werden angezeigt
            dropdown_menu.add_command(label="→ Andere", command=lambda: show_right_table(8, "8",
                                                                                         "ANDERE"))  # Andere Objekte mit der Gruppe x werden angezeigt (z.B.: Bücher)
            dropdown_menu.post(grp8_button.winfo_rootx(), grp8_button.winfo_rooty() + grp8_button.winfo_height())

        grp8_button = tk.Button(verzeichniss, text="Gruppe 8   ", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=show_dropdown_grp8)
        grp8_button.pack(pady=10, anchor='w')

        # Seiteninhalt
        # switch_button = tk.Button(self, text="switch", bg='#081424', fg='white',
        # font=("Inter", 20, 'bold'),
        # command=lambda: controller.show_frame(Gerateansicht))
        # switch_button.grid(row=4, column=0, pady=20)
        # Bilder
        self.imgFilter = load_image(root_path + "/gui/assets/Filter_Button.png")
        self.imgSuche = load_image(root_path + "/gui/assets/Search.png")
        self.imgHinzufugen = load_image(root_path + "/gui/assets/Adding_Icon.png")
        self.imgAktionen = load_image(root_path + "/gui/assets/Aktionen_Button.png")

        def fill_in_sort(table, where, DESC_OR_ASC):
            items_uberschrift = fetch_headers("items", [""])

            # Überschriften konfigurieren
            overview_table_tree["columns"] = items_uberschrift
            for up in items_uberschrift:
                overview_table_tree.column(up, anchor=CENTER, width=100)
                overview_table_tree.heading(up, text=up)

            items_data = table_sort(table, where, [""], DESC_OR_ASC)

            overview_table_tree.delete(*overview_table_tree.get_children())
            TreeLogger.debug(f"'{overview_table_tree.get_children()}'")

            # Daten aus DB einfügen
            i = 0
            for item in items_data:
                formatted_row = [value if value is not None else "-" for value in
                                 item]  # Leere Felder durch "-" ersetzen
                overview_table_tree.insert("", "end", values=formatted_row, tags=("even" if i % 2 == 0 else "odd"))
                TreeLogger.debug(f"'{overview_table_tree.get_children()}'")
                i += 1

        # Filterfunktion
        def show_dropdown_Filter():
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg='white', fg='black')
            dropdown_menu.add_command(label="→ Status", command=lambda: fill_in_sort("items", "Status", "DESC"))
            dropdown_menu.add_command(label="→ ID", command=lambda: fill_in_sort("items", "ID", "ASC"))
            dropdown_menu.add_command(label="→ Typ", command=lambda: fill_in_sort("items", "Typ", "DESC"))
            dropdown_menu.add_command(label="→ Gruppe", command=lambda: fill_in_sort("items", "Gruppe", "ASC"))
            dropdown_menu.add_command(label="→ Andere", command=lambda: print("nach anderen sortieren"))
            dropdown_menu.post(Filter_button.winfo_rootx(), Filter_button.winfo_rooty() + Filter_button.winfo_height())

        Filter_button = tk.Button(self.ubersicht_frame, image=self.imgFilter, bd=0, bg='white', fg='black',
                                  font=("Inter", 20, 'bold'),
                                  command=show_dropdown_Filter)
        Filter_button.place(relx=0, rely=0.1)

        # Suche

        def search_bar_output():
            suche_text = suche_entry.get()
            search_results = search_bar_update(suche_text)
            overview_table_tree.delete(*overview_table_tree.get_children())

            # Daten aus DB einfügen
            i = 0
            for item in search_results:
                overview_table_tree.insert("", "end", values=item, tags=("even" if i % 2 == 0 else "odd"))
                i += 1

        suche_button = ctk.CTkButton(self.ubersicht_frame, image=self.imgSuche, corner_radius=8, border_width=0,
                                     fg_color="transparent", hover_color='#D9D9D9',
                                     command=lambda: search_bar_output())
        suche_entry = ctk.CTkEntry(self.ubersicht_frame, corner_radius=8, fg_color="#D9D9D9", text_color="black",
                                   border_width=0, font=("Inter", 12))

        # Binde die Enter-Taste an die Suchfunktion
        suche_entry.bind("<Return>", lambda event: search_bar_output())

        suche_button.place(relx=0.1, rely=0.1, relheight=0.04, relwidth=0.022)
        suche_entry.place(relx=0.125, rely=0.1, relwidth=0.33, relheight=0.04)

        # Hinzufügen
        Hinzufugen_button = tk.Button(self.ubersicht_frame, image=self.imgHinzufugen, bd=0, bg='white',
                                      command=lambda: controller.show_frame(Gerateansicht))
        Hinzufugen_button.place(relx=0.5, rely=0.1)

        # Aktionen
        Aktionen_button = tk.Button(self.ubersicht_frame, image=self.imgAktionen, bd=0, bg='white',
                                    command=lambda: print("Aktionen werden ausgeführt"))
        Aktionen_button.place(relx=0.6, rely=0.1)

        # Tabelle
        # Styling
        style = ttk.Style()
        # style.theme_use("")
        style.configure("Treeview.Heading", font=("Inter", 12), background="#D9D9D9", foreground="#6E6893")
        style.configure("Treeview", font=("Arial", 11), rowheight=35, background="white", foreground="black")
        style.map("Treeview", background=[("selected", "#D9D9D9")], foreground=[("selected", "black")])
        style.configure("evenrow.Treeview", background="#f2f2f2")
        style.configure("oddrow.Treeview", background="white")

        scroll = ctk.CTkScrollbar(
            self.tabelle_frame,
            button_color=ThemeManager.SRH_Grey,
            orientation="vertical",
            command=overview_table_tree.yview,
            height=650
        )

        # Treeview Scrollverbindung
        overview_table_tree.configure(yscrollcommand=scroll.set)
        TreeLogger.debug(f"'{overview_table_tree.get_children()}'")

        def starting_table():
            logging.debug(
                f"{loggerStyleAnsiEscSgr.foregroundColor.brightyellow}starting_table{loggerStyleAnsiEscSgr.foregroundColor.yellow}(){loggerStyleAnsiEscSgr.foregroundColor.reset} wird ausgeführt")
            # Spaltennamen aus der Datenbank holen
            overview_table_tree.delete(*overview_table_tree.get_children())
            TreeLogger.debug(f"'{overview_table_tree.get_children()}'")
            items_uberschrift = fetch_headers("items", ["image"])

            # Überschriften konfigurieren
            overview_table_tree["columns"] = items_uberschrift
            for up in items_uberschrift:
                overview_table_tree.column(up, anchor=CENTER, width=100)
                overview_table_tree.heading(up, text=up)
            TreeLogger.debug(f"'{overview_table_tree.get_children()}'")
            items_data = fetch_tables("items", ["image"])

            # Daten aus DB einfügen

            for i, row in enumerate(items_data):
                formatted_row = [value if value is not None else "-" for value in
                                 row]  # Leere Felder durch "-" ersetzen
                overview_table_tree.insert("", "end", values=formatted_row, tags=("even" if i % 2 == 0 else "odd"))
            TreeLogger.debug(f"'{overview_table_tree.get_children()}'")
            logging.debug(
                f"{loggerStyleAnsiEscSgr.foregroundColor.brightyellow}starting_table{loggerStyleAnsiEscSgr.foregroundColor.yellow}(){loggerStyleAnsiEscSgr.foregroundColor.reset} wurde ausgeführt")

        # Gerät aus Tabelle öffnen
        def on_item_select(event):
            try:

                selected_Item = overview_table_tree.focus()
                print(f"Ausgewähltes Item: {selected_Item}")
                if selected_Item:
                    # exports the data to a cache file for later usage
                    cache.selected_item = showDetails(selected_Item, overview_table_tree, controller)

            except Exception as e:
                print(f"Fehler bei der Auswahl {e}")

        overview_table_tree.bind("<Double-1>", on_item_select)

        # Farben für Tags definieren
        overview_table_tree.tag_configure("even", background="#f7f7f7")
        overview_table_tree.tag_configure("odd", background="white")

        scroll.place(x=1400, y=0)
        # Setze explizite Mindesthöhe für Zeile 5
        # self.tabelle_frame.grid_rowconfigure(5, minsize=10)
        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)
        verzeichniss.place(relx=0, rely=0.15, relwidth=0.15, relheight=0.85)
        self.tabelle_frame.place(relx=0.15, rely=0.3, relwidth=0.85, height=800)
        show_the_active_group()


def showDetails(selected_Item, tree, controller):
    data = tree.item(selected_Item, "values")
    print(f"Daten des ausgewählten Items: {data}")

    details = controller.frames[Gerateansicht]
    details.update_data(data)
    details.update_history_table(controller, data)
    controller.show_frame(Gerateansicht)
    return data


############################################
# ୧‿̩͙ ˖︵ ꕀ⠀ ♱ Geräteansicht ♱⠀ ꕀ ︵˖ ‿̩͙୨#
############################################

class Gerateansicht(tk.Frame):
    def __init__(self, parent, controller):
        root_path = os.path.dirname(os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir)))
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.root_path = root_path

        self.configure(bg='white')
        self.setup_grid()
        self.load_images()
        self.setup_styles()
        self.create_widgets()
        self.place_widgets()
        self.dbupdate()

    def setup_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)

    def load_images(self):
        self.imglogin = tk.PhotoImage(file=self.root_path + "/gui/assets/Closeicon.png")
        self.imgmainpage = tk.PhotoImage(file=self.root_path + "/gui/assets/backtosite_grey_icon.png")
        self.imgprofil = load_image(self.root_path + "/gui/assets/profileicon.png")
        self.imghelp = tk.PhotoImage(file=self.root_path + "/gui/assets/helpicon.png")
        self.schaeden_img = load_image(self.root_path + "/gui/assets/Button_Schaeden.png")
        self.buchung_img = load_image(self.root_path + "/gui/assets/Button_Buchung.png")
        self.speichern_img = load_image(self.root_path + "/gui/assets/Button_Speichern.png")

    def setup_styles(self):
        style = ttk.Style()
        style.configure("Header.TLabel", foreground='white', background=ThemeManager.SRH_Orange, font=("Inter", 50, 'bold'))
        style.configure("Footer.TLabel", background=ThemeManager.SRH_Grey)

    def create_widgets(self):
        self.header = ttk.Label(self, text="Geräteansicht", anchor="center", style="Header.TLabel")
        self.verzeichniss = ttk.Label(self, style="Footer.TLabel")
        self.gerateansicht_frame = tk.Frame(self, bg='white')

        self.login_button = ctk.CTkButton(self.header, image=self.imglogin, fg_color=ThemeManager.SRH_Orange,
                                          bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                                          hover=True, hover_color='#e25a1f', text="",
                                          command=lambda: self.controller.show_frame(LogInWindow))

        self.profil_button = ctk.CTkButton(self.header, image=self.imgprofil, fg_color=ThemeManager.SRH_Orange,
                                           bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                                           hover=True, hover_color='#e25a1f', text="",
                                           command=lambda: self.controller.show_frame(Profil))

        self.help_button = ctk.CTkButton(self.header, image=self.imghelp, fg_color=ThemeManager.SRH_Orange,
                                         bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                                         hover=True, hover_color='#e25a1f', text="",
                                         command=lambda: self.controller.show_frame(Help))

        self.mainpage_button = ctk.CTkButton(self, text="↩", fg_color='white', text_color=ThemeManager.SRH_Grey, width=5,
                                             font=("Inter", 50, 'bold'), corner_radius=8, hover=False,
                                             command=lambda: self.controller.show_frame(Ubersicht))

        self.tree = ttk.Treeview(self.gerateansicht_frame, columns=("c1", "c2", "c3"), show="headings", height=5)
        self.scroll = ctk.CTkScrollbar(self.gerateansicht_frame, button_color=ThemeManager.SRH_Grey,
                                       orientation="vertical", command=self.tree.yview, height=650)

        self.name_frame = self.create_entry_frame("Gerätename", 900, 20)
        self.name_entry = self.create_entry(self.name_frame, 5, 50)

        self.tag_frame = self.create_entry_frame("Servicetag/Seriennummer", 900, 120)
        self.tag_entry = self.create_entry(self.tag_frame, 5, 50)

        self.typ_frame = self.create_entry_frame("Gerätetyp", 900, 220)
        self.typ_aktuell_label = ctk.CTkLabel(self.typ_frame, text="", text_color='black', font=("Inter", 20))
        self.typ_aktuell_label.place(x=5, y=50)
        self.typ_drop = tk.Button(self.typ_frame, text="↓", bd=0, bg='white', fg='black', font=("Inter", 20, 'bold'),
                                  command=self.typ_dropdown)
        self.typ_drop.place(x=420, y=30)

        self.status_frame = self.create_entry_frame("Status", 900, 320)
        self.status_aktuell_label = ctk.CTkLabel(self.status_frame, text="", text_color='black', font=("Inter", 20))
        self.status_aktuell_label.place(x=5, y=50)
        self.status_drop = tk.Button(self.status_frame, text="↓", bd=0, bg='white', fg='black', font=("Inter", 20, 'bold'),
                                     command=self.status_dropdown)
        self.status_drop.place(x=420, y=30)

        self.gruppe_frame = self.create_entry_frame("Gruppe", 900, 420)
        self.gruppe_aktuell_label = ctk.CTkLabel(self.gruppe_frame, text="", text_color='black', font=("Inter", 20))
        self.gruppe_aktuell_label.place(x=5, y=50)
        self.gruppe_drop = tk.Button(self.gruppe_frame, text="↓", bd=0, bg='white', fg='black', font=("Inter", 20, 'bold'),
                                     command=self.gruppe_dropdown)
        self.gruppe_drop.place(x=420, y=30)

        self.anzahl_frame = self.create_entry_frame("Stückzahl", 900, 520)
        self.anzahl_entry = self.create_entry(self.anzahl_frame, 5, 50)

        self.details_frame = self.create_entry_frame("Details", 900, 620)
        self.details_entry = self.create_entry(self.details_frame, 5, 50)

        self.standort_frame = self.create_entry_frame("Standort (Haus, Raum)", 900, 720)
        self.standort_entry = self.create_entry(self.standort_frame, 5, 50)

        self.buttons_frame = tk.Frame(self.gerateansicht_frame, bg='white', bd=0, relief="solid")
        self.schaeden_button = tk.Button(self.buttons_frame, image=self.schaeden_img, bd=0, bg='white',
                                         command=self.open_schaeden_page)
        self.schaeden_button.place(x=5, y=10)

        self.buchung_button = tk.Button(self.buttons_frame, image=self.buchung_img, bd=0, bg='white',
                                        command=self.open_buchen_page)
        self.buchung_button.place(x=165, y=10)

        self.speichern_button = tk.Button(self.buttons_frame, image=self.speichern_img, bd=0, bg='white',
                                          command=self.button_click)
        self.speichern_button.place(x=330, y=10)

    def place_widgets(self):
        self.header.place(relx=0, rely=0, relwidth=1, relheight=0.15)
        self.verzeichniss.place(relx=0, rely=0.15, relwidth=0.15, relheight=0.85)
        self.login_button.place(relx=0.95, rely=0.5, anchor="center")
        self.profil_button.place(relx=0.90, rely=0.5, anchor="center")
        self.help_button.place(relx=0.85, rely=0.5, anchor="center")
        self.mainpage_button.place(relx=0.16, rely=0.16, anchor='nw')
        self.gerateansicht_frame.place(relx=0.21, rely=0.15, relwidth=1, relheight=0.85)
        self.buttons_frame.place(x=150, y=710, width=480, height=74)

    def create_entry_frame(self, label_text, x, y):
        frame = ctk.CTkFrame(self.gerateansicht_frame, width=480, height=88, bg_color='transparent',
                             fg_color='transparent', border_width=1, border_color='#B8B7B7', corner_radius=8)
        label = ctk.CTkLabel(frame, text=label_text, text_color='#858383', font=("Inter", 25, 'bold'))
        label.place(x=5, y=5)
        frame.place(x=x, y=y)
        return frame

    def create_entry(self, frame, x, y):
        entry = ctk.CTkEntry(frame, text_color='black', font=("Inter", 20), border_width=0, fg_color='transparent')
        entry.place(x=x, y=y)
        return entry

    def dbupdate(self):
        self.tree.configure(yscrollcommand=self.scroll.set)
        self.tree.delete(*self.tree.get_children())
        items_uberschrift = fetch_headers("history", ["foreign_item_num", "image", "name", "tag"])
        self.tree["columns"] = items_uberschrift
        for up in items_uberschrift:
            self.tree.column(up, anchor=CENTER, width=100)
            self.tree.heading(up, text=up)
        items_data = fetch_tables("history", ["foreign_item_num", "image", "name", "tag"])
        for i, row in enumerate(items_data):
            formatted_row = [value if value is not None else "-" for value in row]
            self.tree.insert("", "end", values=formatted_row, tags=("even" if i % 2 == 0 else "odd"))
        self.tree.place(x=0, y=20, relwidth=0.40, relheight=0.5)
        self.scroll.place(x=770, y=20, relheight=0.5)
        self.tree.bind("<<TreeviewSelect>>", self.on_row_click)

    def on_row_click(self, event):
        selected_item = self.tree.focus()
        item_data = self.tree.item(selected_item, "values")
        if item_data and item_data[1] == 'DMG':
            indexnum = item_data[0]
            show_image_from_db(indexnum)

    def typ_dropdown(self):
        dropdown_menu = tk.Menu(self.typ_frame, tearoff=0, bd=1, bg='white', fg='black')
        Kategorienname = ["PC", "Laptop", "Bildschirm", "Raspberrypie", "Dockingstation", "Drucker", "Kabel", "Peripherie", "Software", "Sonstiges"]
        for value1 in Kategorienname:
            dropdown_menu.add_command(label=f"→ {value1}", command=lambda value=value1: [self.typ_aktuell_label.configure(text=value), print(f"{value} ausgewählt")])
        dropdown_menu.post(self.typ_drop.winfo_rootx() - 77, self.typ_drop.winfo_rooty() + self.typ_drop.winfo_height())

    def status_dropdown(self):
        dropdown_menu = tk.Menu(self.status_frame, tearoff=0, bd=1, bg='white', fg='black')
        Kategorienname = ["⛔In Wartung", "✔Verfügbar", "❌Gemietet"]
        for value1 in Kategorienname:
            dropdown_menu.add_command(label=f"→ {value1}", command=lambda value=value1: [self.status_aktuell_label.configure(text=value), print(f"Produkt {value}")])
        dropdown_menu.post(self.status_drop.winfo_rootx() - 62, self.status_drop.winfo_rooty() + self.status_drop.winfo_height())

    def gruppe_dropdown(self):
        dropdown_menu = tk.Menu(self.gruppe_frame, tearoff=0, bd=1, bg='white', fg='black')
        Gruppenname = [i for i in range(1, 9)]
        for value2 in Gruppenname:
            dropdown_menu.add_command(label=f"→ {value2}", command=lambda value=value2: [self.gruppe_aktuell_label.configure(text=value2), print(f"Produkt {value2}")])
        dropdown_menu.post(self.gruppe_drop.winfo_rootx() - 62, self.gruppe_drop.winfo_rooty() + self.gruppe_drop.winfo_height())

    def open_schaeden_page(self):
        schaeden_page = tk.Toplevel()  # root
        schaeden_page.title("Schäden eintragen")
        schaeden_page.geometry("819x594+500+300")
        schaeden_page.configure(bg='white')

        schaeden_page.grab_set()

        # Bilder
        self.aktualisieren_img = load_image(self.root_path + "/gui/assets/Button_Aktualisieren.png")
        self.upload_img = load_image(self.root_path + "/gui/assets/Button_Drop.png")

        # Informationen
        info_frame = tk.Frame(schaeden_page, bg='white', bd=1)
        verlauf_frame = tk.Frame(schaeden_page, bg='white', bd=1)

        name_label = tk.Label(info_frame, text="Gerätename", bg='white', font=("Inter", 19))
        name_entry_frame = ctk.CTkFrame(info_frame, width=150, height=40, bg_color='transparent',
                                        fg_color='transparent', border_width=1, border_color='#B8B7B7',
                                        corner_radius=8)
        name_entry = ctk.CTkEntry(name_entry_frame, text_color='black', font=("Inter", 15), border_width=0,
                                    fg_color='transparent', width=100)
        pre_filled_name = cache.selected_item[1]  # enters the name of the selected item into the field
        name_entry.insert(0, pre_filled_name)  # Insert text at position 0 (start of the field)

        tag_label = tk.Label(info_frame, text="Tag", bg='white', font=("Inter", 19))
        tag_entry_frame = ctk.CTkFrame(info_frame, width=150, height=40, bg_color='transparent',
                                        fg_color='transparent', border_width=1, border_color='#B8B7B7',
                                        corner_radius=8)
        tag_entry = ctk.CTkEntry(tag_entry_frame, text_color='black', font=("Inter", 15), border_width=0,
                                    fg_color='transparent', width=100)
        pre_filled_tag = cache.selected_item[6]  # enters the name of the selected item into the field
        tag_entry.insert(0, pre_filled_tag)  # Insert text at position 0 (start of the field)

        date_label = tk.Label(info_frame, text="Datum", bg='white', font=("Inter", 19))
        date_entry_frame = ctk.CTkFrame(info_frame, width=150, height=40, bg_color='transparent',
                                        fg_color='transparent', border_width=1, border_color='#B8B7B7',
                                        corner_radius=8)
        date_entry = datetime.now().strftime("%d.%m.%Y")
        current_date = tk.Label(date_entry_frame, text=date_entry, font=("Inter", 13), bg='white', fg='black', bd=0)

        beschreibung_label = tk.Label(info_frame, text="Beschreibung", bg='white', font=("Inter", 19))
        beschreibung_entry_frame = ctk.CTkFrame(info_frame, width=380, height=382, bg_color='transparent',
                                                fg_color='transparent', border_width=1, border_color='#B8B7B7',
                                                corner_radius=8)
        beschreibung_entry = ctk.CTkEntry(beschreibung_entry_frame, fg_color='transparent', text_color='black',
                                            font=("Inter", 13), width=380, height=382, border_width=1,
                                            border_color='#B8B7B7', corner_radius=8)

        # Verlauf
        verlauf_label = tk.Label(verlauf_frame, text="Verlauf", bg='white', font=("Inter", 19))
        verlauf_inh_entry = ctk.CTkEntry(verlauf_frame, fg_color='transparent', text_color='black',
                                            font=("Inter", 13),
                                            width=380, height=382, border_width=1, border_color='#B8B7B7',
                                            corner_radius=8)

        # Button-Funktion
        def process_user_input():
            
            # Werte aus den Eingabefeldern abrufen
            name = name_entry.get()
            tag = tag_entry.get()
            beschreibung = beschreibung_entry.get()
            img = self.last_uploaded_file

            schaeden_page.destroy()
            self.dbupdate()

            # Hier kannst du die Daten weiterverarbeiten
            # ausgabe an die Funktion, die die Daten in die Datenbank weiterreicht
            item_update_damage(name, tag, cache.selected_item[0], "DMG", img, beschreibung)
            self.dbupdate()

        # Buttons
        schaeden_button_frame = tk.Frame(schaeden_page, bg='white', bd=1)

        self.last_uploaded_file = None
        upload_button = tk.Button(schaeden_button_frame, image=self.upload_img, bd=0, bg='white',
                                    command=lambda: [
                                        self.image_to_binary(self.choose_image_popup()),
                                        print("Bild hochgeladen")])
        close_button = tk.Button(schaeden_button_frame, image=self.aktualisieren_img, bd=0, bg='white',
                                    command=process_user_input)

        # Placement
        name_label.place(x=0, y=2)
        name_entry.place(x=5, y=5)
        name_entry_frame.place(x=150, y=2)

        tag_label.place(x=0, y=52)
        tag_entry.place(x=5, y=5)
        tag_entry_frame.place(x=150, y=52)

        date_label.place(x=0, y=102)
        current_date.place(x=8, y=8)
        date_entry_frame.place(x=150, y=102)

        beschreibung_label.place(x=0, y=152)
        beschreibung_entry.place(x=0, y=0)
        beschreibung_entry_frame.place(x=10, y=202)

        verlauf_label.place(x=15, y=0)
        verlauf_inh_entry.place(x=15, y=50)

        upload_button.place(x=10, y=10)
        close_button.place(x=200, y=40)
        info_frame.place(x=0, y=0, width=409, height=594)
        verlauf_frame.place(x=409, y=0, width=409, height=444)
        schaeden_button_frame.place(x=409, y=444, width=409, height=150)

    def open_buchen_page(self):
        buchen_page = tk.Toplevel()  # root
        buchen_page.title("Gerät buchen")
        buchen_page.geometry("819x594+500+300")
        buchen_page.configure(bg='white')

        buchen_page.grab_set()
        # Bilder
        self.aktualisieren_img = load_image(self.root_path + "/gui/assets/Button_Aktualisieren.png")

        # Informationen
        info_frame = tk.Frame(buchen_page, bg='white', bd=1)
        date_frame = tk.Frame(buchen_page, bg='white', bd=1)

        name_label = tk.Label(info_frame, text="Gerätename", bg='white',
                                font=("Inter", 19))
        name_entry = ctk.CTkEntry(info_frame, fg_color='transparent', text_color='black', font=("Inter", 15),
                                    width=150, border_width=1, border_color='#B8B7B7', corner_radius=8)
        pre_filled_name = cache.selected_item[1]  # enters the name of the selected item into the field
        name_entry.insert(0, pre_filled_name)  # Insert text at position 0 (start of the field)

        tag_label = tk.Label(info_frame, text="Servicetag", bg='white',
                                font=("Inter", 19))
        tag_entry = ctk.CTkEntry(info_frame, fg_color='transparent', text_color='black', font=("Inter", 15),
                                    width=150, border_width=1, border_color='#B8B7B7', corner_radius=8)
        pre_filled_tag = cache.selected_item[6]  # enters the name of the selected item into the field
        tag_entry.insert(0, pre_filled_tag)  # Insert text at position 0 (start of the field)

        verlauf_label = tk.Label(info_frame, text="Verlauf", bg='white',
                                    font=("Inter", 19))
        verlauf_entry = ctk.CTkEntry(info_frame, fg_color='transparent', text_color='black', font=("Inter", 15),
                                        width=380, height=382, border_width=1, border_color='#B8B7B7', corner_radius=8)

        def ask_startdate():

            # Benutzer nach Datum fragen
            entered_date = simpledialog.askstring("Datum", "Startdatum (Format: DD.MM.YYYY:)")
            try:
                # Datum validieren
                datetime.strptime(entered_date, "%d.%m.%Y")
                start_result_label.config(text=f"von: {entered_date}")
                global global_input_date
                global_input_date = entered_date
            except (ValueError, TypeError):
                start_result_label.config(text="Ungültiges Datum!")

        # Button zur Datumseingabe
        ask_date_button = ctk.CTkButton(date_frame, text="Startdatum", command=ask_startdate, corner_radius=8,
                                        fg_color="#6F6C6C", text_color="white", hover_color="#081424")
        ask_date_button.place(x=0, y=0)

        
        start_result_label = tk.Label(date_frame, text=datetime.now().strftime('von: %d.%m.%Y'), font=("Arial", 14),
                                        bg='white')
        start_result_label.place(x=150, y=0)

        def ask_enddate():
            date_frame.focus_set()
            # Benutzer nach Datum fragen
            entered_date = simpledialog.askstring("Datum", "Enddatum (Format: DD.MM.YYYY:)")
            try:
                # Datum validieren
                datetime.strptime(entered_date, "%d.%m.%Y")
                global global_input_enddate
                global_input_enddate = entered_date

                end_result_label.config(text=f"bis: {entered_date}")
            except ValueError:
                end_result_label.config(text="Ungültiges Datum!")
            # Button zur Datumseingabe

        ask_date_button = ctk.CTkButton(date_frame, text="Enddatum", command=ask_enddate, corner_radius=8,
                                        fg_color="#081424", text_color="white", hover_color="#6F6C6C")
        ask_date_button.place(x=0, y=100)
        # Ergebnis-Label
        end_result_label = tk.Label(date_frame, text=datetime.now().strftime('bis: %d.%m.%Y'), font=("Arial", 14),
                                    bg='white')
        end_result_label.place(x=150, y=100)

        # Button-Funktion
        def process_user_input():
            
            # Werte aus den Eingabefeldern abrufen
            name = name_entry.get()
            tag = tag_entry.get()
            global global_input_date
            eingangsdatum = global_input_date
            global global_input_enddate
            enddatum = global_input_enddate
            img = None  # der upload img button hat noch keine funktion

            buchen_page.destroy()

            # Hier kannst du die Daten weiterverarbeiten
            # ausgabe an die Funktion, die die Daten in die Datenbank weiterreicht
            item_update_damage(name, tag, cache.selected_item[0], "BUCHUNG", img, "BUCHUNG", eingangsdatum,
                                enddatum)
            self.dbupdate()

        # Buttons
        buchen_button_frame = tk.Frame(buchen_page, bg='white', bd=1)
        close_button = tk.Button(buchen_button_frame, image=self.aktualisieren_img, bd=0, bg='white',
                                    command=process_user_input)
        # Placement
        name_label.place(x=0, y=2)
        name_entry.place(x=150, y=2)

        tag_label.place(x=0, y=52)
        tag_entry.place(x=150, y=52)

        verlauf_label.place(x=0, y=152)
        verlauf_entry.place(x=10, y=202)

        close_button.place(x=200, y=40)
        info_frame.place(x=0, y=0, width=409, height=594)
        date_frame.place(x=409, y=0, width=409, height=444)
        buchen_button_frame.place(x=409, y=444, width=409, height=150)

    def button_click(self):
        update_item(self.update_items_on_save())
        self.controller.show_frame(Ubersicht)
        messagebox.showinfo("Erfolgreich", "Änderungen erfolgreich gespeichert")

    def update_history_table(self, controller, data):
        tree = ttk.Treeview(self.gerateansicht_frame, columns=("c1", "c2", "c3"), show="headings",
                            height=5)
        scroll = ctk.CTkScrollbar(
            self.gerateansicht_frame,
            button_color=ThemeManager.SRH_Grey,
            orientation="vertical",
            command=tree.yview,
            height=650
        )

        item_ID = data[0]

        def dbupdate(item_ID):
            # Treeview Scrollverbindung
            tree.configure(yscrollcommand=scroll.set)

            # Spaltennamen aus der Datenbank holen
            tree.delete(*tree.get_children())
            items_uberschrift = fetch_headers("history", ["foreign_item_num", "image", "name", "tag"])

            # Überschriften konfigurieren
            tree["columns"] = items_uberschrift
            for up in items_uberschrift:
                tree.column(up, anchor=CENTER, width=100)
                tree.heading(up, text=up)

            print(item_ID)
            items_data = show_history_table(item_ID, ["foreign_item_num", "image", "name", "tag"])

            # Daten aus DB einfügen
            for i, row in enumerate(items_data):
                formatted_row = [value if value is not None else "-" for value in
                                 row]  # Leere Felder durch "-" ersetzen    
                tree.insert("", "end", values=formatted_row, tags=("even" if i % 2 == 0 else "odd"))

            tree.place(x=0, y=20, relwidth=0.40, relheight=0.5)
            scroll.place(x=770, y=20, relheight=0.5)

            # Add row click event
            tree.bind("<<TreeviewSelect>>", on_row_click)

        def on_row_click(event):
            # Get the selected item
            selected_item = tree.focus()  # Returns the ID of the selected item
            item_data = tree.item(selected_item, "values")  # Fetch the values of the selected row

            # Retrieve the indexnum (assuming it's the first column)
            if item_data:
                print(f"Selected itemdata: {item_data}")
                if item_data[1] == 'DMG':
                    indexnum = item_data[0]  # Replace with the desired index number
                    show_image_from_db(indexnum)

        dbupdate(item_ID)

    def update_data(self, data):
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, data[1])
        self.tag_entry.delete(0, tk.END)
        self.tag_entry.insert(0, data[6])
        self.typ_aktuell_label.configure(text=data[8])
        self.status_aktuell_label.configure(text=data[9])
        self.gruppe_aktuell_label.configure(text=data[2])
        self.details_entry.delete(0, tk.END)
        self.details_entry.insert(0, data[5])
        self.anzahl_entry.delete(0, tk.END)
        self.anzahl_entry.insert(0, data[4])
        self.standort_entry.delete(0, tk.END)
        self.standort_entry.insert(0, data[3])

    def update_items_on_save(self):
        updated_items = {
            "ID": cache.selected_item[0],
            "Name": self.name_entry.get(),
            "Gruppe": self.gruppe_aktuell_label.cget("text"),
            "Raum": self.standort_entry.get(),
            "amount": self.anzahl_entry.get(),
            "Details": self.details_entry.get(),
            "service_tag": self.tag_entry.get(),
            "added_by_user": cache.selected_item[7],
            "Typ": self.typ_aktuell_label.cget("text"),
            "Status": self.status_aktuell_label.cget("text")
        }
        return updated_items

    def choose_image_popup(self):
        import tkinter
        file = tkinter.filedialog.askopenfilename()
        return file

    def image_to_binary(self, image_path):
        try:
            with open(image_path, 'rb') as image_file:
                binary_data = image_file.read()
                self.last_uploaded_file = binary_data
            return binary_data
        except FileNotFoundError:
            print("Error: Image file not found.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None


#####################################
# ୧‿̩͙ ˖︵ ꕀ⠀ ♱ Profil ♱⠀ ꕀ ︵˖ ‿̩͙୨#
#####################################

class Profil(tk.Frame):
    """
    Stellt die Profilansicht eines Benutzers bereit, einschließlich Anzeige und
    Verwaltung der Benutzerinformationen.

    Diese Klasse repräsentiert die Profilseite einer Anwendung und bietet
    Funktionen zur Anzeige von Benutzerinformationen, zur Seitennavigation und
    zur Aktualisierung der angezeigten Inhalte. Sie verwaltet verschiedene
    grafische Elemente wie Labels und Buttons, um eine benutzerfreundliche
    Schnittstelle zu bieten.

    :ivar profil_frame: Hauptcontainer für die Anzeige der Benutzerprofilelemente.
    :type profil_frame: tk.Frame
    :ivar imglogin: Bild für den Login-Button.
    :type imglogin: tk.PhotoImage
    :ivar imgmainpage: Bild für den Hauptseiten-Button.
    :type imgmainpage: tk.PhotoImage
    :ivar imgProfileTest: Bild für den Benutzerprofil-Button.
    :type imgProfileTest: tk.PhotoImage
    :ivar imghelp: Bild für den Hilfe-Button.
    :type imghelp: tk.PhotoImage
    :ivar username: Label zur Anzeige des Benutzernamens.
    :type username: tk.Label
    :ivar vorname: Label zur Anzeige des Vornamens.
    :type vorname: tk.Label
    :ivar nachname: Label zur Anzeige des Nachnamens.
    :type nachname: tk.Label
    :ivar usergruppen: Label zur Anzeige der Benutzergruppen.
    :type usergruppen: tk.Label
    :ivar useremail: Label zur Anzeige der E-Mail-Adresse.
    :type useremail: tk.Label
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        root_path = os.path.dirname(os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir)))
        self.configure(bg='white')

        def update_label():

            global user_stuff
            user_stuff = "", "", "", ""
            while True:

                user_stuff = lookup_user_stuff()
                if user_stuff[0] == "" or user_stuff[0] == None:
                    time.sleep(0.3)
                    continue

                else:
                    break

            # Header für die Hauptseite
            header = ttk.Label(self, text="Profil", anchor="center", style="Header.TLabel")
            header.place(relx=0, rely=0, relwidth=1, relheight=0.15)

            # Seitennavigation und laden der Bilder für Buttons
            verzeichniss = tk.Frame(self, bg=ThemeManager.SRH_Grey)
            verzeichniss.place(relx=0, rely=0.15, relwidth=0.15, relheight=0.85)
            self.profil_frame = tk.Frame(self, bg='white')

            self.imglogin = tk.PhotoImage(
                file=root_path + "/gui/assets/Closeicon.png")
            self.imgmainpage = tk.PhotoImage(
                file=root_path + "/gui/assets/backtosite_icon.png")
            self.imgProfileTest = tk.PhotoImage(file=root_path + "/gui/assets/profile.png")
            self.imghelp = tk.PhotoImage(file=root_path + "/gui/assets/helpicon.png")

            # Positionierung der Buttons
            login = ctk.CTkButton(header, image=self.imglogin, fg_color=ThemeManager.SRH_Orange,
                                  bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                                  hover=True, hover_color='#e25a1f', text="",
                                  command=lambda: controller.show_frame(LogInWindow))

            mainpage = ctk.CTkButton(header, image=self.imgmainpage, fg_color=ThemeManager.SRH_Orange,
                                     bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                                     hover=True, hover_color='#e25a1f', text="",
                                     command=lambda: controller.show_frame(MainPage))

            help = ctk.CTkButton(header, image=self.imghelp, fg_color=ThemeManager.SRH_Orange,
                                 bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                                 hover=True, hover_color='#e25a1f', text="",
                                 command=lambda: controller.show_frame(Help))

            # Seiteninhalt
            profilbild = tk.Button(self.profil_frame, image=self.imgProfileTest, bd=0, bg='white',
                                   command=lambda: controller.show_frame(MainPage))
            username = tk.Label(self.profil_frame, text="Username", bd=0, bg='white', fg='#6F6C6C',
                                font=("Poppins", 15))
            self.username = tk.Label(self.profil_frame, text=" ", bd=0, bg='white', fg='black', font=("Poppins", 18))

            vorname = tk.Label(self.profil_frame, text="Vorname", bd=0, bg='white', fg='#6F6C6C', font=("Poppins", 15))
            self.vorname = tk.Label(self.profil_frame, text=user_stuff[1] if user_stuff[1] else "", bd=0, bg='white',
                                    fg='black', font=("Poppins", 18))

            nachname = tk.Label(self.profil_frame, text="Nachname", bd=0, bg='white', fg='#6F6C6C',
                                font=("Poppins", 15))
            self.nachname = tk.Label(self.profil_frame, text=user_stuff[2] if user_stuff[2] else "", bd=0, bg='white',
                                     fg='black', font=("Poppins", 18))

            gruppen = tk.Label(self.profil_frame, text="Gruppen", bd=0, bg='white', fg='#6F6C6C', font=("Poppins", 15))
            self.usergruppen = tk.Label(self.profil_frame, text=user_stuff[3] if user_stuff[3] else "", bd=0,
                                        bg='white', fg='black', font=("Poppins", 18))

            email = tk.Label(self.profil_frame, text="Email", bd=0, bg='white', fg='#6F6C6C', font=("Poppins", 15))
            self.useremail = tk.Label(self.profil_frame, text="xxx@srhk.de", bd=0, bg='white', fg='black',
                                      font=("Poppins", 18))

            rechte = tk.Label(self.profil_frame, text="Rechte", bd=0, bg='white', fg='#6F6C6C', font=("Poppins", 15))
            rechte_frame = tk.Frame(self.profil_frame, bg='#D9D9D9')
            adminrechte = tk.Label(self.profil_frame, text="Admin", bd=0, bg='white',
                                   fg='black' if user_stuff[0][0] == "admin" else '#6F6C6C', font=("Poppins", 18))
            ausbilderrechte = tk.Label(self.profil_frame, text="Ausbilder", bd=0, bg='white',
                                       fg='black' if user_stuff[0][0] == "admin" else '#6F6C6C', font=("Poppins", 18))
            userrechte = tk.Label(self.profil_frame, text="Schüler", bd=0, bg='white',
                                  fg='black' if user_stuff[0][0] == 'user' else '#6F6C6C', font=("Poppins", 18))

            # Seitennavigations-Buttons für Benutzer, Admin, Statistiken und Einstellungen
            user_button = tk.Button(verzeichniss, text="User", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                    font=("Inter", 20, 'bold'),
                                    command=lambda: controller.show_frame(Profil))

            admin_button = tk.Button(verzeichniss, text="Administration", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                     font=("Inter", 20, 'bold'),
                                     command=lambda: controller.show_frame(Admin))

            stats_button = tk.Button(verzeichniss, text="Statistiken", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                     font=("Inter", 20, 'bold'),
                                     command=lambda: controller.show_frame(Stats))

            einstellungen_button = tk.Button(verzeichniss, text="Einstellungen", bd=0, bg=ThemeManager.SRH_Grey,
                                             fg='black',
                                             font=("Inter", 20, 'bold'),
                                             command=lambda: controller.show_frame(Einstellungen))
            verzeichniss_help_button = tk.Button(verzeichniss, text="Hilfe", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                                 font=("Inter", 20, 'bold'),
                                                 command=lambda: controller.show_frame(Help))

            ###### Plazierung #######
            user_button.pack(pady=10, anchor='w')
            admin_button.pack(pady=10, anchor='w')
            stats_button.pack(pady=10, anchor='w')
            einstellungen_button.pack(pady=10, anchor='w')
            verzeichniss_help_button.pack(pady=10, anchor='w')

            login.place(relx=0.95, rely=0.5, anchor="center")
            mainpage.place(relx=0.90, rely=0.5, anchor="center")
            help.place(relx=0.85, rely=0.5, anchor="center")

            profilbild.place(x=0, y=0)

            username.place(x=499, y=10)
            self.username.place(x=502, y=40)

            vorname.place(x=499, y=90)
            self.vorname.place(x=502, y=120)

            nachname.place(x=499, y=170)
            self.nachname.place(x=502, y=200)

            gruppen.place(x=499, y=250)
            self.usergruppen.place(x=502, y=280)

            email.place(x=0, y=500)
            self.useremail.place(x=3, y=525)

            rechte.place(x=0, y=570)
            rechte_frame.place(x=3, y=605, width=1, height=80)
            adminrechte.place(x=13, y=590)
            ausbilderrechte.place(x=13, y=630)
            userrechte.place(x=13, y=670)

            self.profil_frame.place(relx=0.21, rely=0.15, relwidth=1, relheight=0.85)

        thread = threading.Thread(target=update_label, daemon=True)
        thread.start()


##############################################
# ୧‿̩͙ ˖︵ ꕀ⠀ ♱ Admin - Tabelle ♱⠀ ꕀ ︵˖ ‿̩͙୨#
##############################################

class Admin(tk.Frame):
    """
    Die Klasse Admin erstellt die Administrationsseite mit Navigation, Such- und Hinzufügefunktionen
    sowie einer Tabelle zur Anzeige von Benutzerdaten.
    """

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.root_path = os.path.dirname(os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir)))
        self.configure(bg='white')
        self.tabelle_frame = tk.Frame(self, bg='white')
        self.tree = ttk.Treeview(self.tabelle_frame, columns=("c1", "c2", "c3", "c4"), show="headings", height=5)

        # Initialisiere GUI-Komponenten
        self.initialize_header()
        self.initialize_navigation()
        self.initialize_table_frame()

    def initialize_header(self):
        """Erstellt und positioniert den Header-Bereich der Seite."""
        header = ttk.Label(self, text="Administration", anchor="center", style="Header.TLabel")
        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)

        self.imglogin = tk.PhotoImage(file=self.root_path + "/gui/assets/Closeicon.png")
        self.imgmainpage = tk.PhotoImage(file=self.root_path + "/gui/assets/backtosite_icon.png")
        self.imghelp = tk.PhotoImage(file=self.root_path + "/gui/assets/helpicon.png")

        login = ctk.CTkButton(header, image=self.imglogin, fg_color=ThemeManager.SRH_Orange,
                              bg_color=ThemeManager.SRH_Orange,
                              corner_radius=40, height=10, width=10, hover=True, hover_color='#e25a1f', text="",
                              command=lambda: self.controller.show_frame(LogInWindow))
        mainpage = ctk.CTkButton(header, image=self.imgmainpage, fg_color=ThemeManager.SRH_Orange,
                                 bg_color=ThemeManager.SRH_Orange,
                                 corner_radius=40, height=10, width=10, hover=True, hover_color='#e25a1f', text="",
                                 command=lambda: self.controller.show_frame(MainPage))
        help_button = ctk.CTkButton(header, image=self.imghelp, fg_color=ThemeManager.SRH_Orange,
                                    bg_color=ThemeManager.SRH_Orange,
                                    corner_radius=40, height=10, width=10, hover=True, hover_color='#e25a1f', text="",
                                    command=lambda: self.controller.show_frame(Help))

        login.place(relx=0.95, rely=0.5, anchor="center")
        mainpage.place(relx=0.90, rely=0.5, anchor="center")
        help_button.place(relx=0.85, rely=0.5, anchor="center")

    def initialize_navigation(self):
        """Erstellt und positioniert die Navigationsleiste."""
        verzeichniss = tk.Frame(self, bg=ThemeManager.SRH_Grey)

        buttons = [
            ("User", Profil),
            ("Administration", Admin),
            ("Statistiken", Stats),
            ("Einstellungen", Einstellungen),
            ("Hilfe", Help),
        ]

        for text, frame in buttons:
            button = tk.Button(verzeichniss, text=text, bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                               font=("Inter", 20, 'bold'),
                               command=lambda frame=frame: self.controller.show_frame(frame))
            button.pack(pady=10, anchor='w')

        verzeichniss.place(relx=0, rely=0.15, relwidth=0.15, relheight=0.85)

    def initialize_table_frame(self):
        """Erstellt und positioniert die Tabelle und die zugehörigen Bedienelemente."""

        self.imgSuche = load_image(self.root_path + "/gui/assets/Search.png")
        self.imgHinzufugen = load_image(self.root_path + "/gui/assets/Adding_Icon.png")

        suche_entry = ctk.CTkEntry(self.tabelle_frame, corner_radius=8, fg_color="#D9D9D9", text_color="black",
                                   border_width=0, font=("Inter", 12))

        suche_entry.bind("<Return>", lambda event: print("ersetz mich"))

        suche_button = ctk.CTkButton(self.tabelle_frame, image=self.imgSuche, corner_radius=8, border_width=0,
                                     fg_color="transparent", hover_color='#D9D9D9',
                                     command=lambda: print(f"nach {suche_entry.get()} gesucht"))
        Hinzufugen_button = tk.Button(self.tabelle_frame, image=self.imgHinzufugen, bd=0, bg='white',
                                      command=self.open_empty_user)

        suche_entry.place(relx=0.108, rely=0.1, relwidth=0.33, relheight=0.04)
        suche_button.place(relx=0.075, rely=0.1, relheight=0.04, relwidth=0.028)
        Hinzufugen_button.place(x=1280, y=100)

        self.initialize_table()
        self.tabelle_frame.place(relx=0.15, rely=0.15, relwidth=0.85, height=1000)

    def initialize_table(self):
        """Erstellt und konfiguriert die Tabelle zur Anzeige von Benutzerdaten."""
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Inter", 12), background="#D9D9D9", foreground="#6E6893")
        style.configure("Treeview", font=("Arial", 11), rowheight=35, background="white", foreground="black")
        style.map("Treeview", background=[("selected", "#D9D9D9")], foreground=[("selected", "black")])
        style.configure("evenrow.Treeview", background="#f2f2f2")
        style.configure("oddrow.Treeview", background="white")

        scroll = ctk.CTkScrollbar(self.tabelle_frame, button_color=ThemeManager.SRH_Grey,
                                  orientation="vertical", command=self.tree.yview, height=600)
        self.tree.configure(yscrollcommand=scroll.set)

        headers = fetch_headers("benutzer", ["Passwort"])
        data = fetch_tables("benutzer", ["Passwort"])

        self.tree["columns"] = headers
        for header in headers:
            self.tree.column(header, anchor='center', width=100)
            self.tree.heading(header, text=header)

        for i, row in enumerate(data):
            formatted_row = [value if value is not None else "-" for value in row]
            self.tree.insert("", "end", values=formatted_row, tags=("even" if i % 2 == 0 else "odd"))

        self.tree.tag_configure("even", background="#f7f7f7")
        self.tree.tag_configure("odd", background="white")

        self.tree.place(x=120, y=160, width=1280, height=600)
        scroll.place(x=1400, y=160)

        self.tree.bind("<Double-1>", self.on_user_select)

    def open_empty_user(self):
        """Öffnet ein Fenster zum Hinzufügen eines neuen Benutzers."""
        self.open_admin_user_page()
        self.update_admin_data(['', '', '', '', '', '', ''])

    def open_admin_user_page(self):
        """Öffnet die Detailansicht für einen Benutzer."""
        root_path = os.path.dirname(os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir)))
        admin_user_page = tk.Toplevel()  # root
        admin_user_page.title("Benutzer verwalten")

        # Fenstergröße
        window_width = 1204
        window_height = 853

        # Bildschirmgröße abrufen
        screen_width = admin_user_page.winfo_screenwidth()
        screen_height = admin_user_page.winfo_screenheight()

        # Position berechnen
        position_x = int((screen_width / 2) - (window_width / 2))
        position_y = int((screen_height / 2) - (window_height / 2))

        # Fenster positionieren
        admin_user_page.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
        admin_user_page.configure(bg='white')
        admin_user_page.configure(bg='white')

        admin_user_page.grab_set()

        admin_user_page.configure(bg='white')

        def update_label():

            global user_stuff
            user_stuff = "", "", "", ""
            while True:

                user_stuff = lookup_user_stuff()
                if user_stuff[0] == "" or user_stuff[0] == None:
                    time.sleep(0.3)
                    continue

                else:
                    break

        # Header für die Hauptseite
        header = ttk.Label(admin_user_page, text="Profil verwalten", anchor="center", style="Header.TLabel")
        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)

        # Seitennavigation und laden der Bilder für Buttons
        self.admin_profil_frame = tk.Frame(admin_user_page, bg='white')

        self.imglogin = tk.PhotoImage(
            file=root_path + "/gui/assets/Closeicon.png")
        self.imgmainpage = tk.PhotoImage(
            file=root_path + "/gui/assets/backtosite_icon.png")
        self.imgProfileTest = tk.PhotoImage(file=root_path + "/gui/assets/profile.png")
        self.imghelp = tk.PhotoImage(file=root_path + "/gui/assets/helpicon.png")
        self.aktualisieren_img = load_image(root_path + "/gui/assets/Button_Aktualisieren.png")

        # Seiteninhalt

        profilbild = tk.Button(self.admin_profil_frame, image=self.imgProfileTest, bd=0, bg='white',
                               command=lambda: self.controller.show_frame(MainPage))
        admin_username = tk.Label(self.admin_profil_frame, text="Username", bd=0, bg='white',
                                  fg='#6F6C6C',
                                  font=("Poppins", 15))
        self.admin_username = tk.Entry(self.admin_profil_frame, text=" ", bd=0, bg='white', fg='black',
                                       font=("Poppins", 18))

        admin_vorname = tk.Label(self.admin_profil_frame, text="Vorname", bd=0, bg='white',
                                 fg='#6F6C6C',
                                 font=("Poppins", 15))
        self.admin_vorname = tk.Entry(self.admin_profil_frame,
                                      text=user_stuff[1] if user_stuff[1] else "", bd=0,
                                      bg='white',
                                      fg='black', font=("Poppins", 18))

        admin_nachname = tk.Label(self.admin_profil_frame, text="Nachname", bd=0, bg='white',
                                  fg='#6F6C6C',
                                  font=("Poppins", 15))
        self.admin_nachname = tk.Entry(self.admin_profil_frame,
                                       text=user_stuff[2] if user_stuff[2] else "", bd=0,
                                       bg='white',
                                       fg='black', font=("Poppins", 18))

        admin_gruppen = tk.Label(self.admin_profil_frame, text="Gruppen", bd=0, bg='white',
                                 fg='#6F6C6C',
                                 font=("Poppins", 15))
        self.admin_gruppen = tk.Entry(self.admin_profil_frame,
                                      text=user_stuff[3] if user_stuff[3] else "", bd=0,
                                      bg='white', fg='black', font=("Poppins", 18))

        admin_email = tk.Label(self.admin_profil_frame, text="Email", bd=0, bg='white', fg='#6F6C6C',
                               font=("Poppins", 15))
        self.admin_email = tk.Entry(self.admin_profil_frame, text="@srhk.de", bd=0, bg='white',
                                    fg='black',
                                    font=("Poppins", 18))

        rechte = tk.Label(self.admin_profil_frame, text="Rechte", bd=0, bg='white', fg='#6F6C6C',
                          font=("Poppins", 15))
        rechte_frame = tk.Frame(self.admin_profil_frame, bg='#D9D9D5')  # statt 5 -> 9
        admin_adminrechte = tk.Label(self.admin_profil_frame, text="Admin", bd=0, bg='white',
                                     fg='black' if user_stuff[0][0] == "admin" else '#6F6C6C',
                                     font=("Poppins", 18))
        admin_ausbilderrechte = tk.Label(self.admin_profil_frame, text="Ausbilder", bd=0, bg='white',
                                         fg='black' if user_stuff[0][0] == "admin" else '#6F6C6C',
                                         font=("Poppins", 18))
        admin_userrechte = tk.Label(self.admin_profil_frame, text="Schüler", bd=0, bg='white',
                                    fg='black' if user_stuff[0][0] == 'user' else '#6F6C6C',
                                    font=("Poppins", 18))

        # Speicherbutton
        def admin_button_click():
            admin_user_page.destroy()
            messagebox.showinfo("Erfolgreich", "User erfolgreich gespeichert")

        admin_speichern_button = ctk.CTkButton(admin_user_page, text="Speichern", fg_color=ThemeManager.SRH_Orange,
                                               text_color="white", font=('Inter', 20, 'bold'),
                                               corner_radius=8, hover=True,
                                               hover_color=ThemeManager.SRH_DarkBlau,
                                               command=admin_button_click, width=137, height=44)
        admin_speichern_button.place(x=1000, y=800)

        # Löschbutton
        def admin_delete_click():
            confirm = messagebox.askokcancel("Löschen", "User löschen?")

            if confirm:  # Wenn der Benutzer "OK" klickt
                admin_user_page.destroy()
                messagebox.showinfo("Erfolgreich", "User erfolgreich gelöscht")
            else:  # Wenn der Benutzer "Abbrechen" klickt
                messagebox.showinfo("Abgebrochen", "Löschen abgebrochen, User wurde nicht gelöscht.")

        admin_delete_button = ctk.CTkButton(admin_user_page, text="Löschen", fg_color=ThemeManager.SRH_DarkBlau,
                                            text_color="white", font=('Inter', 20, 'bold'),
                                            corner_radius=8, hover=True,
                                            hover_color=ThemeManager.SRH_Orange,
                                            command=admin_delete_click, width=137, height=44)
        admin_delete_button.place(x=830, y=800)

        adminpage = ctk.CTkButton(admin_user_page, text="↩", fg_color='white', text_color=ThemeManager.SRH_Grey,
                                  width=5,
                                  font=("Inter", 50, 'bold'), corner_radius=8, hover=False,
                                  command=admin_user_page.destroy)
        adminpage.place(relx=0.05, rely=0.16, anchor='nw')

        ###### Plazierung #######

        profilbild.place(x=0, y=0)

        admin_username.place(x=499, y=10)
        self.admin_username.place(x=502, y=40)

        admin_vorname.place(x=499, y=90)
        self.admin_vorname.place(x=502, y=120)

        admin_nachname.place(x=499, y=170)
        self.admin_nachname.place(x=502, y=200)

        admin_gruppen.place(x=499, y=250)
        self.admin_gruppen.place(x=502, y=280)

        admin_email.place(x=0, y=500)
        self.admin_email.place(x=3, y=525)

        rechte.place(x=0, y=570)
        rechte_frame.place(x=3, y=605, width=1, height=80)
        admin_adminrechte.place(x=13, y=590)
        admin_ausbilderrechte.place(x=13, y=630)
        admin_userrechte.place(x=13, y=670)

        self.admin_profil_frame.place(relx=0.1, rely=0.15, relwidth=2, relheight=0.85)

        thread = threading.Thread(target=update_label, daemon=True)
        thread.start()

    def update_admin_data(self, data):
        """ 
        Aktualisiert die Admin-Daten in der Benutzeroberfläche.
        übernimmt die Daten der Datenbank in die Label-Objekte
        """
        self.admin_username.delete(0, tk.END)
        self.admin_username.insert(0, data[1])

        self.admin_vorname.delete(0, tk.END)
        self.admin_vorname.insert(0, data[2])

        self.admin_nachname.delete(0, tk.END)
        self.admin_nachname.insert(0, data[3])

        self.admin_gruppen.delete(0, tk.END)
        self.admin_gruppen.insert(0, data[4])

        self.admin_email.delete(0, tk.END)
        self.admin_email.insert(0, data[0])

    def showDetails1(self, selected_User):
        data = self.tree.item(selected_User, "values")
        print(f"Daten des ausgewählten Items: {data}")
        self.open_admin_user_page()
        self.update_admin_data(data)

    def on_user_select(self, event):
        try:
            selected_User = self.tree.focus()
            print(f"Ausgewählter User: {selected_User}")
            if selected_User:
                self.showDetails1(selected_User)
        except Exception as e:
            print(f"Fehler bei der Auswahl {e}")


##########################################
# ୧‿̩͙ ˖︵ ꕀ⠀ ♱ Statistiken ♱⠀ ꕀ ︵˖ ‿̩͙୨#
##########################################

class Stats(tk.Frame):
    """
    Stellt eine GUI für Statistiken bereit.

    Diese Klasse repräsentiert eine Seite innerhalb einer GUI-Anwendung, die dem Anzeigen von Statistiken
    dient. Es wird eine Kopfzeile, eine vertikale Navigationsleiste sowie verschiedene interaktive
    Buttons bereitgestellt. Die Navigationsleiste ermöglicht den Wechsel zwischen verschiedenen
    Ansichten der Anwendung.

    :ivar stats_frame: Hauptinhaltbereich für die Statistikseite.
    :ivar imglogin: Bild für den Login-Button.
    :ivar imgmainpage: Bild für den Zurück-zur-Hauptseite-Button.
    :ivar imghelp: Bild für den Hilfe-Button.
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        root_path = os.path.dirname(os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir)))
        self.configure(bg='white')

        # Header-Label für die Statistikseite
        header = ttk.Label(self, text="Statistiken", anchor="center", style="Header.TLabel")
        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)

        # Navigationsleiste auf der linken Seite
        verzeichniss = tk.Frame(self, bg=ThemeManager.SRH_Grey)
        self.stats_frame = tk.Frame(self, bg='white')

        # Bilder für die Login- und Hauptseite-Buttons laden
        self.imglogin = tk.PhotoImage(
            file=root_path + "/gui/assets/Closeicon.png")
        self.imgmainpage = tk.PhotoImage(
            file=root_path + "/gui/assets/backtosite_icon.png")
        self.imghelp = tk.PhotoImage(file=root_path + "/gui/assets/helpicon.png")

        # Header-Navigationsbuttons (Login und Hauptseite), Platzierung der Header-Buttons
        login = ctk.CTkButton(header, image=self.imglogin, fg_color=ThemeManager.SRH_Orange,
                              bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                              hover=True, hover_color='#e25a1f', text="",
                              command=lambda: controller.show_frame(LogInWindow))

        mainpage = ctk.CTkButton(header, image=self.imgmainpage, fg_color=ThemeManager.SRH_Orange,
                                 bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                                 hover=True, hover_color='#e25a1f', text="",
                                 command=lambda: controller.show_frame(MainPage))

        help = ctk.CTkButton(header, image=self.imghelp, fg_color=ThemeManager.SRH_Orange,
                             bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                             hover=True, hover_color='#e25a1f', text="",
                             command=lambda: controller.show_frame(Help))

        login.place(relx=0.95, rely=0.5, anchor="center")
        mainpage.place(relx=0.90, rely=0.5, anchor="center")
        help.place(relx=0.85, rely=0.5, anchor="center")

        # Linksseitige Navigationsbutton für verschiedene Ansichten
        user_button = tk.Button(verzeichniss, text="User", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=lambda: controller.show_frame(Profil))
        user_button.pack(pady=10, anchor='w')

        admin_button = tk.Button(verzeichniss, text="Administration", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                 font=("Inter", 20, 'bold'),
                                 command=lambda: controller.show_frame(Admin))
        admin_button.pack(pady=10, anchor='w')

        stats_button = tk.Button(verzeichniss, text="Statistiken", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                 font=("Inter", 20, 'bold'),
                                 command=lambda: controller.show_frame(Stats))
        stats_button.pack(pady=10, anchor='w')

        einstellungen_button = tk.Button(verzeichniss, text="Einstellungen", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                         font=("Inter", 20, 'bold'),
                                         command=lambda: controller.show_frame(Einstellungen))
        einstellungen_button.pack(pady=10, anchor='w')

        verzeichniss_help_button = tk.Button(verzeichniss, text="Hilfe", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                             font=("Inter", 20, 'bold'),
                                             command=lambda: controller.show_frame(Help))
        verzeichniss_help_button.pack(pady=10, anchor='w')

        # Platzierung des Hauptinhaltsbereichs und der Navigationsleiste
        self.stats_frame.place(relx=0.21, rely=0.15, relwidth=1, relheight=0.85)
        verzeichniss.place(relx=0, rely=0.15, relwidth=0.15, relheight=0.85)


############################################
# ୧‿̩͙ ˖︵ ꕀ⠀ ♱ Einstellungen ♱⠀ ꕀ ︵˖ ‿̩͙୨#
############################################

class Einstellungen(tk.Frame):
    """
    Die Klasse Einstellungen stellt eine grafische Benutzerschnittstelle für die
    Einstellungen der Anwendung bereit.

    Sie enthält Widgets wie Header-Labels, Navigationsbuttons, Dropdown-Menüs und
    verschiedene Schaltflächen, mit denen der Benutzer zwischen verschiedenen
    Abschnitten navigieren und Einstellungen anpassen kann. Zusätzlich unterstützt
    sie die Umschaltung zwischen Light- und Darkmode, inklusive dynamischer
    Anpassung der Benutzeroberfläche.

    :ivar header: Das Header-Label der Seite „Einstellungen“, das als Titel
        dient.
    :type header: ttk.Label
    :ivar imglogin: Speichert das Bild für den Login-Navigationsbutton.
    :type imglogin: tk.PhotoImage
    :ivar imgmainpage: Speichert das Bild für den Mainpage-Navigationsbutton.
    :type imgmainpage: tk.PhotoImage
    :ivar imghelp: Speichert das Bild für den Hilfenavigationsbutton.
    :type imghelp: tk.PhotoImage
    :ivar einstellung_frame: Der Rahmen, der den Hauptinhalt der Einstellungen
        darstellt.
    :type einstellung_frame: tk.Frame
    :ivar switch_value: Boolean-Wert, der den aktuellen Status der
        Theme-Umschaltung (Light- oder Darkmode) speichert.
    :type switch_value: bool
    :ivar light: Bild für die Light-Theme-Schalterposition.
    :type light: tk.PhotoImage
    :ivar dark: Bild für die Dark-Theme-Schalterposition.
    :type dark: tk.PhotoImage
    """

    def __init__(self, parent, controller):
        super().__init__()
        root_path = os.path.dirname(os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir)))
        tk.Frame.__init__(self, parent)

        self.configure(bg='white')
        self.switch_value = True

        # Layout Festlegung der flexiblen Skalierung der Einstellungen
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)

        # Header-Label für die Seite "Einstellungen"
        self.header = ttk.Label(self, text="Einstellungen", anchor="center", style="Header.TLabel")
        self.header.place(relx=0, rely=0, relwidth=1, relheight=0.15)

        # Seitenmenü (Verzeichnis) und Hauptinhaltsbereich (Einstellung)
        verzeichniss = tk.Frame(self, bg=ThemeManager.SRH_Grey)
        self.einstellung_frame = tk.Frame(self, bg='white')

        ttk.Label(self, text="Einstellungen", anchor="center", style="Einstellungen.TLabel")

        # Navigationsbuttons im Header (Login und Mainpage)
        self.imglogin = tk.PhotoImage(
            file=root_path + "/gui/assets/Closeicon.png")
        self.imgmainpage = tk.PhotoImage(
            file=root_path + "/gui/assets/backtosite_icon.png")
        self.imghelp = tk.PhotoImage(file=root_path + "/gui/assets/helpicon.png")

        login = ctk.CTkButton(self.header, image=self.imglogin, fg_color=ThemeManager.SRH_Orange,
                              bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                              hover=True, hover_color='#e25a1f', text="",
                              command=lambda: controller.show_frame(LogInWindow))

        mainpage = ctk.CTkButton(self.header, image=self.imgmainpage, fg_color=ThemeManager.SRH_Orange,
                                 bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                                 hover=True, hover_color='#e25a1f', text="",
                                 command=lambda: controller.show_frame(MainPage))

        help = ctk.CTkButton(self.header, image=self.imghelp, fg_color=ThemeManager.SRH_Orange,
                             bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                             hover=True, hover_color='#e25a1f', text="",
                             command=lambda: controller.show_frame(Help))

        login.place(relx=0.95, rely=0.5, anchor="center")
        mainpage.place(relx=0.90, rely=0.5, anchor="center")
        help.place(relx=0.85, rely=0.5, anchor="center")

        user_button = tk.Button(verzeichniss, text="User", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=lambda: controller.show_frame(Profil))
        user_button.pack(pady=10, anchor='w')

        admin_button = tk.Button(verzeichniss, text="Administration", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                 font=("Inter", 20, 'bold'),
                                 command=lambda: controller.show_frame(Admin))
        admin_button.pack(pady=10, anchor='w')

        stats_button = tk.Button(verzeichniss, text="Statistiken", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                 font=("Inter", 20, 'bold'),
                                 command=lambda: controller.show_frame(Stats))
        stats_button.pack(pady=10, anchor='w')

        einstellungen_button = tk.Button(verzeichniss, text="Einstellungen", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                         font=("Inter", 20, 'bold'),
                                         command=lambda: controller.show_frame(Einstellungen))
        einstellungen_button.pack(pady=10, anchor='w')

        verzeichniss_help_button = tk.Button(verzeichniss, text="Hilfe", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                             font=("Inter", 20, 'bold'),
                                             command=lambda: controller.show_frame(Help))
        verzeichniss_help_button.pack(pady=10, anchor='w')

        # Platziung des Verzeichnisses (Navigationsleiste)
        verzeichniss.place(relx=0, rely=0.15, relwidth=0.15, relheight=0.85)

        # Seiteninhalt

        # Label für die Details-Sektion
        details_label = tk.Label(self.einstellung_frame, text="Details", bg='white', fg='#858383', font=("Inter", 19))
        details_label.place(relx=0.0, rely=0.15)

        # Dropdown für Exportformat
        format_drop = tk.Button(self.einstellung_frame, text="Format exportieren in", bd=0, bg='white',
                                fg=ThemeManager.SRH_Grey,
                                font=("Inter", 20, 'bold'),
                                command=lambda: controller.show_frame())

        format_drop = tk.Button(self.einstellung_frame, text="Format exportieren in", bd=0, bg='white', fg='black',
                                font=("Inter", 20, 'bold'),
                                command=lambda: controller.show_frame())
        format_drop = tk.Button(self.einstellung_frame, text="Format exportieren in ↴", bd=1, bg='white', fg='black',
                                font=("Inter", 12),
                                command=lambda: show_dropdown())  # Button öffnet Dropdown-Menü
        format_drop.place(relx=0.01, rely=0.20)

        # Funktion zur Anzeige des Dropdown-Menüs für Exportoptionen
        def show_dropdown():
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=1, bg='white', fg='black')
            dropdown_menu.add_command(label="→ Excel", command=lambda: print("Excel ausgewählt"))
            dropdown_menu.add_command(label="→ SQL", command=lambda: print("SQL ausgewählt"))
            dropdown_menu.add_command(label="→ CSS", command=lambda: print("CSS ausgewählt"))
            dropdown_menu.add_command(label="→ Andere", command=lambda: print("Andere ausgewählt"))

            dropdown_menu.post(format_drop.winfo_rootx(), format_drop.winfo_rooty() + format_drop.winfo_height())

        # Darstellung Label
        darstellung_label = tk.Label(self.einstellung_frame, text="Darstellung", bg='white', fg='#858383',
                                     font=("Inter", 19))
        darstellung_label.place(relx=0.0, rely=0.32)

        # Bildvariablen zur Theme-Umschaltung
        try:
            self.light = tk.PhotoImage(file=root_path + "/gui/assets/switchoff.png")
            self.dark = tk.PhotoImage(file=root_path + "/gui/assets/switchon.png")
        except tk.EXCEPTION as e:
            print(f"Fehler beim laden der Bilder: {e}")
            return  # Beende falls die Bilder nicht geladen werden können

        def toggle():
            if self.switch_value:
                apply_darkmode()
                self.switch.config(image=self.dark, bg="black", activebackground="black")
                self.switch_value = False
            else:
                apply_lightmode()
                self.switch.config(image=self.light, bg="white", activebackground="white")
                self.switch_value = True

        # Funktion zum Anwenden des Darkmode
        def apply_darkmode():
            self.config(bg=ThemeManager.Darkmode_Black)
            self.einstellung_frame.config(bg=ThemeManager.Darkmode_Black)
            verzeichniss.config(bg=ThemeManager.Darkmode_Grey)
            user_button.config(bg=ThemeManager.Darkmode_Grey, fg="white")
            admin_button.config(bg=ThemeManager.Darkmode_Grey, fg="white")
            stats_button.config(bg=ThemeManager.Darkmode_Grey, fg="white")
            einstellungen_button.config(bg=ThemeManager.Darkmode_Grey, fg="white")
            verzeichniss_help_button.config(bg=ThemeManager.Darkmode_Grey, fg="white")

            addSpalten_button.config(bg=ThemeManager.Darkmode_Black, fg="white")
            addTyp_button.config(bg=ThemeManager.Darkmode_Black, fg="white")
            addGerat_button.config(bg=ThemeManager.Darkmode_Black, fg="white")
            addStatus_button.config(bg=ThemeManager.Darkmode_Black, fg="white")

            details_label.config(bg=ThemeManager.Darkmode_Black, fg="white")
            darstellung_label.config(bg=ThemeManager.Darkmode_Black, fg="white")
            datenbank_label.config(bg=ThemeManager.Darkmode_Black, fg="white")

        # Funktion zum Anwenden des Lightmodes
        def apply_lightmode():
            self.config(bg="white")
            self.einstellung_frame.config(bg="white")
            verzeichniss.config(bg=ThemeManager.SRH_Grey)
            user_button.config(bg=ThemeManager.SRH_Grey, fg="black")
            admin_button.config(bg=ThemeManager.SRH_Grey, fg="black")
            stats_button.config(bg=ThemeManager.SRH_Grey, fg="black")
            einstellungen_button.config(bg=ThemeManager.SRH_Grey, fg="black")
            verzeichniss_help_button.config(bg=ThemeManager.SRH_Grey, fg="black")

            addSpalten_button.config(bg="white", fg="black")
            addTyp_button.config(bg="white", fg="black")
            addGerat_button.config(bg="white", fg="black")
            addStatus_button.config(bg="white", fg="black")

            details_label.config(bg="white", fg="black")
            darstellung_label.config(bg="white", fg="black")
            datenbank_label.config(bg="white", fg="black")

        # Button zur Umschaltung des Themes
        self.switch = tk.Button(self, image=self.light, bd=0, bg="white", activebackground="white", command=toggle)
        self.switch.place(relx=0.16, rely=0.46)

        def change_header_color(event):
            # Dropdown zur Auswahl der Header-Farbe
            selected_color = color_dropdown.get()
            if selected_color == "Orange":
                self.header.configure(background=ThemeManager.SRH_Orange)
                login.config(bg=ThemeManager.SRH_Orange)
                mainpage.config(bg=ThemeManager.SRH_Orange)
            elif selected_color == "Blau":
                self.header.configure(background=ThemeManager.SRH_Blau)
                login.config(bg=ThemeManager.SRH_Blau)
                mainpage.config(bg=ThemeManager.SRH_Blau)
            elif selected_color == "Lila":
                self.header.configure(background="#c7afe2")
                login.config(bg="#c7afe2")
                mainpage.config(bg="#c7afe2")

        # Combobox zur Auswahl der Header-Farbe
        color_options = ["Orange", "Blau", "Lila"]
        color_dropdown = ttk.Combobox(self, values=color_options, state="readonly")
        color_dropdown.set("Farbeschema")  # Default text
        color_dropdown.place(relx=0.16, rely=0.5, relwidth=0.103, relheight=0.032)  # Adjust positioning as needed
        color_dropdown.bind("<<ComboboxSelected>>", change_header_color)

        # Datenbank-Sektion und Buttons zur Verwaltung der Datenbankelemente
        datenbank_label = tk.Label(self.einstellung_frame, text="Datenbank", bg='white', fg='#858383',
                                   font=("Inter", 19))
        datenbank_label.place(relx=0.0, rely=0.59)

        def open_spalten_page():
            spalten_page = tk.Toplevel()  # root
            spalten_page.title("Spalte hinzufügen")
            spalten_page.geometry("400x200+500+300")
            spalten_page.configure(bg='white')

            spalten_page.grab_set()
            # Bilder
            self.aktualisieren_img = load_image(root_path + "/gui/assets/Button_Aktualisieren.png")
            self.upload_img = load_image(root_path + "/gui/assets/Button_Drop.png")

            # Informationen
            info_frame = tk.Frame(spalten_page, bg='white', bd=1)

            name_label = tk.Label(info_frame, text="Name", bg='white',
                                  font=("Inter", 19))
            name_entry = tk.Entry(info_frame, bg='#D9D9D9', bd=0,
                                  font=("Inter", 19, 'italic'))

            tabelle_label = tk.Label(info_frame, text="Tabelle", bg='white',
                                     font=("Inter", 19))
            tabelle_entry = tk.Entry(info_frame, bg='#D9D9D9', bd=0,
                                     font=("Inter", 19, 'italic'))

            # Buttons
            button_frame = tk.Frame(spalten_page, bg='white', bd=1)
            close_button = tk.Button(button_frame, image=self.aktualisieren_img, bd=0, bg='white',
                                     command=spalten_page.destroy)

            # Placement
            name_label.place(x=0, y=2)
            name_entry.place(x=100, y=2, width=150)

            tabelle_label.place(x=0, y=52)
            tabelle_entry.place(x=100, y=52, width=150)

            close_button.place(x=0, y=40)
            info_frame.place(x=0, y=0, width=600, height=594)
            button_frame.place(x=100, y=100, width=409, height=150)

        # Funktion zuende
        addSpalten_button = tk.Button(self.einstellung_frame, text="Spalte\t+", bd=0, bg='white', fg='black',
                                      font=("Inter", 16),
                                      command=open_spalten_page)

        addSpalten_button.place(relx=0.01, rely=0.64, relheight=0.032)

        def open_typ_page():
            typ_page = tk.Toplevel()  # root
            typ_page.title("Typ hinzufügen")
            typ_page.geometry("400x200+500+300")
            typ_page.configure(bg='white')

            # Modal-Fenster aktivieren
            typ_page.grab_set()

            # Bilder
            self.aktualisieren_img = load_image(root_path + "/gui/assets/Button_Aktualisieren.png")
            self.upload_img = load_image(root_path + "/gui/assets/Button_Drop.png")

            # Informationen
            info_frame = tk.Frame(typ_page, bg='white', bd=1)

            name_label = tk.Label(info_frame, text="Name", bg='white',
                                  font=("Inter", 19))
            name_entry = tk.Entry(info_frame, bg='#D9D9D9', bd=0,
                                  font=("Inter", 19, 'italic'))

            # Buttons
            button_frame = tk.Frame(typ_page, bg='white', bd=1)
            close_button = tk.Button(button_frame, image=self.aktualisieren_img, bd=0, bg='white',
                                     command=typ_page.destroy)

            # Placement
            name_label.place(x=0, y=2)
            name_entry.place(x=100, y=2, width=150)

            close_button.place(x=0, y=40)
            info_frame.place(x=0, y=0, width=600, height=594)
            button_frame.place(x=100, y=100, width=409, height=150)

        # Funktion zuende
        addTyp_button = tk.Button(self.einstellung_frame, text="Typ\t+", bd=0, bg='white', fg='black',
                                  font=("Inter", 16),
                                  command=open_typ_page)
        addTyp_button.place(relx=0.01, rely=0.69, relheight=0.032)

        def open_status_page():
            spalten_page = tk.Toplevel()  # root
            spalten_page.title("Status hinzufügen")
            spalten_page.geometry("400x200+500+300")
            spalten_page.configure(bg='white')

            spalten_page.grab_set()
            # Bilder
            self.aktualisieren_img = load_image(root_path + "/gui/assets/Button_Aktualisieren.png")
            self.upload_img = load_image(root_path + "/gui/assets/Button_Drop.png")

            # Informationen
            info_frame = tk.Frame(spalten_page, bg='white', bd=1)

            name_label = tk.Label(info_frame, text="Name", bg='white',
                                  font=("Inter", 19))
            name_entry = tk.Entry(info_frame, bg='#D9D9D9', bd=0,
                                  font=("Inter", 19, 'italic'))

            icon_label = tk.Label(info_frame, text="Icon", bg='white',
                                  font=("Inter", 19))
            icon_entry = tk.Entry(info_frame, bg='#D9D9D9', bd=0,
                                  font=("Inter", 19, 'italic'))

            # Buttons
            button_frame = tk.Frame(spalten_page, bg='white', bd=1)
            close_button = tk.Button(button_frame, image=self.aktualisieren_img, bd=0, bg='white',
                                     command=spalten_page.destroy)

            # Placement
            name_label.place(x=0, y=2)
            name_entry.place(x=100, y=2, width=150)
            icon_label.place(x=0, y=50)
            icon_entry.place(x=100, y=50, width=150)

            close_button.place(x=0, y=40)
            info_frame.place(x=0, y=0, width=600, height=594)
            button_frame.place(x=100, y=100, width=409, height=150)

        # Funktion zuende

        addStatus_button = tk.Button(self.einstellung_frame, text="Status\t+", bd=0, bg='white', fg='black',
                                     font=("Inter", 16),
                                     command=open_status_page)
        addStatus_button.place(relx=0.01, rely=0.74, relheight=0.032)

        addGerat_button = tk.Button(self.einstellung_frame, text="Gerät\t+", bd=0, bg='white', fg='black',
                                    font=("Inter", 16),
                                    command=lambda: controller.show_frame(Gerateansicht))
        addGerat_button.place(relx=0.01, rely=0.79, relheight=0.032)

        # Platzierung der Hauptframe-Bereiche
        self.einstellung_frame.place(relx=0.15, rely=0.15, relwidth=1, relheight=0.85)
        self.header.place(relx=0, rely=0, relwidth=1, relheight=0.15)


#########################################
# ୧‿̩͙ ˖︵ ꕀ⠀ ♱ Hilfsseite ♱⠀ ꕀ ︵˖ ‿̩͙୨#
#########################################

class Help(tk.Frame):
    """
    Stellt eine GUI für Statistiken bereit.

    Diese Klasse repräsentiert eine Seite innerhalb einer GUI-Anwendung, die dem Anzeigen von Statistiken
    dient. Es wird eine Kopfzeile, eine vertikale Navigationsleiste sowie verschiedene interaktive
    Buttons bereitgestellt. Die Navigationsleiste ermöglicht den Wechsel zwischen verschiedenen
    Ansichten der Anwendung.

    :ivar stats_frame: Hauptinhaltbereich für die Statistikseite.
    :ivar imglogin: Bild für den Login-Button.
    :ivar imgmainpage: Bild für den Zurück-zur-Hauptseite-Button.
    :ivar imghelp: Bild für den Hilfe-Button.
    """

    # from configuration import Einstellungen
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        root_path = os.path.dirname(os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir)))
        self.configure(bg='white')

        # Header-Label für die Statistikseite
        header = ttk.Label(self, text="Hilfsseite", anchor="center", style="Header.TLabel")
        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)

        # Navigationsleiste auf der linken Seite
        verzeichniss = tk.Frame(self, bg=ThemeManager.SRH_Grey)
        self.hilfe_frame = tk.Frame(self, bg='white')

        # Bilder für die Login- und Hauptseite-Buttons laden
        self.imglogin = tk.PhotoImage(file=root_path + "/gui/assets/Closeicon.png")
        self.imgmainpage = tk.PhotoImage(file=root_path + "/gui/assets/backtosite_icon.png")
        self.imghelp = tk.PhotoImage(file=root_path + "/gui/assets/helpicon.png")

        # Header-Navigationsbuttons (Login und Hauptseite), Platzierung der Header-Buttons
        login = ctk.CTkButton(header, image=self.imglogin, fg_color=ThemeManager.SRH_Orange,
                              bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                              hover=True, hover_color='#e25a1f', text="",
                              command=lambda: controller.show_frame(LogInWindow))

        mainpage = ctk.CTkButton(header, image=self.imgmainpage, fg_color=ThemeManager.SRH_Orange,
                                 bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                                 hover=True, hover_color='#e25a1f', text="",
                                 command=lambda: controller.show_frame(MainPage))

        def meme_help():
            meme_page = tk.Toplevel()  # root
            meme_page.title("Meme")
            meme_page.geometry("240x300+500+300")
            meme_page.iconbitmap(root_path + "/gui/assets/sad.ico")
            meme_page.configure(bg='white')

            meme_page.grab_set()
            # Bilder
            self.meme1 = load_image(root_path + "/gui/assets/meme1.png")

            def meme2_button_command():
                meme_page.destroy()  # Fenster schließen

                meme2_page = tk.Toplevel()  # root
                meme2_page.title("Meme")
                meme2_page.geometry("240x300+500+300")
                meme2_page.iconbitmap(root_path + "/gui/assets/sad.ico")
                meme2_page.configure(bg='white')

                meme2_page.grab_set()
                # Bilder
                self.meme2 = load_image(root_path + "/gui/assets/meme2.png")

                def meme3_button_command():
                    meme2_page.destroy()  # Fenster schließen

                    meme3_page = tk.Toplevel()  # root
                    meme3_page.title("Meme")
                    meme3_page.geometry("240x300+500+300")
                    meme3_page.iconbitmap(root_path + "/gui/assets/sad.ico")
                    meme3_page.configure(bg='white')

                    meme3_page.grab_set()
                    # Bilder
                    self.meme3 = load_image(root_path + "/gui/assets/meme3.png")

                    meme3 = tk.Label(meme3_page, image=self.meme3, bg='white')
                    meme3_button = tk.Button(meme3_page, text="Okay!", bd=0, bg='white', fg='black',
                                             command=meme3_page.destroy)  # Schließen des aktuellen Fensters
                    meme3.place(relx=0.5, rely=0.5, anchor="center")
                    meme3_button.place(relx=0.5, rely=0.96, anchor="center")

                meme2 = tk.Label(meme2_page, image=self.meme2, bg='white')
                meme2_button = tk.Button(meme2_page, text="Ja", bd=0, bg='white', fg='black',
                                         command=meme3_button_command)
                meme25_button = tk.Button(meme2_page, text="Nein", bd=0, bg='white', fg='black',
                                          command=meme3_button_command)
                meme2.place(relx=0.5, rely=0.5, anchor="center")
                meme25_button.place(relx=0.7, rely=0.96, anchor="center")
                meme2_button.place(relx=0.3, rely=0.96, anchor="center")

            meme1 = tk.Label(meme_page, image=self.meme1, bg='white')
            meme1_button = tk.Button(meme_page, text="Ich brauch aber hilfe!", bd=0, bg='white', fg='black',
                                     command=meme2_button_command)
            meme1.place(relx=0.5, rely=0.5, anchor="center")
            meme1_button.place(relx=0.5, rely=0.96, anchor="center")

        help = ctk.CTkButton(header, image=self.imghelp, fg_color=ThemeManager.SRH_Orange,
                             bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                             hover=True, hover_color='#e25a1f', text="",
                             command=meme_help)

        login.place(relx=0.95, rely=0.5, anchor="center")
        mainpage.place(relx=0.90, rely=0.5, anchor="center")
        help.place(relx=0.85, rely=0.5, anchor="center")

        # Linksseitige Navigationsbutton für verschiedene Ansichten

        user_button = tk.Button(verzeichniss, text="User", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=lambda: controller.show_frame(Profil))
        user_button.pack(pady=10, anchor='w')

        admin_button = tk.Button(verzeichniss, text="Administration", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                 font=("Inter", 20, 'bold'),
                                 command=lambda: controller.show_frame(Admin))
        admin_button.pack(pady=10, anchor='w')

        stats_button = tk.Button(verzeichniss, text="Statistiken", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                 font=("Inter", 20, 'bold'),
                                 command=lambda: controller.show_frame(Stats))
        stats_button.pack(pady=10, anchor='w')

        einstellungen_button = tk.Button(verzeichniss, text="Einstellungen", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                         font=("Inter", 20, 'bold'),
                                         command=lambda: controller.show_frame(Einstellungen))
        einstellungen_button.pack(pady=10, anchor='w')

        verzeichniss_help_button = tk.Button(verzeichniss, text="Hilfe", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                             font=("Inter", 20, 'bold'),
                                             command=lambda: controller.show_frame(Help))
        verzeichniss_help_button.pack(pady=10, anchor='w')

        # Seiteninhalt
        # help_frame ist ein scrollable Frame, Labels müssen auf dem Frame platziert werden,
        # und passend angepasst werden, damit das funktioniert (siehe Beispiel)
        help_frame = ctk.CTkScrollableFrame(self.hilfe_frame, fg_color='white', scrollbar_fg_color='white',
                                            scrollbar_button_hover_color=ThemeManager.SRH_Orange,
                                            scrollbar_button_color=ThemeManager.SRH_Grey, height=1000, width=1000)

        # Platzieren des help_frame so, dass es self.hilfe_frame vollständig abdeckt
        help_frame.place(relx=0, rely=0, relwidth=0.9, relheight=0.99)

        # Labels hinzufügen, um die Scroll-Funktion zu testen
        for i in range(50):  # 50 Labels, um eine Scrollbarkeit sicherzustellen
            label = ctk.CTkLabel(help_frame, text=f"Label {i + 1}", text_color="black")
            label.pack(pady=5, padx=5, anchor="w")

        # Beispiel
        # label = ctk.CTkLabel(help_frame, text='Test', text_color="black")
        # label.pack(pady=5, padx=5, anchor="w")
        # Erstelle die inneren Frames
        # help_main_frame = tk.Frame(help_frame, bg='green')
        # help_profile_frame = tk.Frame(help_frame, bg='yellow')
        # help_einstellung_frame = tk.Frame(help_frame, bg='blue')
        # help_gerateansicht_frame = tk.Frame(help_frame, bg='red')
        # help_gerateubersicht_frame = tk.Frame(help_frame, bg='orange')
        # help_admin_frame = tk.Frame(help_frame, bg='black')

        # Passe ggf. auch die Platzierung von self.hilfe_frame an
        self.hilfe_frame.place(relx=0.21, rely=0.15, relwidth=0.79, relheight=0.85)

        # Passe verzeichniss entsprechend an
        verzeichniss.place(relx=0, rely=0.15, relwidth=0.15, relheight=0.85)


# Funktion, wenn Bild nicht geladen werden kann
def load_image(image_path):
    if os.path.exists(image_path):
        return tk.PhotoImage(file=image_path)
    else:
        print(f"Warnung: Bild '{image_path}' nicht gefunden.")
        return None


# try:
#     app = GuiTest()
#     app.mainloop()
# except Exception as e:
#     print(f"Fehler beim Starten des Programms: {e}")

app = GuiTest()
app.mainloop()