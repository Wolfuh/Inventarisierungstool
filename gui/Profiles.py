import tkinter as tk
from tkinter import ttk, messagebox

import PIL.ImageTk
import customtkinter as ctk

import os
import sys
import time
import threading

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from db.SQLite_db import *


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
        from ThemeManager import ThemeManager
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
            self.imglogin = ctk.CTkImage(PIL.ImageTk.Image.open(root_path + "/gui/assets/Closeicon.png"))

            self.imgmainpage = ctk.CTkImage(PIL.ImageTk.Image.open(root_path + "/gui/assets/backtosite.png"))
            self.imgProfileTest = ctk.CTkImage(PIL.ImageTk.Image.open(root_path + "/gui/assets/profile.png"))
            self.imghelp = ctk.CTkImage(PIL.ImageTk.Image.open(root_path + "/gui/assets/helpicon.png"))

            # Positionierung der Buttons
            def login():
                from gui_prototyp import LogInWindow
                controller.show_frame(LogInWindow)

            login = ctk.CTkButton(header, image=self.imglogin, fg_color=ThemeManager.SRH_Orange,
                                  bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                                  hover=True, hover_color='#e25a1f', text="",
                                  command=login)

            def mainpage():
                from Mainpages import MainPage
                controller.show_frame(MainPage)

            mainpage = ctk.CTkButton(header, image=self.imgmainpage, fg_color=ThemeManager.SRH_Orange,
                                     bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                                     hover=True, hover_color='#e25a1f', text="",
                                     command=mainpage)

            def help():
                controller.show_frame(Help)

            help = ctk.CTkButton(header, image=self.imghelp, fg_color=ThemeManager.SRH_Orange,
                                 bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                                 hover=True, hover_color='#e25a1f', text="",
                                 command=help)

            # Seiteninhalt
            def profilbild():
                from Mainpages import MainPage
                controller.show_frame(MainPage)

            profilbild = tk.Button(self.profil_frame, image=self.imgProfileTest, bd=0, bg='white',
                                   command=profilbild)

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

            def user_button():
                controller.show_frame(Profil)

            user_button = tk.Button(verzeichniss, text="User", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                    font=("Inter", 20, 'bold'),
                                    command=user_button)

            def admin_button():
                controller.show_frame(Admin)

            admin_button = tk.Button(verzeichniss, text="Administration", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                     font=("Inter", 20, 'bold'),
                                     command=admin_button)

            def stats_button():
                controller.show_frame(Stats)

            stats_button = tk.Button(verzeichniss, text="Statistiken", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                     font=("Inter", 20, 'bold'),
                                     command=stats_button)

            def einstellungen():
                from configuration import Einstellungen
                controller.show_frame(Einstellungen)

            einstellungen_button = tk.Button(verzeichniss, text="Einstellungen", bd=0, bg=ThemeManager.SRH_Grey,
                                             fg='black',
                                             font=("Inter", 20, 'bold'),
                                             command=einstellungen)

            def verzeichnis_help_button():
                controller.show_frame(Help)

            verzeichniss_help_button = tk.Button(verzeichniss, text="Hilfe", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                                 font=("Inter", 20, 'bold'),
                                                 command=verzeichnis_help_button)

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


