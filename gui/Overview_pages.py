import tkinter as tk
from tkinter import ttk
from tkinter import *
import os
import gui_prototyp
import ThemeManager
import Mainpages
import configuration
import Profiles


class Ubersicht(tk.Frame):
    """Repraesentiert die Geraeteuebersichtsseite der Anwendung. Zeigt eine Liste oder Tabelle der verfügbaren
       Geräte und bietet Optionen für die Navigation zurück zur Hauptseite, zum Login und zu Benutzerprofilen """

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
        self.ubersicht_frame.place(relx=0.21, rely=0.15, relwidth=1, relheight=0.85)

        # Layout Festlegung der flexiblen Skalierung der Übersichtsseite
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)

        # Laden der Bilder für die Navigation und Header Buttons
        self.imglogin = gui_prototyp.load_image(root_path+"/gui/assets/Closeicon.png")
        self.imgprofil = gui_prototyp.load_image(root_path+"/gui/assets/profileicon.png")

        # Login und Profil Buttons im Header-Bereich, Platzierung der Buttons, Header und Sidebar
        login = tk.Button(header, image=self.imglogin, bd=0, bg=ThemeManager.SRH_Orange,
                          command=lambda: controller.show_frame(gui_prototyp.LogInWindow))
        profil = tk.Button(header, image=self.imgprofil, bd=0, bg=ThemeManager.SRH_Orange,
                           command=lambda: controller.show_frame(Profiles.Profil))
        self.imgmainpage = tk.PhotoImage(
            file=root_path+"/gui/assets/backtosite_icon.png")

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
            dropdown_menu.add_command(label="→ Andere", command=lambda: controller.show_frame(configuration))
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
            dropdown_menu.add_command(label="→ Andere", command=lambda: controller.show_frame(configuration))
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
            dropdown_menu.add_command(label="→ Andere", command=lambda: controller.show_frame(configuration))
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
            dropdown_menu.add_command(label="→ Andere", command=lambda: controller.show_frame(configuration))
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
            dropdown_menu.add_command(label="→ Andere", command=lambda: controller.show_frame(configuration))
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
            dropdown_menu.add_command(label="→ Andere", command=lambda: controller.show_frame(configuration))
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
            dropdown_menu.add_command(label="→ Andere", command=lambda: controller.show_frame(configuration))
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
            dropdown_menu.add_command(label="→ Andere", command=lambda: controller.show_frame(configuration))
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
        self.imgFilter = gui_prototyp.load_image(root_path+"/gui/assets/Filter_Button.png")
        self.imgSuche = gui_prototyp.load_image(root_path+"/gui/assets/Search.png")
        self.imgHinzufugen = gui_prototyp.load_image(root_path+"/gui/assets/Adding_Icon.png")
        self.imgAktionen = gui_prototyp.load_image(root_path+"/gui/assets/Aktionen_Button.png")

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
        root_path = os.path.dirname(os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir)))
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
        self.imglogin = tk.PhotoImage(file=root_path+"/gui/assets/Closeicon.png")
        self.imgmainpage = tk.PhotoImage(file=root_path+"/gui/assets/backtosite_grey_icon.png")
        self.imgprofil = gui_prototyp.load_image(root_path+"/gui/assets/profileicon.png")

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
        tree = ttk.Treeview(self.gerateansicht_frame, columns=("c1", "c2", "c3"), show="headings",
                            height=5)
        scroll = ttk.Scrollbar(self.gerateansicht_frame, orient='vertical', command=tree.yview)
        #scroll.place(x=700, y=0.9, height=tree.winfo_height())
        tree.configure(yscrollcommand=scroll.set)

        tree.column("#1", anchor=CENTER, width=50)
        tree.heading("#1", text="Benutzer")
        tree.column("#2", anchor=CENTER, width=100)
        tree.heading("#2", text="Datum")
        tree.column("#3", anchor=CENTER, width=200)
        tree.heading("#3", text="Änderung")
        tree.place(x=0, y=20, relwidth=0.40, relheight=0.5)
        scroll.place(x=770, y=20, relheight=0.5)

        name_frame = tk.Frame(self.gerateansicht_frame, bg='white', bd=1, relief="solid")
        name_frame.place(x=900, y=20, width=480, height=88)
        name_label = tk.Label(name_frame, text="Gerätename", bg='white',
                              font=("Inter", 19))

        tag_frame = tk.Frame(self.gerateansicht_frame, bg='white', bd=1, relief="solid")

        tag_label = tk.Label(tag_frame, text="Seriennummer/Servicetag", bg='white',
                              font=("Inter", 19))

        typ_frame = tk.Frame(self.gerateansicht_frame, bg='white', bd=1, relief="solid")
        typ_label = tk.Label(typ_frame, text="Gerätetyp", bg='white',
                             font=("Inter", 19))
       #Dropdown Menü Typen
        typ_drop = tk.Button(typ_frame, text="↓", bd=0, bg='white',
                                fg=ThemeManager.SRH_Grey,
                                font=("Inter", 20, 'bold'),
                                command=lambda: controller.show_frame())
        typ_drop = tk.Button(typ_frame, text="Typ", bd=0, bg='white', fg='black',
                                font=("Inter", 20, 'bold'),
                                command=lambda: controller.show_frame())
        typ_drop = tk.Button(typ_frame, text="↓", bd=0, bg='white', fg='black',
                                font=("Inter", 20, 'bold'),
                                command=lambda: typ_dropdown())  # Button öffnet Dropdown-Menü
        typ_drop.place(x=420, y=30)
        def typ_dropdown():
            dropdown_menu = tk.Menu(typ_frame, tearoff=0, bd=1, bg='white', fg='black')
            dropdown_menu.add_command(label="→ PC", command=lambda: print("PC ausgewählt"))
            dropdown_menu.add_command(label="→ Laptop", command=lambda: print("Laptop ausgewählt"))
            dropdown_menu.add_command(label="→ Bildschirm", command=lambda: print("Bildschirm ausgewählt"))
            dropdown_menu.add_command(label="→ Raspberrypie", command=lambda: print("Raspberrypie ausgewählt"))
            dropdown_menu.add_command(label="→ Dockingstation", command=lambda: print("Dockingstation ausgewählt"))
            dropdown_menu.add_command(label="→ Drucker", command=lambda: print("Drucker ausgewählt"))
            dropdown_menu.add_command(label="→ Kabel", command=lambda: print("Kabel ausgewählt"))
            dropdown_menu.add_command(label="→ Peripherie", command=lambda: print("Peripherie ausgewählt"))
            dropdown_menu.add_command(label="→ Sonstiges", command=lambda: print("Sonstiges ausgewählt"))

            dropdown_menu.post(
                typ_drop.winfo_rootx() - 77,
                typ_drop.winfo_rooty() + typ_drop.winfo_height()
            )

        status_frame = tk.Frame(self.gerateansicht_frame, bg='white', bd=1, relief="solid")
        status_label = tk.Label(status_frame, text="Status", bg='white',
                             font=("Inter", 19))

        status_drop = tk.Button(status_frame, text="↓", bd=0, bg='white',
                             fg=ThemeManager.SRH_Grey,
                             font=("Inter", 20, 'bold'),
                             command=lambda: controller.show_frame())
        status_drop = tk.Button(status_frame, text="Status", bd=0, bg='white', fg='black',
                             font=("Inter", 20, 'bold'),
                             command=lambda: controller.show_frame())
        status_drop = tk.Button(status_frame, text="↓", bd=0, bg='white', fg='black',
                             font=("Inter", 20, 'bold'),
                             command=lambda: status_dropdown())  # Button öffnet Dropdown-Menü
        status_drop.place(x=420, y=30)
        def status_dropdown():
            dropdown_menu = tk.Menu(status_frame, tearoff=0, bd=1, bg='white', fg='black')
            dropdown_menu.add_command(label=f"{'✔'.ljust(3)} in Betrieb", command=lambda: print("Produkt in Betrieb"))
            dropdown_menu.add_command(label=f"{'⛔'.ljust(1)} in Wartung", command=lambda: print("Produkt in Wartung"))
            dropdown_menu.add_command(label=f"{'⚠'.ljust(1)} Beschädigt", command=lambda: print("Produkt beschädigt"))
            dropdown_menu.add_command(label=f"{'✔'.ljust(2)} verfügbar", command=lambda: print("Produkt zum Mieten bereit"))
            dropdown_menu.add_command(label=f"{'❌'.ljust(3)} gemietet", command=lambda: print("Produkt gemietet"))

            dropdown_menu.post(
                status_drop.winfo_rootx() - 77,  # Verschiebt das Menü 50 Pixel nach links
                status_drop.winfo_rooty() + status_drop.winfo_height()
            )

        standort_frame = tk.Frame(self.gerateansicht_frame, bg='white', bd=1, relief="solid")
        standort_frame.place(x=900, y=420, width=480, height=88)
        standort_label = tk.Label(standort_frame, text="Standort", bg='white',
                             font=("Inter", 19))

        # Positionierung
        name_label.grid(row=5, column=5, pady=10)
        tag_label.grid(row=5, column=5, pady=10)
        typ_label.grid(row=5, column=5, pady=10)
        status_label.grid(row=5, column=5, pady=10)
        standort_label.grid(row=5, column=5, pady=10)

        tag_frame.place(x=900, y=120, width=480, height=88)
        typ_frame.place(x=900, y=220, width=480, height=88)
        status_frame.place(x=900, y=320, width=480, height=88)
        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)
        verzeichniss.place(relx=0, rely=0.15, relwidth=0.15, relheight=0.85)
        login.place(relx=0.95, rely=0.5, anchor="center")
        profil.place(relx=0.90, rely=0.5, anchor="center")
        mainpage.place(relx=0.16, rely=0.16, anchor='nw')  # Anpassen der Position des mainpage-Buttons
