import tkinter as tk
from tkinter import ttk
import os
import customtkinter as ctk
from customtkinter import *

import gui_prototyp
import Overview_pages
import Profiles


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
        from ThemeManager import ThemeManager
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
        self.imghelp = tk.PhotoImage(file=root_path + "/gui/assets/helpicon.png")
        self.imgbildgr1 = tk.PhotoImage(file=root_path+"/gui/assets/Gruppe_1.png")
        self.imgbildgr2 = tk.PhotoImage(file=root_path+"/gui/assets/Gruppe2.png")
        self.imgbildgr3 = tk.PhotoImage(file=root_path+"/gui/assets/Gruppe3.png")
        self.imgbildgr4 = tk.PhotoImage(file=root_path+"/gui/assets/Gruppe4.png")
        self.imgbildgr5 = tk.PhotoImage(file=root_path+"/gui/assets/Gruppe5.png")
        self.imgbildgr6 = tk.PhotoImage(file=root_path+"/gui/assets/Gruppe6.png")
        self.imgbildgr7 = tk.PhotoImage(file=root_path+"/gui/assets/Gruppe7.png")
        self.imgbildgr8 = tk.PhotoImage(file=root_path+"/gui/assets/Gruppe8.png")
        self.imgseitevor = tk.PhotoImage(file=root_path+"/gui/assets/pageforward_icon.png")

        # Platzierung der Buttons
        login = ctk.CTkButton(header, image=self.imglogin, fg_color=ThemeManager.SRH_Orange, bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                              hover=True, hover_color='#e25a1f', text="", command=lambda :controller.show_frame(gui_prototyp.LogInWindow))
        profil = ctk.CTkButton(header, image=self.imgprofil, fg_color=ThemeManager.SRH_Orange, bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                              hover=True, hover_color='#e25a1f', text="", command=lambda: controller.show_frame(Profiles.Profil))
        help = ctk.CTkButton(header, image=self.imghelp, fg_color=ThemeManager.SRH_Orange,
                             bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                             hover=True, hover_color='#e25a1f', text="",
                             command=lambda: print("help"))

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

        all = ctk.CTkButton(self, text="Alle Anzeigen", fg_color='white', text_color=ThemeManager.SRH_Blau,
                                     font=("Inter", 20), corner_radius=8, hover=False,
                                     command=lambda: controller.show_frame(Overview_pages.Ubersicht))

        seitevor = ctk.CTkButton(self, image=self.imgseitevor, text="", fg_color='white', text_color='black', font=("Inter", 20, 'bold'),
                      corner_radius=8, hover=False,
                      command=lambda: controller.show_frame(MainPageS2), width=200, height=30, hover_color=ThemeManager.SRH_Orange)

        # Festlegung des Styles für Header- und Footer Labels, Positionierung der Navigationsbuttons im Header, die
        # Anordnung der Bildgruppen-Buttons in einem Rasterlayout, sowie Platzierungen.
        style = ttk.Style()
        style.configure("Header.TLabel", foreground='white', background='#DF4807', font=("Inter", 55, 'bold'))
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
        bildgr8.place(relx=0.80, rely=0.55, anchor='n')

        all.place(relx=0.01, rely=0.18, anchor='w')
        seitevor.place(relx=0.51, rely=0.80, anchor='n')
        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)
        bottom.place(relx=0, rely=0.85, relwidth=1, relheight=0.13)


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
        from ThemeManager import ThemeManager
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
        self.imghelp = tk.PhotoImage(file=root_path + "/gui/assets/helpicon.png")
        self.imgbildgr1 = tk.PhotoImage(file=root_path+"/gui/assets/Gruppe_1.png")
        self.imgbildgr2 = tk.PhotoImage(file=root_path+"/gui/assets/Gruppe2.png")
        self.imgbildgr3 = tk.PhotoImage(file=root_path+"/gui/assets/Gruppe3.png")
        self.imgbildgr4 = tk.PhotoImage(file=root_path+"/gui/assets/Gruppe4.png")
        self.imgbildgr5 = tk.PhotoImage(file=root_path+"/gui/assets/Gruppe5.png")
        self.imgbildgr6 = tk.PhotoImage(file=root_path+"/gui/assets/Gruppe6.png")
        self.imgbildgr7 = tk.PhotoImage(file=root_path+"/gui/assets/Gruppe7.png")
        #self.imgbildgr8 = tk.PhotoImage(file=root_path+"/gui/assets/Gruppe8.png")
        self.imgseitevor = tk.PhotoImage(file=root_path+"/gui/assets/pageforward_icon.png")
        self.imgseiteback = tk.PhotoImage(file=root_path+"/gui/assets/pageback_icon.png")
        login = ctk.CTkButton(header, image=self.imglogin, fg_color=ThemeManager.SRH_Orange,
                              bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                              hover=True, hover_color='#e25a1f', text="",
                              command=lambda: controller.show_frame(gui_prototyp.LogInWindow))

        profil = ctk.CTkButton(header, image=self.imgprofil, fg_color=ThemeManager.SRH_Orange,
                               bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                               hover=True, hover_color='#e25a1f', text="",
                               command=lambda: controller.show_frame(Profiles.Profil))
        help = ctk.CTkButton(header, image=self.imghelp, fg_color=ThemeManager.SRH_Orange,
                             bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                             hover=True, hover_color='#e25a1f', text="",
                             command=lambda: controller.show_frame(Profiles.Help))

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
        all = ctk.CTkButton(self, text="Alle Anzeigen", fg_color='white', text_color=ThemeManager.SRH_Blau,
                            font=("Inter", 20), corner_radius=8, hover=False,
                            command=lambda: controller.show_frame(Overview_pages.Ubersicht))

        seitevor = ctk.CTkButton(self, image=self.imgseitevor, text="", fg_color='white', text_color='black',
                                 font=("Inter", 20, 'bold'),
                                 corner_radius=8, hover=False,
                                 command=lambda: controller.show_frame(MainPageS2), width=10, height=30,
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
