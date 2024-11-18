import tkinter as tk
from tkinter import ttk
import os

import gui_prototyp
import ThemeManager
import Overview_pages
import Profiles


class MainPage(tk.Frame):
    """Erstellt die Startseite mit Navigations- und Funktionsbuttons sowie Bildgurppen
       Ermöglicht den Zugriff auf Login, Profil und Übersichtsseiten"""

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
        self.imglogin = gui_prototyp.load_image(root_path+"/gui/assets/Closeicon.png")
        self.imgprofil = gui_prototyp.load_image(root_path+"/gui/assets/profileicon.png")
        self.imgbildgr1 = tk.PhotoImage(file=root_path+"/gui/assets/Gruppe1.png")
        self.imgbildgr2 = tk.PhotoImage(file=root_path+"/gui/assets/Gruppe2.png")
        self.imgbildgr3 = tk.PhotoImage(file=root_path+"/gui/assets/Gruppe3.png")
        self.imgbildgr4 = tk.PhotoImage(file=root_path+"/gui/assets/Gruppe4.png")
        self.imgbildgr5 = tk.PhotoImage(file=root_path+"/gui/assets/Gruppe5.png")
        self.imgbildgr6 = tk.PhotoImage(file=root_path+"/gui/assets/Gruppe6.png")
        self.imgbildgr7 = tk.PhotoImage(file=root_path+"/gui/assets/Gruppe7.png")
        self.imgbildgr8 = tk.PhotoImage(file=root_path+"/gui/assets/Gruppe8.png")
        self.imgseitevor = tk.PhotoImage(file=root_path+"/gui/assets/pageforward_icon.png")

        # Platzierung der Buttons
        login = tk.Button(header, image=self.imglogin, bd=0, bg=ThemeManager.SRH_Orange,
                          command=lambda: controller.show_frame(gui_prototyp.LogInWindow))
        profil = tk.Button(header, image=self.imgprofil, bd=0, bg=ThemeManager.SRH_Orange,
                           command=lambda: controller.show_frame(Profiles.Profil))
        bildgr1 = tk.Button(self, image=self.imgbildgr1, bd=0, bg='white',
                            command=lambda: controller.show_frame(Overview_pages.Ubersicht))
        bildgr2 = tk.Button(self, image=self.imgbildgr2, bd=0, bg='white',
                            command=lambda: controller.show_frame(Overview_pages.Ubersicht))
        bildgr3 = tk.Button(self, image=self.imgbildgr3, bd=0, bg='white',
                            command=lambda: controller.show_frame(Overview_pages.Ubersicht))
        bildgr4 = tk.Button(self, image=self.imgbildgr4, bd=0, bg='white',
                            command=lambda: controller.show_frame(Overview_pages.Ubersicht))
        bildgr5 = tk.Button(self, image=self.imgbildgr5, bd=0, bg='white',
                            command=lambda: controller.show_frame(Overview_pages.Ubersicht))
        bildgr6 = tk.Button(self, image=self.imgbildgr6, bd=0, bg='white',
                            command=lambda: controller.show_frame(Overview_pages.Ubersicht))
        bildgr7 = tk.Button(self, image=self.imgbildgr7, bd=0, bg='white',
                            command=lambda: controller.show_frame(Overview_pages.Ubersicht))
        bildgr8 = tk.Button(self, image=self.imgbildgr8, bd=0, bg='white',
                            command=lambda: controller.show_frame(Overview_pages.Ubersicht))
        all = tk.Button(self, text="Alle anzeigen", bd=0, bg='white', fg=ThemeManager.SRH_Blau, font=("Inter", 20),
                        command=lambda: controller.show_frame(Overview_pages.Ubersicht))
        seitevor = tk.Button(self, image=self.imgseitevor, bd=0, bg='white', fg='#1E1E1E', font=("Inter", 16),
                             command=lambda: controller.show_frame(MainPageS2))

        # Festlegung des Styles für Header- und Footer Labels, Positionierung der Navigationsbuttons im Header, die
        # Anordnung der Bildgruppen-Buttons in einem Rasterlayout, sowie Platzierungen.
        style = ttk.Style()
        style.configure("Header.TLabel", foreground='white', background='#DF4807', font=("Inter", 55, 'bold'))
        style.configure("Footer.TLabel", background=ThemeManager.SRH_Grey)

        login.place(relx=0.95, rely=0.5, anchor="center")
        profil.place(relx=0.90, rely=0.5, anchor="center")

        bildgr1.place(relx=0.20, rely=0.25, anchor='n')
        bildgr2.place(relx=0.40, rely=0.25, anchor='n')
        bildgr3.place(relx=0.60, rely=0.25, anchor='n')
        bildgr4.place(relx=0.80, rely=0.25, anchor='n')

        bildgr5.place(relx=0.20, rely=0.55, anchor='n')
        bildgr6.place(relx=0.40, rely=0.55, anchor='n')
        bildgr7.place(relx=0.60, rely=0.55, anchor='n')
        bildgr8.place(relx=0.80, rely=0.55, anchor='n')

        all.place(relx=0.01, rely=0.18, anchor='w')
        seitevor.place(relx=0.51, rely=0.80, anchor='n')
        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)
        bottom.place(relx=0, rely=0.85, relwidth=1, relheight=0.13)