class Admin_User(tk.Frame):
    """
    Die Klasse "Admin_User" stellt das GUI für die Verwaltung eines
    Benutzerprofils zur Verfügung.

    Diese Klasse ist Teil eines größeren Desktop-Applikationslayouts
    und erlaubt es, Benutzerprofile aufzurufen, anzuzeigen und zu ändern.
    Es enthält Werkzeuge und Navigationselemente, um Informationen wie
    Benutzernamen, Vorname, Nachname, Gruppen, Rechte und E-Mail zu ändern.
    Darüber hinaus ermöglicht es die Navigation zu verschiedenen Seiten
    der Applikation wie Administration, Statistiken und Hilfeseiten.

    :ivar imglogin: Enthält das Bild für den "Abmelden"-Button.
    :ivar imgmainpage: Enthält das Bild``` fürpython den
     Button
     """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        from ThemeManager import ThemeManager
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
            header = ttk.Label(self, text="Profil verwalten", anchor="center", style="Header.TLabel")
            header.place(relx=0, rely=0, relwidth=1, relheight=0.15)

            # Seitennavigation und laden der Bilder für Buttons
            verzeichniss = tk.Frame(self, bg=ThemeManager.SRH_Grey)
            verzeichniss.place(relx=0, rely=0.15, relwidth=0.15, relheight=0.85)
            self.admin_profil_frame = tk.Frame(self, bg='white')
            from gui_prototyp import load_image
            self.imglogin = tk.PhotoImage(
                file=root_path + "/gui/assets/Closeicon.png")
            self.imgmainpage = tk.PhotoImage(
                file=root_path + "/gui/assets/backtosite_icon.png")
            self.imgProfileTest = tk.PhotoImage(file=root_path + "/gui/assets/profile.png")
            self.imghelp = tk.PhotoImage(file=root_path + "/gui/assets/helpicon.png")
            self.aktualisieren_img = load_image(root_path + "/gui/assets/Button_Aktualisieren.png")

            # Positionierung der Buttons
            def login():
                from gui_prototyp import LogInWindow
                controller.show_frame(LogInWindow)

            login = ctk.CTkButton(header, image=self.imglogin, fg_color=ThemeManager.SRH_Orange,
                                  bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                                  hover=True, hover_color='#e25a1f', text="",
                                  command=login)

            def mainpage():
                from Mainpages import MainPage
                controller.show_frame(MainPage)

            mainpage = ctk.CTkButton(header, image=self.imgmainpage, fg_color=ThemeManager.SRH_Orange,
                                     bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                                     hover=True, hover_color='#e25a1f', text="",
                                     command=mainpage)

            def help():
                controller.show_frame(Help)

            help = ctk.CTkButton(header, image=self.imghelp, fg_color=ThemeManager.SRH_Orange,
                                 bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                                 hover=True, hover_color='#e25a1f', text="",
                                 command=help)

            # Seiteninhalt

            def profilbild():
                from Mainpages import MainPage
                controller.show_frame(MainPage)

            profilbild = tk.Button(self.admin_profil_frame, image=self.imgProfileTest, bd=0, bg='white',
                                   command=profilbild)

            admin_username = tk.Label(self.admin_profil_frame, text="Username", bd=0, bg='white', fg='#6F6C6C',
                                      font=("Poppins", 15))
            self.admin_username = tk.Entry(self.admin_profil_frame, text=" ", bd=0, bg='white', fg='black',
                                           font=("Poppins", 18))

            admin_vorname = tk.Label(self.admin_profil_frame, text="Vorname", bd=0, bg='white', fg='#6F6C6C',
                                     font=("Poppins", 15))
            self.admin_vorname = tk.Entry(self.admin_profil_frame, text=user_stuff[1] if user_stuff[1] else "", bd=0,
                                          bg='white',
                                          fg='black', font=("Poppins", 18))

            admin_nachname = tk.Label(self.admin_profil_frame, text="Nachname", bd=0, bg='white', fg='#6F6C6C',
                                      font=("Poppins", 15))
            self.admin_nachname = tk.Entry(self.admin_profil_frame, text=user_stuff[2] if user_stuff[2] else "", bd=0,
                                           bg='white',
                                           fg='black', font=("Poppins", 18))

            admin_gruppen = tk.Label(self.admin_profil_frame, text="Gruppen", bd=0, bg='white', fg='#6F6C6C',
                                     font=("Poppins", 15))
            self.admin_gruppen = tk.Entry(self.admin_profil_frame, text=user_stuff[3] if user_stuff[3] else "", bd=0,
                                          bg='white', fg='black', font=("Poppins", 18))

            admin_email = tk.Label(self.admin_profil_frame, text="Email", bd=0, bg='white', fg='#6F6C6C',
                                   font=("Poppins", 15))
            self.admin_email = tk.Entry(self.admin_profil_frame, text="@srhk.de", bd=0, bg='white', fg='black',
                                        font=("Poppins", 18))

            rechte = tk.Label(self.admin_profil_frame, text="Rechte", bd=0, bg='white', fg='#6F6C6C',
                              font=("Poppins", 15))
            rechte_frame = tk.Frame(self.admin_profil_frame, bg='#D9D9D9')

            admin_adminrechte = tk.Label(self.admin_profil_frame, text="Admin", bd=0, bg='white',
                                         fg='black' if user_stuff[0][0] == "admin" else '#6F6C6C', font=("Poppins", 18))
            admin_ausbilderrechte = tk.Label(self.admin_profil_frame, text="Ausbilder", bd=0, bg='white',
                                             fg='black' if user_stuff[0][0] == "admin" else '#6F6C6C',
                                             font=("Poppins", 18))
            admin_userrechte = tk.Label(self.admin_profil_frame, text="Schüler", bd=0, bg='white',
                                        fg='black' if user_stuff[0][0] == 'user' else '#6F6C6C', font=("Poppins", 18))

            # Speicherbutton
            def admin_button_click():
                controller.show_frame(Admin)
                messagebox.showinfo("Erfolgreich", "User erfolgreich gespeichert")

            admin_speichern_button = ctk.CTkButton(self, text="Speichern", fg_color=ThemeManager.SRH_Orange,
                                                   text_color="white", font=('Inter', 20, 'bold'),
                                                   corner_radius=8, hover=True, hover_color=ThemeManager.SRH_DarkBlau,
                                                   command=admin_button_click, width=137, height=44)
            admin_speichern_button.place(x=1670, y=950)

            # Löschbutton
            def admin_delete_click():
                confirm = messagebox.askokcancel("Löschen", "User löschen?")

                if confirm:  # Wenn der Benutzer "OK" klickt
                    controller.show_frame(Admin)
                    messagebox.showinfo("Erfolgreich", "User erfolgreich gelöscht")
                else:  # Wenn der Benutzer "Abbrechen" klickt
                    messagebox.showinfo("Abgebrochen", "Löschen abgebrochen, User wurde nicht gelöscht.")

            admin_delete_button = ctk.CTkButton(self, text="Löschen", fg_color=ThemeManager.SRH_DarkBlau,
                                                text_color="white", font=('Inter', 20, 'bold'),
                                                corner_radius=8, hover=True, hover_color=ThemeManager.SRH_Orange,
                                                command=admin_delete_click, width=137, height=44)
            admin_delete_button.place(x=1500, y=950)

            def adminpage():
                controller.show_frame(Admin)

            adminpage = ctk.CTkButton(self, text="↩", fg_color='white', text_color=ThemeManager.SRH_Grey, width=5,
                                      font=("Inter", 50, 'bold'), corner_radius=8, hover=False,
                                      command=adminpage)
            adminpage.place(relx=0.16, rely=0.16, anchor='nw')

            # Seitennavigations-Buttons für Benutzer, Admin, Statistiken und Einstellungen

            def user_button():
                controller.show_frame(Profil)

            user_button = tk.Button(verzeichniss, text="User", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                    font=("Inter", 20, 'bold'),
                                    command=user_button)

            def admin_button():
                controller.show_frame(Admin)

            admin_button = tk.Button(verzeichniss, text="Administration", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                     font=("Inter", 20, 'bold'),
                                     command=admin_button)

            def stats_button():
                controller.show_frame(Stats)

            stats_button = tk.Button(verzeichniss, text="Statistiken", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                     font=("Inter", 20, 'bold'),
                                     command=stats_button)

            def einstellungen_button():
                from configuration import Einstellungen
                controller.show_frame(Einstellungen)

            einstellungen_button = tk.Button(verzeichniss, text="Einstellungen", bd=0, bg=ThemeManager.SRH_Grey,
                                             fg='black',
                                             font=("Inter", 20, 'bold'),
                                             command=einstellungen_button)

            def verzeichniss_help_button():
                controller.show_frame(Help)

            verzeichniss_help_button = tk.Button(verzeichniss, text="Hilfe", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                                 font=("Inter", 20, 'bold'),
                                                 command=verzeichniss_help_button)

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

            self.admin_profil_frame.place(relx=0.21, rely=0.15, relwidth=1, relheight=0.85)

        thread = threading.Thread(target=update_label, daemon=True)
        thread.start()

    def update_admindata(self, data):
        """
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


class Admin(tk.Frame):
    """
    Erstellt die Administrationsseite mit Navigation, Such- und Hinzufügefunktionen sowie einer
    Tabelle zur Anzeige von Benutzerdaten.

    Diese Klasse konfiguriert die Administrationsansicht, in der Administratoren Benutzer verwalten,
    Daten anzeigen und navigieren können.

    **Args:**

    - parent (tk.Widget): Das übergeordnete Widget, in das diese Seite eingebettet wird.
    - controller (object): Eine Instanz, die für den Wechsel zwischen Anwendungsansichten verantwortlich ist.

    **Attributes:**

    - imglogin, imgmainpage, imgSuche, imgHinzufugen (PhotoImage): Bildobjekte für Navigationsbuttons,
      Such- und Hinzufügen-Funktionen.
    - header (ttk.Label): Label als Header der Seite mit dem Titel "Administration".
    - verzeichniss (tk.Frame): Seitenleiste mit Navigationsbuttons für verschiedene Abschnitte
      (z. B. Benutzer, Statistiken).
    - tabelle_frame (tk.Frame): Hauptbereich der Seite, der die Suche, die Hinzufügen-Schaltfläche
      und die Tabelle enthält.
    - tree (ttk.Treeview): Ansicht zur Anzeige der Benutzerdaten in tabellarischer Form.
    - scroll (ttk.Scrollbar): Vertikale Bildlaufleiste für die Tabelle.

    **Verwendet:**

    - login (tk.Button), mainpage (tk.Button): Schaltflächen für die Navigation zur Login-Seite und zur Hauptseite.
    - user_button, admin_button, stats_button, einstellungen_button (tk.Button): Schaltflächen zur Navigation
      zwischen Benutzern, Admin-Daten, Statistiken und Einstellungen.
    - suche_button (ctk.CTkButton), suche_entry (ctk.CTkEntry): Suchfelder und -schaltflächen zur Filterung
      der Daten in der Tabelle.
    - Hinzufugen_button (tk.Button): Schaltfläche zum Hinzufügen eines Benutzers oder Geräts.
    - Spaltenüberschriften und Daten der Tabelle werden dynamisch aus einer Datenbank geladen.
    - showDetails (function): Funktion, die beim Doppelklick auf einen Tabelleneintrag Details
      des ausgewählten Benutzers anzeigt.

    """

    def __init__(self, parent, controller):
        root_path = os.path.dirname(os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir)))
        tk.Frame.__init__(self, parent)
        from ThemeManager import ThemeManager
        self.configure(bg='white')

        # Header-Label für die Profilseite
        header = ttk.Label(self, text="Administration", anchor="center", style="Header.TLabel")
        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)

        # Seitennavigation und laden der Bilder
        verzeichniss = tk.Frame(self, bg=ThemeManager.SRH_Grey)
        # self.admin_frame = tk.Frame(self, bg='white')

        self.imglogin = tk.PhotoImage(
            file=root_path + "/gui/assets/Closeicon.png")
        self.imgmainpage = tk.PhotoImage(
            file=root_path + "/gui/assets/backtosite_icon.png")
        from gui_prototyp import load_image
        self.imgSuche = load_image(root_path + "/gui/assets/Search.png")
        self.imgHinzufugen = load_image(root_path + "/gui/assets/Adding_Icon.png")
        self.imghelp = tk.PhotoImage(file=root_path + "/gui/assets/helpicon.png")

        # Positionierung und Seitennavigations-Buttons für Benutzer, Admin, Statistiken und Einstellungen, Login,
        # Hauptseite und Profilbild

        def login():
            from gui_prototyp import LogInWindow
            controller.show_frame(LogInWindow)

        login = ctk.CTkButton(header, image=self.imglogin, fg_color=ThemeManager.SRH_Orange,
                              bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                              hover=True, hover_color='#e25a1f', text="",
                              command=login)

        def mainpage():
            from Mainpages import MainPage
            controller.show_frame(MainPage)

        mainpage = ctk.CTkButton(header, image=self.imgmainpage, fg_color=ThemeManager.SRH_Orange,
                                 bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                                 hover=True, hover_color='#e25a1f', text="",
                                 command=mainpage)

        def help():
            controller.show_frame(Help)

        help = ctk.CTkButton(header, image=self.imghelp, fg_color=ThemeManager.SRH_Orange,
                             bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                             hover=True, hover_color='#e25a1f', text="",
                             command=help)

        login.place(relx=0.95, rely=0.5, anchor="center")
        mainpage.place(relx=0.90, rely=0.5, anchor="center")
        help.place(relx=0.85, rely=0.5, anchor="center")

        def user_button():
            controller.show_frame(Profil)

        user_button = tk.Button(verzeichniss, text="User", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=user_button)
        user_button.pack(pady=10, anchor='w')

        def admin_button():
            controller.show_frame(Admin)

        admin_button = tk.Button(verzeichniss, text="Administration", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                 font=("Inter", 20, 'bold'),
                                 command=admin_button)
        admin_button.pack(pady=10, anchor='w')

        def stats_button():
            controller.show_frame(Stats)

        stats_button = tk.Button(verzeichniss, text="Statistiken", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                 font=("Inter", 20, 'bold'),
                                 command=stats_button)
        stats_button.pack(pady=10, anchor='w')

        def einstellungen_button():
            from configuration import Einstellungen
            controller.show_frame(Einstellungen)

        einstellungen_button = tk.Button(verzeichniss, text="Einstellungen", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                         font=("Inter", 20, 'bold'),
                                         command=einstellungen_button)
        einstellungen_button.pack(pady=10, anchor='w')

        def verzeichniss_help_button():
            controller.show_frame(Help)

        verzeichniss_help_button = tk.Button(verzeichniss, text="Hilfe", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                             font=("Inter", 20, 'bold'),
                                             command=verzeichniss_help_button)
        verzeichniss_help_button.pack(pady=10, anchor='w')

        # Seiteninhalt
        self.tabelle_frame = tk.Frame(self, bg='white')

        # Suche

        suche_button = ctk.CTkButton(self.tabelle_frame, image=self.imgSuche, corner_radius=8, border_width=0,
                                     fg_color="transparent", hover_color='#D9D9D9',
                                     command=lambda: print(f"nach {suche_entry} gesucht"))
        suche_entry = ctk.CTkEntry(self.tabelle_frame, corner_radius=8, fg_color="#D9D9D9", text_color="black",
                                   border_width=0, font=("Inter", 12))

        suche_button.place(relx=0.075, rely=0.1, relheight=0.04, relwidth=0.028)
        suche_entry.place(relx=0.108, rely=0.1, relwidth=0.33, relheight=0.04)

        # Hinzufügen
        def Hinzufugen_button():
            controller.show_frame(Admin_User)

        Hinzufugen_button = tk.Button(self.tabelle_frame, image=self.imgHinzufugen, bd=0, bg='white',
                                      command=Hinzufugen_button)
        Hinzufugen_button.place(x=1280, y=100)
        # Tabelle
        # Styling
        style = ttk.Style()
        # style.theme_use("clam")
        style.configure("Treeview.Heading", font=("Inter", 12), background="#D9D9D9", foreground="#6E6893")
        style.configure("Treeview", font=("Arial", 11), rowheight=35, background="white", foreground="black")
        style.map("Treeview", background=[("selected", "#D9D9D9")], foreground=[("selected", "black")])
        style.configure("evenrow.Treeview", background="#f2f2f2")
        style.configure("oddrow.Treeview", background="white")

        tree = ttk.Treeview(self.tabelle_frame, columns=("c1", "c2", "c3", "c4"), show="headings",
                            height=5)
        scroll = ctk.CTkScrollbar(
            self.tabelle_frame,
            button_color=ThemeManager.SRH_Grey,
            orientation="vertical",
            command=tree.yview,
            height=600
        )

        # Treeview Scrollverbindung
        tree.configure(yscrollcommand=scroll.set)
        tree.configure(yscrollcommand=scroll.set)

        # Spaltennamen aus der Datenbank holen
        users_uberschrift = fetch_headers("benutzer", ["Passwort"])

        # Überschriften konfigurieren
        tree["columns"] = users_uberschrift
        for up in users_uberschrift:
            tree.column(up, anchor='center', width=100)
            tree.heading(up, text=up)

        users_data = fetch_tables("benutzer", ["Passwort"])

        # Daten aus DB einfügen

        for i, row in enumerate(users_data):
            us_formatted_row = [value if value is not None else "-" for value in row]  # Leere Felder durch "-" ersetzen
            color = "#f3f3f3" if i % 2 == 0 else "white"
            tree.insert("", "end", values=us_formatted_row, tags=("even" if i % 2 == 0 else "odd"))
        # Farben für Tags definieren
        tree.tag_configure("even", background="#f7f7f7")
        tree.tag_configure("odd", background="white")

        tree.place(x=120, y=160, width=1280, height=600)
        scroll.place(x=1400, y=160)
        self.tabelle_frame.place(relx=0.15, rely=0.15, relwidth=0.85, height=1000)
        # self.admin_frame.place(relx=0.21, rely=0.15, relwidth=1, relheight=0.85)
        verzeichniss.place(relx=0, rely=0.15, relwidth=0.15, relheight=0.85)

        # Gerät aus Tabelle öffnen
        def on_user_select(event):
            try:
                selected_User = tree.focus()
                print(f"Ausgewähltes Item: {selected_User}")
                if selected_User:
                    showDetails(selected_User, tree, controller)
            except Exception as e:
                print(f"Fehler bei der Auswahl {e}")

        tree.bind("<Double-1>", on_user_select)


def showDetails(selected_User, tree, controller):
    data = tree.item(selected_User, "values")
    print(f"Daten des ausgewählten Items: {data}")

    details = controller.frames[Admin_User]
    details.update_admindata(data)
    controller.show_frame(Admin_User)


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
        from ThemeManager import ThemeManager
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

        def login():
            from gui_prototyp import LogInWindow
            controller.show_frame(LogInWindow)

        login = ctk.CTkButton(header, image=self.imglogin, fg_color=ThemeManager.SRH_Orange,
                              bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                              hover=True, hover_color='#e25a1f', text="",
                              command=login)

        def mainpage():
            from Mainpages import MainPage
            controller.show_frame(MainPage)

        mainpage = ctk.CTkButton(header, image=self.imgmainpage, fg_color=ThemeManager.SRH_Orange,
                                 bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                                 hover=True, hover_color='#e25a1f', text="",
                                 command=mainpage)

        def help():
            controller.show_frame(Help)

        help = ctk.CTkButton(header, image=self.imghelp, fg_color=ThemeManager.SRH_Orange,
                             bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                             hover=True, hover_color='#e25a1f', text="",
                             command=help)

        login.place(relx=0.95, rely=0.5, anchor="center")
        mainpage.place(relx=0.90, rely=0.5, anchor="center")
        help.place(relx=0.85, rely=0.5, anchor="center")

        # Linksseitige Navigationsbutton für verschiedene Ansichten

        def user_button():
            controller.show_frame(Profil)

        user_button = tk.Button(verzeichniss, text="User", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=user_button)
        user_button.pack(pady=10, anchor='w')

        def admin_button():
            controller.show_frame(Admin)

        admin_button = tk.Button(verzeichniss, text="Administration", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                 font=("Inter", 20, 'bold'),
                                 command=admin_button)
        admin_button.pack(pady=10, anchor='w')

        def stats_button():
            controller.show_frame(Stats)

        stats_button = tk.Button(verzeichniss, text="Statistiken", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                 font=("Inter", 20, 'bold'),
                                 command=stats_button)
        stats_button.pack(pady=10, anchor='w')

        def einstellungen_button():
            from configuration import Einstellungen
            controller.show_frame(Einstellungen)

        einstellungen_button = tk.Button(verzeichniss, text="Einstellungen", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                         font=("Inter", 20, 'bold'),
                                         command=einstellungen_button)
        einstellungen_button.pack(pady=10, anchor='w')

        def verzeichniss_help_button():
            controller.show_frame(Help)

        verzeichniss_help_button = tk.Button(verzeichniss, text="Hilfe", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                             font=("Inter", 20, 'bold'),
                                             command=verzeichniss_help_button)
        verzeichniss_help_button.pack(pady=10, anchor='w')

        # Platzierung des Hauptinhaltsbereichs und der Navigationsleiste
        self.stats_frame.place(relx=0.21, rely=0.15, relwidth=1, relheight=0.85)
        verzeichniss.place(relx=0, rely=0.15, relwidth=0.15, relheight=0.85)


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
        from ThemeManager import ThemeManager
        root_path = os.path.dirname(os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir)))
        self.configure(bg='white')

        # Header-Label für die Statistikseite
        header = ttk.Label(self, text="Hilfsseite", anchor="center", style="Header.TLabel")
        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)

        # Navigationsleiste auf der linken Seite
        verzeichniss = tk.Frame(self, bg=ThemeManager.SRH_Grey)
        self.hilfe_frame = tk.Frame(self, bg='white')

        # Bilder für die Login- und Hauptseite-Buttons laden
        self.imglogin = tk.PhotoImage(
            file=root_path + "/gui/assets/Closeicon.png")
        self.imgmainpage = tk.PhotoImage(
            file=root_path + "/gui/assets/backtosite_icon.png")
        self.imghelp = tk.PhotoImage(file=root_path + "/gui/assets/helpicon.png")

        # Header-Navigationsbuttons (Login und Hauptseite), Platzierung der Header-Buttons

        def login():
            from gui_prototyp import LogInWindow
            controller.show_frame(LogInWindow)

        login = ctk.CTkButton(header, image=self.imglogin, fg_color=ThemeManager.SRH_Orange,
                              bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                              hover=True, hover_color='#e25a1f', text="",
                              command=login)

        def mainpage():
            from Mainpages import MainPage
            controller.show_frame(MainPage)

        mainpage = ctk.CTkButton(header, image=self.imgmainpage, fg_color=ThemeManager.SRH_Orange,
                                 bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                                 hover=True, hover_color='#e25a1f', text="",
                                 command=mainpage)

        def meme_help():
            meme_page = tk.Toplevel()  # root
            meme_page.title("Meme")
            meme_page.geometry("240x300+500+300")
            meme_page.iconbitmap(root_path + "/gui/assets/sad.ico")
            meme_page.configure(bg='white')

            meme_page.grab_set()
            # Bilder
            from gui_prototyp import load_image
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
                from gui_prototyp import load_image
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
                    from gui_prototyp import load_image
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

        def user_button():
            controller.show_frame(Profil)

        user_button = tk.Button(verzeichniss, text="User", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=user_button)
        user_button.pack(pady=10, anchor='w')

        def admin_button():
            controller.show_frame(Admin)

        admin_button = tk.Button(verzeichniss, text="Administration", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                 font=("Inter", 20, 'bold'),
                                 command=admin_button)
        admin_button.pack(pady=10, anchor='w')

        def stats_button():
            controller.show_frame(Stats)

        stats_button = tk.Button(verzeichniss, text="Statistiken", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                 font=("Inter", 20, 'bold'),
                                 command=stats_button)
        stats_button.pack(pady=10, anchor='w')

        def einstellungen_button():
            from configuration import Einstellungen
            controller.show_frame(Einstellungen)

        einstellungen_button = tk.Button(verzeichniss, text="Einstellungen", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                         font=("Inter", 20, 'bold'),
                                         command=einstellungen_button)
        einstellungen_button.pack(pady=10, anchor='w')

        def verzeichniss_help_button():
            controller.show_frame(Help)

        verzeichniss_help_button = tk.Button(verzeichniss, text="Hilfe", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                             font=("Inter", 20, 'bold'),
                                             command=verzeichniss_help_button)
        verzeichniss_help_button.pack(pady=10, anchor='w')
        einstellungen_button.pack(pady=10, anchor='w')

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
