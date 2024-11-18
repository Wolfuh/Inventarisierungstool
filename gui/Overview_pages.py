import tkinter as tk
from tkinter import ttk
from tkinter import *

import gui_prototyp
import ThemeManager
import Mainpages
import Einstellungen
import Profiles


class Ubersicht(tk.Frame):
    """Repraesentiert die Geraeteuebersichtsseite der Anwendung. Zeigt eine Liste oder Tabelle der verfügbaren
       Geräte und bietet Optionen für die Navigation zurück zur Hauptseite, zum Login und zu Benutzerprofilen """

    def __init__(self, parent, controller):
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
        self.ubersicht_frame.place(relx=0.21, rely=0.15, relwidth=1, relheight=0.85)

        # Layout Festlegung der flexiblen Skalierung der Übersichtsseite
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)

        # Laden der Bilder für die Navigation und Header Buttons
        self.imglogin = gui_prototyp.load_image("gui/assets/Closeicon.png")
        self.imgprofil = gui_prototyp.load_image("gui/assets/profileicon.png")

        # Login und Profil Buttons im Header-Bereich, Platzierung der Buttons, Header und Sidebar
        login = tk.Button(header, image=self.imglogin, bd=0, bg=ThemeManager.SRH_Orange,
                          command=lambda: controller.show_frame(gui_prototyp.LogInWindow))
        profil = tk.Button(header, image=self.imgprofil, bd=0, bg=ThemeManager.SRH_Orange,
                           command=lambda: controller.show_frame(Profiles.Profil))
        self.imgmainpage = tk.PhotoImage(
            file="gui/assets/backtosite_icon.png")

        login.place(relx=0.95, rely=0.5, anchor="center")
        profil.place(relx=0.90, rely=0.5, anchor="center")

        tk.Button(header, image=self.imgmainpage, bd=0, bg=ThemeManager.SRH_Orange,
                  command=lambda: controller.show_frame(Mainpages.MainPage))

        # "Alle Anzeigen" Button in der Seitenleiste
        all_button = tk.Button(verzeichniss, text="Alle anzeigen", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                               font=("Inter", 20, 'bold'),
                               command=lambda: controller.show_frame(Ubersicht))

        all_button.pack(pady=10, anchor='w')

        # Gruppe 1
        def show_dropdown_grp1():
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg=ThemeManager.SRH_Grey, fg='black')
            dropdown_menu.add_command(label="→ Hardware", command=lambda: controller.show_frame(Profiles.Admin))
            dropdown_menu.add_command(label="→ Software", command=lambda: controller.show_frame(Profiles.Stats))
            dropdown_menu.add_command(label="→ Peripherie", command=lambda: controller.show_frame(Profiles.Profil))
            dropdown_menu.add_command(label="→ Andere", command=lambda: controller.show_frame(Einstellungen))
            dropdown_menu.post(grp1_button.winfo_rootx(), grp1_button.winfo_rooty() + grp1_button.winfo_height())

        grp1_button = tk.Button(verzeichniss, text="Gruppe 1   ", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=show_dropdown_grp1)
        grp1_button.pack(pady=10, anchor='w')

        # Gruppe 2
        def show_dropdown_grp2():
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg=ThemeManager.SRH_Grey, fg='black')
            dropdown_menu.add_command(label="→ Hardware", command=lambda: controller.show_frame(Profiles.Admin))
            dropdown_menu.add_command(label="→ Software", command=lambda: controller.show_frame(Profiles.Stats))
            dropdown_menu.add_command(label="→ Peripherie", command=lambda: controller.show_frame(Profiles.Profil))
            dropdown_menu.add_command(label="→ Andere", command=lambda: controller.show_frame(Einstellungen))
            dropdown_menu.post(grp2_button.winfo_rootx(), grp2_button.winfo_rooty() + grp2_button.winfo_height())

        grp2_button = tk.Button(verzeichniss, text="Gruppe 2   ", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=show_dropdown_grp2)
        grp2_button.pack(pady=10, anchor='w')

        # Gruppe 3
        def show_dropdown_grp3():
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg=ThemeManager.SRH_Grey, fg='black')
            dropdown_menu.add_command(label="→ Hardware", command=lambda: controller.show_frame(Profiles.Admin))
            dropdown_menu.add_command(label="→ Software", command=lambda: controller.show_frame(Profiles.Stats))
            dropdown_menu.add_command(label="→ Peripherie", command=lambda: controller.show_frame(Profiles.Profil))
            dropdown_menu.add_command(label="→ Andere", command=lambda: controller.show_frame(Einstellungen))
            dropdown_menu.post(grp3_button.winfo_rootx(), grp3_button.winfo_rooty() + grp3_button.winfo_height())

        grp3_button = tk.Button(verzeichniss, text="Gruppe 3   ", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=show_dropdown_grp3)
        grp3_button.pack(pady=10, anchor='w')

        # Gruppe 4
        def show_dropdown_grp4():
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg=ThemeManager.SRH_Grey, fg='black')
            dropdown_menu.add_command(label="→ Hardware", command=lambda: controller.show_frame(Profiles.Admin))
            dropdown_menu.add_command(label="→ Software", command=lambda: controller.show_frame(Profiles.Stats))
            dropdown_menu.add_command(label="→ Peripherie", command=lambda: controller.show_frame(Profiles.Profil))
            dropdown_menu.add_command(label="→ Andere", command=lambda: controller.show_frame(Einstellungen))
            dropdown_menu.post(grp4_button.winfo_rootx(), grp4_button.winfo_rooty() + grp4_button.winfo_height())

        grp4_button = tk.Button(verzeichniss, text="Gruppe 4   ", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=show_dropdown_grp4)
        grp4_button.pack(pady=10, anchor='w')

        # Gruppe 5
        def show_dropdown_grp5():
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg=ThemeManager.SRH_Grey, fg='black')
            dropdown_menu.add_command(label="→ Hardware", command=lambda: controller.show_frame(Profiles.Admin))
            dropdown_menu.add_command(label="→ Software", command=lambda: controller.show_frame(Profiles.Stats))
            dropdown_menu.add_command(label="→ Peripherie", command=lambda: controller.show_frame(Profiles.Profil))
            dropdown_menu.add_command(label="→ Andere", command=lambda: controller.show_frame(Einstellungen))
            dropdown_menu.post(grp5_button.winfo_rootx(), grp5_button.winfo_rooty() + grp5_button.winfo_height())

        grp5_button = tk.Button(verzeichniss, text="Gruppe 5   ", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=show_dropdown_grp5)
        grp5_button.pack(pady=10, anchor='w')

        # Gruppe 6
        def show_dropdown_grp6():
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg=ThemeManager.SRH_Grey, fg='black')
            dropdown_menu.add_command(label="→ Hardware", command=lambda: controller.show_frame(Profiles.Admin))
            dropdown_menu.add_command(label="→ Software", command=lambda: controller.show_frame(Profiles.Stats))
            dropdown_menu.add_command(label="→ Peripherie", command=lambda: controller.show_frame(Profiles.Profil))
            dropdown_menu.add_command(label="→ Andere", command=lambda: controller.show_frame(Einstellungen))
            dropdown_menu.post(grp6_button.winfo_rootx(), grp6_button.winfo_rooty() + grp6_button.winfo_height())

        grp6_button = tk.Button(verzeichniss, text="Gruppe 6   ", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=show_dropdown_grp6)
        grp6_button.pack(pady=10, anchor='w')

        # Gruppe 7
        def show_dropdown_grp7():
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg=ThemeManager.SRH_Grey, fg='black')
            dropdown_menu.add_command(label="→ Hardware", command=lambda: controller.show_frame(Profiles.Admin))
            dropdown_menu.add_command(label="→ Software", command=lambda: controller.show_frame(Profiles.Stats))
            dropdown_menu.add_command(label="→ Peripherie", command=lambda: controller.show_frame(Profiles.Profil))
            dropdown_menu.add_command(label="→ Andere", command=lambda: controller.show_frame(Einstellungen))
            dropdown_menu.post(grp7_button.winfo_rootx(), grp7_button.winfo_rooty() + grp7_button.winfo_height())

        grp7_button = tk.Button(verzeichniss, text="Gruppe 7   ", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=show_dropdown_grp7)
        grp7_button.pack(pady=10, anchor='w')

        # Gruppe 8
        def show_dropdown_grp8():
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg=ThemeManager.SRH_Grey, fg='black')
            dropdown_menu.add_command(label="→ Hardware", command=lambda: controller.show_frame(Profiles.Admin))
            dropdown_menu.add_command(label="→ Software", command=lambda: controller.show_frame(Profiles.Stats))
            dropdown_menu.add_command(label="→ Peripherie", command=lambda: controller.show_frame(Profiles.Profil))
            dropdown_menu.add_command(label="→ Andere", command=lambda: controller.show_frame(Einstellungen))
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
        self.imgFilter = gui_prototyp.load_image("gui/assets/Filter_Button.png")
        self.imgSuche = gui_prototyp.load_image("gui/assets/Search.png")
        self.imgHinzufugen = gui_prototyp.load_image("gui/assets/Adding_Icon.png")
        self.imgAktionen = gui_prototyp.load_image("gui/assets/Aktionen_Button.png")

        # Filterfunktion
        def show_dropdown_Filter():
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg='white', fg='black')
            dropdown_menu.add_command(label="→ Status", command=lambda: print("nach Status sortieren"))
            dropdown_menu.add_command(label="→ ID", command=lambda: print("nach ID sortieren"))
            dropdown_menu.add_command(label="→ Typ", command=lambda: print("nach Typ sortieren"))
            dropdown_menu.add_command(label="→ Andere", command=lambda: print("nach anderen sortieren"))
            dropdown_menu.post(Filter_button.winfo_rootx(), Filter_button.winfo_rooty() + Filter_button.winfo_height())

        Filter_button = tk.Button(self.ubersicht_frame, image=self.imgFilter, bd=0, bg='white', fg='black',
                                  font=("Inter", 20, 'bold'),
                                  command=show_dropdown_Filter)
        Filter_button.place(relx=0, rely=0.1)
        # Suche
        suche_button = tk.Button(self.ubersicht_frame, image=self.imgSuche, bd=0, bg=ThemeManager.SRH_Grey,
                                 command=lambda: print(f"nach {suche_entry} gesucht"))
        suche_entry = tk.Entry(self.ubersicht_frame, bg='#D9D9D9', bd=0, font=("Inter", 12))

        suche_button.place(relx=0.1, rely=0.1, relheight=0.04, relwidth=0.02)
        suche_entry.place(relx=0.12, rely=0.1, relwidth=0.33, relheight=0.04)

        # Hinzufügen
        Hinzufugen_button = tk.Button(self.ubersicht_frame, image=self.imgHinzufugen, bd=0, bg='white',
                                      command=lambda: controller.show_frame(Gerateansicht))
        Hinzufugen_button.place(relx=0.5, rely=0.1)

        # Aktionen
        Aktionen_button = tk.Button(self.ubersicht_frame, image=self.imgAktionen, bd=0, bg='white',
                                    command=lambda: print("Aktionen werden ausgeführt"))
        Aktionen_button.place(relx=0.6, rely=0.1)

        # Tabelle
        lst = [(1, 'IT-18', 'hfsfdfs', 'PC', 'Aktiv', 'frei'),
               (2, 'IT-98', 'gdsg', 'PC', 'Aktiv', 'frei'),
               (3, 'IT-08', 'hfsfggwerdfs', 'PC', 'in Reperatur', '/'),
               (4, 'IT-58', 'fdghrth', 'PC', 'Aktiv', 'frei'),
               (5, 'IT-38', '324fd', 'PC', 'kaputt', '/'),
               (6, 'IT-28', 'gfg56', 'PC', 'Aktiv', 'gebucht')
               ]

        for i in range(len(lst)):
            for j in range(len(lst[0])):
                e = tk.Entry(self.tabelle_frame, width=10, fg='black', bd=0, font=('Inter', 14))
                e.grid(row=i, column=j, padx=3, pady=3, ipady=3, sticky="nsew")
                e.insert(tk.END, lst[i][j])

        # Konfiguriere die Spalten für gleiche Breite
        for j in range(len(lst[0])):
            self.tabelle_frame.grid_columnconfigure(j, weight=1)

        # Setze explizite Mindesthöhe für Zeile 5
        self.tabelle_frame.grid_rowconfigure(5, minsize=10)  # Falls die Höhe manuell angepasst werden soll

        # Platziere die Elemente
        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)
        verzeichniss.place(relx=0, rely=0.15, relwidth=0.15, relheight=0.85)
        self.tabelle_frame.place(relx=0.15, rely=0.3, relwidth=0.85, relheight=0.5)  # Frame für Tabelle definieren