class MainPageS2(tk.Frame):
    """Repräsentiert die zweite Seite der Startseite mit weiteren Gruppen und Navigation.
       Ermöglicht die Navigation zurück zur Hauptseite oder zu zusätzlichen Detailansichten."""

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
        self.imglogin = gui_prototyp.load_image(root_path+"/gui/assets/Closeicon.png")
        self.imgprofil = gui_prototyp.load_image(root_path+"/gui/assets/profileicon.png")
        self.imgbildgr1 = tk.PhotoImage(file=root_path+"/gui/assets/Gruppe1.png")
        self.imgbildgr2 = tk.PhotoImage(file=root_path+"/gui/assets/Gruppe2.png")
        self.imgbildgr3 = tk.PhotoImage(file=root_path+"/gui/assets/Gruppe3.png")
        self.imgbildgr4 = tk.PhotoImage(file=root_path+"/gui/assets/Gruppe4.png")
        self.imgbildgr5 = tk.PhotoImage(file=root_path+"/gui/assets/Gruppe5.png")
        self.imgbildgr6 = tk.PhotoImage(file=root_path+"/gui/assets/Gruppe6.png")
        self.imgbildgr7 = tk.PhotoImage(file=root_path+"/gui/assets/Gruppe7.png")
        # self.imgbildgr8 = tk.PhotoImage(file=root_path+"/gui/assets/Gruppe8.png")
        self.imgseitevor = tk.PhotoImage(file=root_path+"/gui/assets/pageforward_icon.png")
        self.imgseiteback = tk.PhotoImage(file=root_path+"/gui/assets/pageback_icon.png")
        login = tk.Button(header, image=self.imglogin, bd=0, bg=ThemeManager.SRH_Orange,
                          command=lambda: controller.show_frame(gui_prototyp.LogInWindow))
        profil = tk.Button(header, image=self.imgprofil, bd=0, bg=ThemeManager.SRH_Orange,
                           command=lambda: controller.show_frame(Profiles.Profil))
        bildgr1 = tk.Button(self, image=self.imgbildgr1, bd=0, bg='white',
                            command=lambda: controller.show_frame(Overview_pages.Ubersicht))
        bildgr2 = tk.Button(self, image=self.imgbildgr2, bd=0, bg='white',
                            command=lambda: controller.show_frame(Overview_pages.Ubersicht))
        bildgr3 = tk.Button(self, image=self.imgbildgr3, bd=0, bg='white',
                            command=lambda: controller.show_frame(Overview_pages.Ubersicht))
        bildgr4 = tk.Button(self, image=self.imgbildgr4, bd=0, bg='white',
                            command=lambda: controller.show_frame(Overview_pages.Ubersicht))
        bildgr5 = tk.Button(self, image=self.imgbildgr5, bd=0, bg='white',
                            command=lambda: controller.show_frame(Overview_pages.Ubersicht))
        bildgr6 = tk.Button(self, image=self.imgbildgr6, bd=0, bg='white',
                            command=lambda: controller.show_frame(Overview_pages.Ubersicht))
        bildgr7 = tk.Button(self, image=self.imgbildgr7, bd=0, bg='white',
                            command=lambda: controller.show_frame(Overview_pages.Ubersicht))
        # bildgr8 = tk.Button(self, image=self.imgbildgr8, bd=0, bg='white',
        # command=lambda: controller.show_frame(Ubersicht))

        # Buttons zum Wechseln zwischen den Hauptseiten und "Alle anzeigen" Button für die Übersichtsseite
        all = tk.Button(self, text="Alle anzeigen", bd=0, bg='white', fg=ThemeManager.SRH_Blau, font=("Inter", 20),
                        command=lambda: controller.show_frame(Overview_pages.Ubersicht))
        seitevor = tk.Button(self, image=self.imgseitevor, bd=0, bg='white', fg='#1E1E1E', font=("Inter", 16),
                             command=lambda: controller.show_frame(MainPageS2))
        seiteback = tk.Button(self, image=self.imgseiteback, bd=0, bg='white', fg='#1E1E1E', font=("Inter", 16),
                              command=lambda: controller.show_frame(MainPage))

        # Style Konfiguration für Header und Footer, Platzierung der Buttons, Header und Footer
        style = ttk.Style()
        style.configure("Header.TLabel", foreground='white', background=ThemeManager.SRH_Orange,
                        font=("Inter", 55, 'bold'))
        style.configure("Footer.TLabel", background=ThemeManager.SRH_Grey)

        login.place(relx=0.95, rely=0.5, anchor="center")
        profil.place(relx=0.90, rely=0.5, anchor="center")

        bildgr1.place(relx=0.20, rely=0.25, anchor='n')
        bildgr2.place(relx=0.40, rely=0.25, anchor='n')
        bildgr3.place(relx=0.60, rely=0.25, anchor='n')
        bildgr4.place(relx=0.80, rely=0.25, anchor='n')

        bildgr5.place(relx=0.20, rely=0.55, anchor='n')
        bildgr6.place(relx=0.40, rely=0.55, anchor='n')
        bildgr7.place(relx=0.60, rely=0.55, anchor='n')
        # bildgr8.place(relx=0.80, rely=0.55, anchor='n')

        all.place(relx=0.01, rely=0.18, anchor='w')
        seitevor.place(relx=0.51, rely=0.80, anchor='n')
        seiteback.place(relx=0.49, rely=0.80, anchor='n')
        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)
        bottom.place(relx=0, rely=0.85, relwidth=1, relheight=0.13)
