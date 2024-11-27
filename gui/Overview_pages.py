import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
import os
import gui_prototyp
import ThemeManager
import Mainpages
import configuration
import Profiles
from datetime import datetime
from tkinter import simpledialog
import sys

sys.path.append(os.path.join(os.path.dirname(__file__),'..'))

from db.SQLite_db import *


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
        # Styling
        style = ttk.Style()
        #style.theme_use("")
        style.configure("Treeview.Heading", font=("Inter", 12), background="#D9D9D9", foreground="#6E6893")
        style.configure("Treeview", font=("Arial", 11), rowheight=35, background="white", foreground="black")
        style.map("Treeview", background=[("selected", "#D9D9D9")], foreground=[("selected", "black")])
        style.configure("evenrow.Treeview", background="#f2f2f2")
        style.configure("oddrow.Treeview", background="white")

        tree = ttk.Treeview(self.tabelle_frame, columns=("c1", "c2", "c3", "c4", "c5"), show="headings",
                            height=5)
        scroll = ttk.Scrollbar(self.tabelle_frame, orient='vertical', command=tree.yview)
        # scroll.place(x=700, y=0.9, height=tree.winfo_height())
        tree.configure(yscrollcommand=scroll.set)

                # Spaltennamen aus der Datenbank holen
        items_uberschrift = fetch_items_headers()

        # Überschriften konfigurieren
        tree["columns"] = items_uberschrift
        for up in items_uberschrift:
            tree.column(up, anchor=CENTER, width=100)
            tree.heading(up, text=up)

        items_data = fetch_items()

        # Daten aus DB einfügen

        for i,row in enumerate(items_data):
            formatted_row = [value if value is not None else "-" for value in row] # Leere Felder durch "-" ersetzen
            color = "#f3f3f3" if i % 2 == 0 else "white"
            tree.insert("", "end", values=formatted_row, tags=("even" if i % 2 == 0 else "odd"))
            
        #Farben für Tags definieren
        tree.tag_configure("even", background="#f7f7f7")
        tree.tag_configure("odd", background="white")

        tree.place(x=120, y=0, width=1280, height=650)
        scroll.place(x=1400, y=0, height=650)
        # Setze explizite Mindesthöhe für Zeile 5
        #self.tabelle_frame.grid_rowconfigure(5, minsize=10)
        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)
        verzeichniss.place(relx=0, rely=0.15, relwidth=0.15, relheight=0.85)
        self.tabelle_frame.place(relx=0.15, rely=0.3, relwidth=0.85, height=800)

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

        name_frame = tk.Frame(self.gerateansicht_frame, bg='white', bd=0, relief="solid", highlightthickness=1, highlightbackground='#B8B7B7')
        name_frame.place(x=900, y=20, width=480, height=88)
        name_label = tk.Label(name_frame, text="Gerätename", bg='white', fg='#858383',
                              font=("Inter", 19))
        name_entry = tk.Entry(name_frame, bg='white', fg='black', font=("Inter", 16), bd=0)

        tag_frame = tk.Frame(self.gerateansicht_frame, bg='white', bd=0, relief="solid", highlightthickness=1, highlightbackground='#B8B7B7')

        tag_label = tk.Label(tag_frame, text="Seriennummer/Servicetag", bg='white', fg='#858383',
                              font=("Inter", 19))
        tag_entry = tk.Entry(tag_frame, bg='white', fg='black', font=("Inter", 16), bd=0)

        typ_frame = tk.Frame(self.gerateansicht_frame, bg='white', bd=0, relief="solid", highlightthickness=1, highlightbackground='#B8B7B7')
        typ_label = tk.Label(typ_frame, text="Gerätetyp", bg='white', fg='#858383',
                             font=("Inter", 19))
        typ_aktuell_label = tk.Label(typ_frame, text="PC", bg='white', fg='#858383',
                             font=("Inter", 19))
       #Dropdown Menü Typen
        typ_drop = tk.Button(typ_frame, text="↓", bd=0, bg='white',
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

        status_frame = tk.Frame(self.gerateansicht_frame, bg='white', bd=0, relief="solid", highlightthickness=1, highlightbackground='#B8B7B7')
        status_label = tk.Label(status_frame, text="Status", bg='white', fg='#858383',
                             font=("Inter", 19))
        status_aktuell_label = tk.Label(status_frame, text="✔ In Betrieb", bg='white', fg='#858383',
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

        # Dropdown Menü Status
        def status_dropdown():
            dropdown_menu = tk.Menu(status_frame, tearoff=0, bd=1, bg='white', fg='black')
            dropdown_menu.add_command(label=f"{'✔'.ljust(3)} in Betrieb", command=lambda: print("Produkt in Betrieb"))
            dropdown_menu.add_command(label=f"{'⛔'.ljust(1)} in Wartung", command=lambda: print("Produkt in Wartung"))
            dropdown_menu.add_command(label=f"{'⚠'.ljust(1)} Beschädigt", command=lambda: print("Produkt beschädigt"))
            dropdown_menu.add_command(label=f"{'✔'.ljust(2)} verfügbar", command=lambda: print("Produkt zum Mieten bereit"))
            dropdown_menu.add_command(label=f"{'❌'.ljust(3)} gemietet", command=lambda: print("Produkt gemietet"))

            dropdown_menu.post(
                status_drop.winfo_rootx() - 62,  # Verschiebt das Menü 50 Pixel nach links
                status_drop.winfo_rooty() + status_drop.winfo_height()
            )

        standort_frame = tk.Frame(self.gerateansicht_frame, bg='white', bd=0, relief="solid", highlightthickness=1, highlightbackground='#B8B7B7')
        standort_label = tk.Label(standort_frame, text="Standort", bg='white', fg='#858383',
                             font=("Inter", 19))
        standort_entry = tk.Entry(standort_frame, bg='white', fg='black', font=("Inter", 16), bd=0)

        #Button
        buttons_frame = tk.Frame(self.gerateansicht_frame, bg='white', bd=0, relief="solid")
        #Img definitionen
        self.schaeden_img = gui_prototyp.load_image(root_path+"/gui/assets/Button_Schaeden.png")
        self.buchung_img = gui_prototyp.load_image(root_path+"/gui/assets/Button_Buchung.png")
        self.speichern_img = gui_prototyp.load_image(root_path+"/gui/assets/Button_Speichern.png")
        self.upload_img = gui_prototyp.load_image(root_path + "/gui/assets/Button_PicDrop.png")

        # Button Bilder hochladen
        upload_frame = tk.Frame(self.gerateansicht_frame, bg='white')
        upload_button = tk.Button(upload_frame, image=self.upload_img, bd=0, bg='white',
                                  command=lambda: print("Bild hochgeladen"))
        #Button Schäden
        def open_schaeden_page():
            schaeden_page = tk.Toplevel()#root
            schaeden_page.title("Schäden eintragen")
            schaeden_page.geometry("819x594+500+300")
            schaeden_page.configure(bg='white')

            schaeden_page.grab_set()
            #Bilder
            self.aktualisieren_img = gui_prototyp.load_image(root_path+"/gui/assets/Button_Aktualisieren.png")
            self.upload_img = gui_prototyp.load_image(root_path+"/gui/assets/Button_Drop.png")

            #Informationen
            info_frame = tk.Frame(schaeden_page, bg='white', bd=1)
            verlauf_frame = tk.Frame(schaeden_page, bg='white', bd=1)

            name_label = tk.Label(info_frame, text="Gerätename", bg='white',
                                      font=("Inter", 19))
            name_entry = tk.Entry(info_frame, bg= '#D9D9D9', bd=0,
                                      font=("Inter", 19, 'italic'))

            tag_label = tk.Label(info_frame, text="Servicetag", bg='white',
                                      font=("Inter", 19))
            tag_entry = tk.Entry(info_frame, bg='#D9D9D9', bd=0,
                                      font=("Inter", 19, 'italic'))

            date_label = tk.Label(info_frame, text="Datum", bg='white',
                                 font=("Inter", 19))
            date_entry = datetime.now().strftime("%d.%m.%Y")
            current_date = tk.Label(info_frame, text=date_entry, font=("Arial", 14), bg='#D9D9D9', fg='black', bd=0)


            beschreibung_label = tk.Label(info_frame, text="Beschreibung", bg='white',
                                 font=("Inter", 19))
            beschreibung_entry = tk.Entry(info_frame, bg='#D9D9D9', bd=0,
                                 font=("Inter", 19, 'italic'))
            #Verlauf
            verlauf_label = tk.Label(verlauf_frame, text="Verlauf", bg='white',
                                 font=("Inter", 19))
            verlauf_inh_label = tk.Entry(verlauf_frame, bg='#D9D9D9', bd=0,
                                 font=("Inter", 19, 'italic'))
            #Buttons
            schaeden_button_frame = tk.Frame(schaeden_page, bg='white', bd=1)
            close_button = tk.Button(schaeden_button_frame, image=self.aktualisieren_img, bd=0, bg='white', command=schaeden_page.destroy)
            upload_button = tk.Button(schaeden_button_frame, image=self.upload_img, bd=0, bg='white', command=lambda: print("Bild hochgeladen"))

            #Placement
            name_label.place(x=0, y=2)
            name_entry.place(x=150, y=2, width=150)

            tag_label.place(x=0, y=52)
            tag_entry.place(x=150, y=52, width=150)

            date_label.place(x=0, y=102)
            current_date.place(x=150, y=102)

            beschreibung_label.place(x=0, y=152)
            beschreibung_entry.place(x=10, y=202, width=380, height=382)

            verlauf_label.place(x=15, y=0)
            verlauf_inh_label.place(x=15, y=50, width=380, height=382)

            upload_button.place(x=10, y=10)
            close_button.place(x=200, y=40)
            info_frame.place(x=0, y=0, width=409, height=594)
            verlauf_frame.place(x=409, y=0, width=409, height=444)
            schaeden_button_frame.place(x=409, y=444, width=409, height=150)

        #Funktion zuende

        schaeden_button = tk.Button(buttons_frame, image=self.schaeden_img, bd=0, bg='white', command=open_schaeden_page)
        schaeden_button.place(x=10, y=10)

        def open_buchen_page():
            buchen_page = tk.Toplevel()  # root
            buchen_page.title("Gerät buchen")
            buchen_page.geometry("819x594+500+300")
            buchen_page.configure(bg='white')

            buchen_page.grab_set()
            # Bilder
            self.aktualisieren_img = gui_prototyp.load_image(root_path + "/gui/assets/Button_Aktualisieren.png")

            # Informationen
            info_frame = tk.Frame(buchen_page, bg='white', bd=1)
            date_frame = tk.Frame(buchen_page, bg='white', bd=1)

            name_label = tk.Label(info_frame, text="Gerätename", bg='white',
                                  font=("Inter", 19))
            name_entry = tk.Entry(info_frame, bg='#D9D9D9', bd=0,
                                  font=("Inter", 19, 'italic'))

            tag_label = tk.Label(info_frame, text="Servicetag", bg='white',
                                 font=("Inter", 19))
            tag_entry = tk.Entry(info_frame, bg='#D9D9D9', bd=0,
                                 font=("Inter", 19, 'italic'))

            verlauf_label = tk.Label(info_frame, text="Verlauf", bg='white',
                                          font=("Inter", 19))
            verlauf_entry = tk.Entry(info_frame, bg='#D9D9D9', bd=0,
                                          font=("Inter", 19, 'italic'))
            #Datum
            def ask_startdate():
                # Benutzer nach Datum fragen
                entered_date = simpledialog.askstring("Datum", "Startdatum (Format: DD.MM.YYYY:)")
                try:
                    # Datum validieren
                    datetime.strptime(entered_date, "%d.%m.%Y")
                    start_result_label.config(text=f"von: {entered_date}")
                except ValueError:
                    start_result_label.config(text="Ungültiges Datum! Bitte erneut eingeben.")
                # Button zur Datumseingabe

            ask_date_button = tk.Button(date_frame, text="Startdatum eingeben", command=ask_startdate)
            ask_date_button.place(x=0, y=0)

            start_result_label = tk.Label(date_frame, text="Kein Datum ausgewählt", font=("Arial", 14))
            start_result_label.place(x=150, y=0)
            def ask_enddate():
                # Benutzer nach Datum fragen
                entered_date = simpledialog.askstring("Datum", "Enddatum (Format: DD.MM.YYYY:)")
                try:
                    # Datum validieren
                    datetime.strptime(entered_date, "%d.%m.%Y")
                    end_result_label.config(text=f"bis: {entered_date}")
                except ValueError:
                    end_result_label.config(text="Ungültiges Datum! Bitte erneut eingeben.")
                # Button zur Datumseingabe

            ask_date_button = tk.Button(date_frame, text="Enddatum eingeben", command=ask_enddate)
            ask_date_button.place(x=0, y=100)
            # Ergebnis-Label
            end_result_label = tk.Label(date_frame, text="Kein Datum ausgewählt", font=("Arial", 14))
            end_result_label.place(x=150, y=100)

            # Buttons
            buchen_button_frame = tk.Frame(buchen_page, bg='white', bd=1)
            close_button = tk.Button(buchen_button_frame, image=self.aktualisieren_img, bd=0, bg='white',
                                     command=buchen_page.destroy)


            # Placement
            name_label.place(x=0, y=2)
            name_entry.place(x=150, y=2, width=150)

            tag_label.place(x=0, y=52)
            tag_entry.place(x=150, y=52, width=150)

            verlauf_label.place(x=0, y=152)
            verlauf_entry.place(x=10, y=202, width=380, height=382)

            close_button.place(x=200, y=40)
            info_frame.place(x=0, y=0, width=409, height=594)
            date_frame.place(x=409, y=0, width=409, height=444)
            buchen_button_frame.place(x=409, y=444, width=409, height=150)

        # Funktion zuende
        # Button Buchung
        buchung_button = tk.Button(buttons_frame, image=self.buchung_img, bd=0, bg='white',
                                       command=open_buchen_page)
        buchung_button.place(x=10, y=80)

        #Button Speichern
        def button_click():
            controller.show_frame(Ubersicht)
            messagebox.showinfo("yippie","Änderungen erfolgreich gespeichert")
        speichern_button = tk.Button(buttons_frame, image=self.speichern_img, bd=0, bg='white', command=button_click)
        speichern_button.place(x=10, y=150)


        #Verzeichniss
        # "Alle Anzeigen" Button in der Seitenleiste
        all_button = tk.Button(verzeichniss, text="Alle anzeigen", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                               font=("Inter", 20, 'bold'),
                               command=lambda: controller.show_frame(Ubersicht))

        all_button.pack(pady=10, anchor='w')
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

        # Positionierung
        name_label.grid(row=5, column=5, pady=10)
        name_entry.place(x=5, y=50, width=200)
        tag_label.grid(row=5, column=5, pady=10)
        tag_entry.place(x=5, y=50, width=200)
        typ_label.grid(row=5, column=5, pady=10)
        typ_aktuell_label.place(x=5, y=50, width=200)
        status_label.grid(row=5, column=5, pady=10)
        status_aktuell_label.place(x=5, y=50, width=200)
        standort_label.grid(row=5, column=5, pady=10)
        standort_entry.place(x=5, y=50, width=200)
        upload_button.place(x=100, y=0)

        upload_frame.place(x=0, y=520, relwidth=0.40, height=300)
        tag_frame.place(x=900, y=120, width=480, height=88)
        typ_frame.place(x=900, y=220, width=480, height=88)
        status_frame.place(x=900, y=320, width=480, height=88)
        standort_frame.place(x=900, y=420, width=480, height=88)
        buttons_frame.place(x=900, y=520, width=480, height=300)


        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)
        verzeichniss.place(relx=0, rely=0.15, relwidth=0.15, relheight=0.85)
        login.place(relx=0.95, rely=0.5, anchor="center")
        profil.place(relx=0.90, rely=0.5, anchor="center")
        mainpage.place(relx=0.16, rely=0.16, anchor='nw')  # Anpassen der Position des mainpage-Buttons