class Gerateansicht(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')

        # Konfiguration der Grid-Struktur für die gesamte Seite
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)

        # Header und Verzeichnis-Label erstellen
        header = ttk.Label(self, text="Geräteansicht", anchor="center", style="Header.TLabel")
        verzeichniss = ttk.Label(self, style="Footer.TLabel")

        # Frame für Hauptinhalt der Geräteansicht erstellen
        self.gerateansicht_frame = tk.Frame(self, bg='white')
        self.gerateansicht_frame.place(relx=0.21, rely=0.15, relwidth=1, relheight=0.85)

        # Bilder laden
        self.imglogin = tk.PhotoImage(file="gui/assets/Closeicon.png")
        self.imgmainpage = tk.PhotoImage(file="gui/assets/backtosite_grey_icon.png")
        self.imgprofil = gui_prototyp.load_image("gui/assets/profileicon.png")

        # Stil für Header und Footer anpassen
        style = ttk.Style()
        style.configure("Header.TLabel", foreground='white',
                        background=ThemeManager.SRH_Orange, font=("Inter", 50, 'bold'))
        style.configure("Footer.TLabel", background=ThemeManager.SRH_Grey)

        # Buttons hinzufügen
        login = tk.Button(header, image=self.imglogin, bd=0, bg=ThemeManager.SRH_Orange,
                          command=lambda: controller.show_frame(gui_prototyp.LogInWindow))
        profil = tk.Button(header, image=self.imgprofil, bd=0, bg=ThemeManager.SRH_Orange,
                           command=lambda: controller.show_frame(Profiles.Profil))

        # Mainpage-Button innerhalb von gerateansicht_frame, an der gleichen Position wie das profilbild in Profil
        mainpage = tk.Button(self, image=self.imgmainpage, bd=0, bg='white',
                             command=lambda: controller.show_frame(Ubersicht))
        # Seiteninhalt
        tree = ttk.Treeview(self.gerateansicht_frame, columns=("c1", "c2", "c3", "c4", "c5", "c6"), show="headings",
                            height=5)
        scroll = ttk.Scrollbar(self.gerateansicht_frame, orient='vertical', command=tree.yview)
        scroll.grid(row=0, column=1)
        tree.configure(yscrollcommand=scroll.set)

        tree.column("#1", anchor=CENTER, width=50)
        tree.heading("#1", text="das")
        tree.column("#2", anchor=CENTER, width=100)
        tree.heading("#2", text="ist")
        tree.column("#3", anchor=CENTER, width=200)
        tree.heading("#3", text="ein")
        tree.column("#4", anchor=CENTER, width=230)
        tree.heading("#4", text="Test")
        tree.column("#5", anchor=CENTER, width=235)
        tree.heading("#5", text="hilfe")
        tree.grid(row=0, column=0)

        # Positionierung
        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)
        verzeichniss.place(relx=0, rely=0.15, relwidth=0.15, relheight=0.85)
        login.place(relx=0.95, rely=0.5, anchor="center")
        profil.place(relx=0.90, rely=0.5, anchor="center")
        mainpage.place(relx=0.16, rely=0.16, anchor='nw')  # Anpassen der Position des mainpage-Buttons
