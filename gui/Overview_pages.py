#########################
#       Imports         #
#########################
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
import customtkinter as ctk
from customtkinter import *

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
    """
    Initialisiert eine Klasse zur Darstellung der Geräteübersichtsseite innerhalb einer Anwendung.

    Diese Klasse konfiguriert Layout, Stil und Aktionen für die Benutzerinteraktion auf der Geräteübersichtsseite,
    einschließlich Navigation, Geräteliste und Filterfunktionen.

    **Args:**
    parent (tk.Widget): Das übergeordnete Widget, in das dieser Frame eingebettet wird.
    controller (object): Eine Instanz für die Verwaltung und den Wechsel zwischen verschiedenen Anwendungsansichten.

    **Methods:**

    show_dropdown_grp1() - show_dropdown_grp8(): Zeigt Dropdown-Menüs für verschiedene Gerätegruppen an.
    show_dropdown_Filter(): Zeigt ein Dropdown-Menü für die Filteroptionen an.
    on_item_select(event): Reagiert auf die Auswahl von Geräten innerhalb der Tabelle und zeigt Details an.

    **Raises:**
    tk.TclError: Falls es ein Problem beim Laden von Bildern gibt.

    **Attributes:**

    :ivar ubersicht_frame: A frame for displaying the main content area.
    :type ubersicht_frame: tk.Frame
    :ivar tabelle_frame: A frame for displaying tabular data or lists.
    :type tabelle_frame: tk.Frame
    - imglogin (PhotoImage): Bild für das Login-Symbol im Header.
    - imgprofil (PhotoImage): Bild für das Profil-Symbol im Header.
    - imgmainpage (PhotoImage): Bild für das Symbol, um zur Hauptseite zurückzukehren.
    - imgFilter, imgSuche, imgHinzufugen, imgAktionen (PhotoImage): Bilder für Filter-, Such-, Hinzufügen- und Aktionsbuttons.
    """

    def __init__(self, parent, controller):
        """

        """
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
        login = ctk.CTkButton(header, image=self.imglogin, fg_color=ThemeManager.SRH_Orange,
                              bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                              hover=True, hover_color='#e25a1f', text="",
                              command=lambda: controller.show_frame(gui_prototyp.LogInWindow))

        profil = ctk.CTkButton(header, image=self.imgprofil, fg_color=ThemeManager.SRH_Orange,
                               bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                               hover=True, hover_color='#e25a1f', text="",
                               command=lambda: controller.show_frame(Profiles.Profil))
        self.imgmainpage = tk.PhotoImage(
            file=root_path+"/gui/assets/backtosite_icon.png")

        login.place(relx=0.95, rely=0.5, anchor="center")
        profil.place(relx=0.90, rely=0.5, anchor="center")

        tk.Button(header, image=self.imgmainpage, bd=0, bg=ThemeManager.SRH_Orange,
                  command=lambda: controller.show_frame(Mainpages.MainPage))

        # "Alle Anzeigen" Button in der Seitenleiste
        all_button = ctk.CTkButton(verzeichniss, text="Alle Anzeigen", fg_color=ThemeManager.SRH_Grey, text_color='black',
                            font=("Inter", 20), corner_radius=8, hover=False,
                            command=lambda: controller.show_frame(Overview_pages.Ubersicht))

        all_button.pack(pady=10, anchor='w')

        # Gruppe 1
        def show_dropdown_grp1():
            """
            Die Methode `show_dropdown_grpx` erstellt und zeigt ein Dropdown-Menü für die erste Gerätegruppe an.
            Dieses Menü enthält verschiedene Optionen wie Hardware, Software, Peripherie und Andere, die bei Auswahl den Benutzer zu entsprechenden Ansichten innerhalb der Anwendung navigieren lassen.
            Das Menü wird an der Position des zugehörigen Buttons im Fenster angezeigt.

            **Methods:**

            - *tk.Menu* erstellt ein Dropdown im Frame "Verzeichniss"
            - *add_command* fügt Auswahlmöglichkeiten hinzu
            - *command=lambda: controller.show_frame(xxx)* öffnet beim Anklicken einer Möglichkeit ein Fenster

            """
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg=ThemeManager.SRH_Grey, fg='black')
            dropdown_menu.add_command(label="→ Hardware", command=lambda: controller.show_frame(Profiles.Admin))
            dropdown_menu.add_command(label="→ Software", command=lambda: controller.show_frame(Profiles.Stats))
            dropdown_menu.add_command(label="→ Peripherie", command=lambda: controller.show_frame(Profiles.Profil))
            dropdown_menu.add_command(label="→ Andere", command=lambda: controller.show_frame(configuration))
            dropdown_menu.post(grp1_button.winfo_rootx(), grp1_button.winfo_rooty() + grp1_button.winfo_height())

        grp1_button = tk.Button(verzeichniss, text="Gruppe 1   ", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=show_dropdown_grp1) #Text, der im Verzeichniss liegt (benutzt Funktion show_dropdown_grpx
        grp1_button.pack(pady=10, anchor='w') # Platzierung

        # Gruppe 2
        def show_dropdown_grp2():
            """
            Die Methode `show_dropdown_grpx` erstellt und zeigt ein Dropdown-Menü für die erste Gerätegruppe an.
            Dieses Menü enthält verschiedene Optionen wie Hardware, Software, Peripherie und Andere, die bei Auswahl den Benutzer zu entsprechenden Ansichten innerhalb der Anwendung navigieren lassen.
            Das Menü wird an der Position des zugehörigen Buttons im Fenster angezeigt.

            **Methods:**

            - *tk.Menu* erstellt ein Dropdown im Frame "Verzeichniss"
            - *add_command* fügt Auswahlmöglichkeiten hinzu
            - *command=lambda: controller.show_frame(xxx)* öffnet beim Anklicken einer Möglichkeit ein Fenster

            """
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg=ThemeManager.SRH_Grey, fg='black')
            dropdown_menu.add_command(label="→ Hardware", command=lambda: controller.show_frame(Profiles.Admin))
            dropdown_menu.add_command(label="→ Software", command=lambda: controller.show_frame(Profiles.Stats))
            dropdown_menu.add_command(label="→ Peripherie", command=lambda: controller.show_frame(Profiles.Profil))
            dropdown_menu.add_command(label="→ Andere", command=lambda: controller.show_frame(configuration))
            dropdown_menu.post(grp2_button.winfo_rootx(), grp2_button.winfo_rooty() + grp2_button.winfo_height())

        grp2_button = tk.Button(verzeichniss, text="Gruppe 2   ", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=show_dropdown_grp2) #Text, der im Verzeichniss liegt (benutzt Funktion show_dropdown_grpx
        grp2_button.pack(pady=10, anchor='w') # Platzierung

        # Gruppe 3
        def show_dropdown_grp3():
            """
            Die Methode `show_dropdown_grpx` erstellt und zeigt ein Dropdown-Menü für die erste Gerätegruppe an.
            Dieses Menü enthält verschiedene Optionen wie Hardware, Software, Peripherie und Andere, die bei Auswahl den Benutzer zu entsprechenden Ansichten innerhalb der Anwendung navigieren lassen.
            Das Menü wird an der Position des zugehörigen Buttons im Fenster angezeigt.

            **Methods:**

            - *tk.Menu* erstellt ein Dropdown im Frame "Verzeichniss"
            - *add_command* fügt Auswahlmöglichkeiten hinzu
            - *command=lambda: controller.show_frame(xxx)* öffnet beim Anklicken einer Möglichkeit ein Fenster

            """
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg=ThemeManager.SRH_Grey, fg='black')
            dropdown_menu.add_command(label="→ Hardware", command=lambda: controller.show_frame(Profiles.Admin))
            dropdown_menu.add_command(label="→ Software", command=lambda: controller.show_frame(Profiles.Stats))
            dropdown_menu.add_command(label="→ Peripherie", command=lambda: controller.show_frame(Profiles.Profil))
            dropdown_menu.add_command(label="→ Andere", command=lambda: controller.show_frame(configuration))
            dropdown_menu.post(grp3_button.winfo_rootx(), grp3_button.winfo_rooty() + grp3_button.winfo_height())

        grp3_button = tk.Button(verzeichniss, text="Gruppe 3   ", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=show_dropdown_grp3) #Text, der im Verzeichniss liegt (benutzt Funktion show_dropdown_grpx
        grp3_button.pack(pady=10, anchor='w') # Platzierung

        # Gruppe 4
        def show_dropdown_grp4():
            """
            Die Methode `show_dropdown_grpx` erstellt und zeigt ein Dropdown-Menü für die erste Gerätegruppe an.
            Dieses Menü enthält verschiedene Optionen wie Hardware, Software, Peripherie und Andere, die bei Auswahl den Benutzer zu entsprechenden Ansichten innerhalb der Anwendung navigieren lassen.
            Das Menü wird an der Position des zugehörigen Buttons im Fenster angezeigt.

            **Methods:**

            - *tk.Menu* erstellt ein Dropdown im Frame "Verzeichniss"
            - *add_command* fügt Auswahlmöglichkeiten hinzu
            - *command=lambda: controller.show_frame(xxx)* öffnet beim Anklicken einer Möglichkeit ein Fenster

            """
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg=ThemeManager.SRH_Grey, fg='black')
            dropdown_menu.add_command(label="→ Hardware", command=lambda: controller.show_frame(Profiles.Admin))
            dropdown_menu.add_command(label="→ Software", command=lambda: controller.show_frame(Profiles.Stats))
            dropdown_menu.add_command(label="→ Peripherie", command=lambda: controller.show_frame(Profiles.Profil))
            dropdown_menu.add_command(label="→ Andere", command=lambda: controller.show_frame(configuration))
            dropdown_menu.post(grp4_button.winfo_rootx(), grp4_button.winfo_rooty() + grp4_button.winfo_height())

        grp4_button = tk.Button(verzeichniss, text="Gruppe 4   ", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=show_dropdown_grp4) #Text, der im Verzeichniss liegt (benutzt Funktion show_dropdown_grpx
        grp4_button.pack(pady=10, anchor='w') # Platzierung

        # Gruppe 5
        def show_dropdown_grp5():
            """
            Die Methode `show_dropdown_grpx` erstellt und zeigt ein Dropdown-Menü für die erste Gerätegruppe an.
            Dieses Menü enthält verschiedene Optionen wie Hardware, Software, Peripherie und Andere, die bei Auswahl den Benutzer zu entsprechenden Ansichten innerhalb der Anwendung navigieren lassen.
            Das Menü wird an der Position des zugehörigen Buttons im Fenster angezeigt.

            **Methods:**

            - *tk.Menu* erstellt ein Dropdown im Frame "Verzeichniss"
            - *add_command* fügt Auswahlmöglichkeiten hinzu
            - *command=lambda: controller.show_frame(xxx)* öffnet beim Anklicken einer Möglichkeit ein Fenster

            """
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg=ThemeManager.SRH_Grey, fg='black')
            dropdown_menu.add_command(label="→ Hardware", command=lambda: controller.show_frame(Profiles.Admin))
            dropdown_menu.add_command(label="→ Software", command=lambda: controller.show_frame(Profiles.Stats))
            dropdown_menu.add_command(label="→ Peripherie", command=lambda: controller.show_frame(Profiles.Profil))
            dropdown_menu.add_command(label="→ Andere", command=lambda: controller.show_frame(configuration))
            dropdown_menu.post(grp5_button.winfo_rootx(), grp5_button.winfo_rooty() + grp5_button.winfo_height())

        grp5_button = tk.Button(verzeichniss, text="Gruppe 5   ", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=show_dropdown_grp5) #Text, der im Verzeichniss liegt (benutzt Funktion show_dropdown_grpx
        grp5_button.pack(pady=10, anchor='w') # Platzierung

        # Gruppe 6
        def show_dropdown_grp6():
            """
            Die Methode `show_dropdown_grpx` erstellt und zeigt ein Dropdown-Menü für die erste Gerätegruppe an.
            Dieses Menü enthält verschiedene Optionen wie Hardware, Software, Peripherie und Andere, die bei Auswahl den Benutzer zu entsprechenden Ansichten innerhalb der Anwendung navigieren lassen.
            Das Menü wird an der Position des zugehörigen Buttons im Fenster angezeigt.

            **Methods:**

            - *tk.Menu* erstellt ein Dropdown im Frame "Verzeichniss"
            - *add_command* fügt Auswahlmöglichkeiten hinzu
            - *command=lambda: controller.show_frame(xxx)* öffnet beim Anklicken einer Möglichkeit ein Fenster

            """
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg=ThemeManager.SRH_Grey, fg='black')
            dropdown_menu.add_command(label="→ Hardware", command=lambda: controller.show_frame(Profiles.Admin))
            dropdown_menu.add_command(label="→ Software", command=lambda: controller.show_frame(Profiles.Stats))
            dropdown_menu.add_command(label="→ Peripherie", command=lambda: controller.show_frame(Profiles.Profil))
            dropdown_menu.add_command(label="→ Andere", command=lambda: controller.show_frame(configuration))
            dropdown_menu.post(grp6_button.winfo_rootx(), grp6_button.winfo_rooty() + grp6_button.winfo_height())

        grp6_button = tk.Button(verzeichniss, text="Gruppe 6   ", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=show_dropdown_grp6) #Text, der im Verzeichniss liegt (benutzt Funktion show_dropdown_grpx
        grp6_button.pack(pady=10, anchor='w') # Platzierung

        # Gruppe 7
        def show_dropdown_grp7():
            """
            Die Methode `show_dropdown_grpx` erstellt und zeigt ein Dropdown-Menü für die erste Gerätegruppe an.
            Dieses Menü enthält verschiedene Optionen wie Hardware, Software, Peripherie und Andere, die bei Auswahl den Benutzer zu entsprechenden Ansichten innerhalb der Anwendung navigieren lassen.
            Das Menü wird an der Position des zugehörigen Buttons im Fenster angezeigt.

            **Methods:**

            - *tk.Menu* erstellt ein Dropdown im Frame "Verzeichniss"
            - *add_command* fügt Auswahlmöglichkeiten hinzu
            - *command=lambda: controller.show_frame(xxx)* öffnet beim Anklicken einer Möglichkeit ein Fenster

            """
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg=ThemeManager.SRH_Grey, fg='black')
            dropdown_menu.add_command(label="→ Hardware", command=lambda: controller.show_frame(Profiles.Admin))
            dropdown_menu.add_command(label="→ Software", command=lambda: controller.show_frame(Profiles.Stats))
            dropdown_menu.add_command(label="→ Peripherie", command=lambda: controller.show_frame(Profiles.Profil))
            dropdown_menu.add_command(label="→ Andere", command=lambda: controller.show_frame(configuration))
            dropdown_menu.post(grp7_button.winfo_rootx(), grp7_button.winfo_rooty() + grp7_button.winfo_height())

        grp7_button = tk.Button(verzeichniss, text="Gruppe 7   ", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=show_dropdown_grp7) #Text, der im Verzeichniss liegt (benutzt Funktion show_dropdown_grpx
        grp7_button.pack(pady=10, anchor='w') # Platzierung

        # Gruppe 8
        def show_dropdown_grp8():
            """
            Die Methode `show_dropdown_grpx` erstellt und zeigt ein Dropdown-Menü für die erste Gerätegruppe an.
            Dieses Menü enthält verschiedene Optionen wie Hardware, Software, Peripherie und Andere, die bei Auswahl den Benutzer zu entsprechenden Ansichten innerhalb der Anwendung navigieren lassen.
            Das Menü wird an der Position des zugehörigen Buttons im Fenster angezeigt.

            **Methods:**

            - *tk.Menu* erstellt ein Dropdown im Frame "Verzeichniss"
            - *add_command* fügt Auswahlmöglichkeiten hinzu
            - *command=lambda: controller.show_frame(xxx)* öffnet beim Anklicken einer Möglichkeit ein Fenster

            """
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg=ThemeManager.SRH_Grey, fg='black')
            dropdown_menu.add_command(label="→ Hardware", command=lambda: controller.show_frame(Profiles.Admin))
            dropdown_menu.add_command(label="→ Software", command=lambda: controller.show_frame(Profiles.Stats))
            dropdown_menu.add_command(label="→ Peripherie", command=lambda: controller.show_frame(Profiles.Profil))
            dropdown_menu.add_command(label="→ Andere", command=lambda: controller.show_frame(configuration))
            dropdown_menu.post(grp8_button.winfo_rootx(), grp8_button.winfo_rooty() + grp8_button.winfo_height())

        grp8_button = tk.Button(verzeichniss, text="Gruppe 8   ", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=show_dropdown_grp8) #Text, der im Verzeichniss liegt (benutzt Funktion show_dropdown_grpx
        grp8_button.pack(pady=10, anchor='w') # Platzierung

        # Bilder
        self.imgFilter = gui_prototyp.load_image(root_path+"/gui/assets/Filter_Button.png")
        self.imgSuche = gui_prototyp.load_image(root_path+"/gui/assets/Search.png")
        self.imgHinzufugen = gui_prototyp.load_image(root_path+"/gui/assets/Adding_Icon.png")
        self.imgAktionen = gui_prototyp.load_image(root_path+"/gui/assets/Aktionen_Button.png")

        # Filterfunktion
        def show_dropdown_Filter():
            """
            Erstellt und zeigt ein Dropdown-Menü für Filteroptionen zur Sortierung von Geräten an.
            Diese Funktion generiert ein Kontextmenü mit verschiedenen Filteroptionen, das an der Position des Filter-Buttons angezeigt wird.

            **Args:**

            Keine direkt übergebenen Argumente.

            **Attributes:**

            Filter_button (tk.Button): Button, der das Dropdown-Menü für Filteroptionen anzeigt und positioniert.

            **Verwendet:**

            dropdown_menu (tk.Menu): Menü, das verschiedene Optionen zur Sortierung darstellt (Status, ID, Typ, Andere).
            """
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg='white', fg='black')
            dropdown_menu.add_command(label="→ Status", command=lambda: print("nach Status sortieren"))
            dropdown_menu.add_command(label="→ ID", command=lambda: print("nach ID sortieren"))
            dropdown_menu.add_command(label="→ Typ", command=lambda: print("nach Typ sortieren"))
            dropdown_menu.add_command(label="→ Andere", command=lambda: print("nach anderen sortieren"))
            dropdown_menu.post(Filter_button.winfo_rootx(), Filter_button.winfo_rooty() + Filter_button.winfo_height())

        Filter_button = tk.Button(self.ubersicht_frame, image=self.imgFilter, bd=0, bg='white', fg='black',
                                  font=("Inter", 20, 'bold'),
                                  command=show_dropdown_Filter)


        # Suche
        suche_button = ctk.CTkButton(self.ubersicht_frame, image=self.imgSuche, corner_radius=8, border_width=0, fg_color="transparent", hover_color='#D9D9D9',
                                 command=lambda: print(f"nach {suche_entry} gesucht"))
        suche_entry = ctk.CTkEntry(self.ubersicht_frame, corner_radius=8, fg_color="#D9D9D9",  text_color="black", border_width=0, font=("Inter", 12))

        # Hinzufügen
        Hinzufugen_button = tk.Button(self.ubersicht_frame, image=self.imgHinzufugen, bd=0, bg='white',
                                      command=lambda: controller.show_frame(Gerateansicht))

        # Aktionen
        Aktionen_button = tk.Button(self.ubersicht_frame, image=self.imgAktionen, bd=0, bg='white',
                                    command=lambda: print("Aktionen werden ausgeführt"))


#### Tabelle ####
        # Styling
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Inter", 12), background="#D9D9D9", foreground="#6E6893")
        style.configure("Treeview", font=("Arial", 11), rowheight=35, background="white", foreground="black")
        style.map("Treeview", background=[("selected", "#D9D9D9")], foreground=[("selected", "black")])
        style.configure("evenrow.Treeview", background="#f2f2f2")
        style.configure("oddrow.Treeview", background="white")

        #Definitoin Layout
        tree = ttk.Treeview(self.tabelle_frame, columns=("c1", "c2", "c3", "c4", "c5"), show="headings",
                            height=5)

        #Scrollbar
        scroll = ctk.CTkScrollbar(
            self.tabelle_frame,
            button_color=ThemeManager.SRH_Grey,
            orientation="vertical",
            command=tree.yview,
            height=650
        )

        # Treeview Scrollverbindung
        tree.configure(yscrollcommand=scroll.set)

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

        # Gerät aus Tabelle öffnen
        def on_item_select(event):
            try:
                selected_Item = tree.focus()
                print(f"Ausgewähltes Item: {selected_Item}")
                if selected_Item:
                    showDetails(selected_Item, tree, controller)
            except Exception as e:
                print(f"Fehler bei der Auswahl {e}")


        tree.bind("<Double-1>", on_item_select)

        #Farben für Tags definieren
        tree.tag_configure("even", background="#f7f7f7")
        tree.tag_configure("odd", background="white")

###### Plazierung #######
        Filter_button.place(relx=0, rely=0.1)
        suche_button.place(relx=0.1, rely=0.1, relheight=0.04, relwidth=0.022)
        suche_entry.place(relx=0.125, rely=0.1, relwidth=0.33, relheight=0.04)
        Hinzufugen_button.place(relx=0.5, rely=0.1)
        Aktionen_button.place(relx=0.6, rely=0.1)
        tree.place(x=120, y=0, width=1280, height=650)
        scroll.place(x=1400, y=0)
        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)
        verzeichniss.place(relx=0, rely=0.15, relwidth=0.15, relheight=0.85)
        self.tabelle_frame.place(relx=0.15, rely=0.3, relwidth=0.85, height=800)



def showDetails(selected_Item, tree, controller):
    """
    Displays the details of the selected item by retrieving its data from the
    given tree and updating the associated frame within a provided controller.

    :param selected_Item: Item identifier to select in the tree. Used to
                          access the item's data.
    :param tree: A Treeview instance from which item's data values are
                 retrieved.
    :param controller: An instance of a controller that manages application
                       frames. It's used for accessing and updating the
                       specific frame with the item's details.
    :return: None
    """
    data = tree.item(selected_Item, "values")
    print(f"Daten des ausgewählten Items: {data}")

    details = controller.frames[Gerateansicht]
    details.update_data(data)
    controller.show_frame(Gerateansicht)

#########################
#     Gerateansicht     #
#########################

class Gerateansicht(tk.Frame):
    """
    Initialisiert einen Frame zur Anzeige von detaillierten Geräteinformationen innerhalb der Anwendung.
    Diese Klasse konfiguriert das Layout und die Funktionen zur detaillierten Darstellung und Interaktion mit einem ausgewählten Gerät.

    **Args:**

    - *parent* (tk.Widget): Das übergeordnete Widget, in das dieser Frame eingebettet wird.
    - *controller* (object): Eine Instanz, die für den Wechsel zwischen Anwendungsansichten verantwortlich ist.

    Attributes:

    - *parent* (tk.Widget): Das übergeordnete Widget, das von der Klasse referenziert wird.
    - *controller* (object): Ein Objekt zur Steuerung der Anwendungsansichtsnavigation.

    **Verwendet:**

    - *self.gerateansicht_frame* - Frame für die Tabelle
    - *name_frame, ...* - Frames für Labels und Entrys der Gerateansicht
    - *button_frame* - Frame auf dem die Buttons positioniert werden
    """
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
        login = ctk.CTkButton(header, image=self.imglogin, fg_color=ThemeManager.SRH_Orange,
                              bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                              hover=True, hover_color='#e25a1f', text="",
                              command=lambda: controller.show_frame(gui_prototyp.LogInWindow))

        profil = ctk.CTkButton(header, image=self.imgprofil, fg_color=ThemeManager.SRH_Orange,
                               bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                               hover=True, hover_color='#e25a1f', text="",
                               command=lambda: controller.show_frame(Profiles.Profil))

        # Mainpage-Button innerhalb von gerateansicht_frame, an der gleichen Position wie das profilbild in Profil
        mainpage = ctk.CTkButton(self, text="↩", fg_color='white', text_color=ThemeManager.SRH_Grey, width=5,
                                     font=("Inter", 50, 'bold'), corner_radius=8, hover=False, command=lambda: controller.show_frame(Ubersicht))
        # Seiteninhalt
        tree = ttk.Treeview(self.gerateansicht_frame, columns=("c1", "c2", "c3"), show="headings",
                            height=5)
        scroll = ttk.Scrollbar(self.gerateansicht_frame, orient='vertical', command=tree.yview)
        #scroll.place(x=700, y=0.9, height=tree.winfo_height())
        tree.configure(yscrollcommand=scroll.set)

        # Definition der Tabelle
        tree.column("#1", anchor=CENTER, width=50)
        tree.heading("#1", text="Benutzer")
        tree.column("#2", anchor=CENTER, width=100)
        tree.heading("#2", text="Datum")
        tree.column("#3", anchor=CENTER, width=200)
        tree.heading("#3", text="Änderung")
        tree.place(x=0, y=20, relwidth=0.40, relheight=0.5)
        scroll.place(x=770, y=20, relheight=0.5)

        # Eintragsfelder -> Schema: frame, label, entry
        name_frame = ctk.CTkFrame(self.gerateansicht_frame, width=480, height=88, bg_color='transparent', fg_color='transparent', border_width=1, border_color='#B8B7B7', corner_radius=8)
        name_label = ctk.CTkLabel(name_frame, text="Gerätename", text_color='#858383', font=("Inter", 25, 'bold'))
        self.name_entry = ctk.CTkEntry(name_frame, text_color='black', font=("Inter", 20), border_width=0, fg_color='transparent')
        name_label.place(x=5, y=5)
        self.name_entry.place(x=5, y=50)
        name_frame.place(x=900, y=20)


        tag_frame = ctk.CTkFrame(self.gerateansicht_frame, width=480, height=88, bg_color='transparent',
                                  fg_color='transparent', border_width=1, border_color='#B8B7B7', corner_radius=8)
        tag_label = ctk.CTkLabel(tag_frame, text="Servicetag/Seriennummer", text_color='#858383', font=("Inter", 25, 'bold'))
        self.tag_entry = ctk.CTkEntry(tag_frame, text_color='black', font=("Inter", 20), border_width=0,
                                       fg_color='transparent')
        tag_label.place(x=5, y=5)
        self.tag_entry.place(x=5, y=50)
        tag_frame.place(x=900, y=120)

        typ_frame = ctk.CTkFrame(self.gerateansicht_frame, width=480, height=88, bg_color='transparent',
                                 fg_color='transparent', border_width=1, border_color='#B8B7B7', corner_radius=8)
        typ_label = ctk.CTkLabel(typ_frame, text="Gerätetyp", text_color='#858383',
                                 font=("Inter", 25, 'bold'))
        self.typ_aktuell_label = ctk.CTkLabel(typ_frame, text="", text_color='black',
                                 font=("Inter", 20))
        typ_label.place(x=5, y=5)
        self.typ_aktuell_label.place(x=5, y=50)
        typ_frame.place(x=900, y=220)

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
            """
            Dropdown für den Gerätetyp

            **Methods:**

            - *tk.Menu* erstellt ein Dropdown im Frame "Verzeichniss"
            - *add_command* fügt Auswahlmöglichkeiten hinzu
            - *command=lambda:*
            :return:
            """
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

        status_frame = ctk.CTkFrame(self.gerateansicht_frame, width=480, height=88, bg_color='transparent',
                                 fg_color='transparent', border_width=1, border_color='#B8B7B7', corner_radius=8)
        status_label = ctk.CTkLabel(status_frame, text="Status", text_color='#858383',
                                 font=("Inter", 25, 'bold'))
        self.status_aktuell_label = ctk.CTkLabel(status_frame, text="", text_color='black',
                                              font=("Inter", 20))
        status_label.place(x=5, y=5)
        self.status_aktuell_label.place(x=5, y=50)
        status_frame.place(x=900, y=320)

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
            """
            Dropdown für den Gerätestatus

            **Methods:**

            - *tk.Menu* erstellt ein Dropdown im Frame "Verzeichniss"
            - *add_command* fügt Auswahlmöglichkeiten hinzu
            - *command=lambda:*
            :return:
            """

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

        standort_frame = ctk.CTkFrame(self.gerateansicht_frame, width=480, height=88, bg_color='transparent',
                                 fg_color='transparent', border_width=1, border_color='#B8B7B7', corner_radius=8)
        standort_label = ctk.CTkLabel(standort_frame, text="Standort (Haus, Raum)", text_color='#858383',
                                 font=("Inter", 25, 'bold'))
        self.standort_entry = ctk.CTkEntry(standort_frame, text_color='black', font=("Inter", 20), border_width=0,
                                      fg_color='transparent')
        standort_label.place(x=5, y=5)
        self.standort_entry.place(x=5, y=50)
        standort_frame.place(x=900, y=420)

        #Button Frame
        buttons_frame = tk.Frame(self.gerateansicht_frame, bg='white', bd=0, relief="solid")

        #Img definitionen für Buttons
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
            """
            Erstellt ein neues Fenster zur Erfassung von Geräteschäden mit Eingabefeldern und Aktionsschaltflächen.

            Diese Funktion initialisiert ein Unterfenster, in dem Benutzer Details zu einem Geräteschaden eingeben und speichern können.


            Attributes:
            aktualisieren_img (PhotoImage): Bild für die Schaltfläche zum Schließen des Fensters.
            upload_img (PhotoImage): Bild für die Schaltfläche zum Hochladen eines Bildes.
            info_frame (tk.Frame): Frame, der Eingabefelder für den Gerätename, Tag, Datum und eine Beschreibung enthält.
            verlauf_frame (tk.Frame): Frame, der ein Eingabefeld für den Verlauf anzeigt.
            schaeden_button_frame (tk.Frame): Frame, der Aktionsschaltflächen enthält.

            **Verwendet:**

            - *name_entry* (ctk.CTkEntry), *tag_entry* (ctk.CTkEntry), *current_date* (tk.Label), *beschreibung_entry* (ctk.CTkEntry):
            - Eingaben und Labels zur Erfassung und Anzeige von Gerätename, Tag, aktuellem Datum und Beschreibung.
            - verlauf_inh_entry (ctk.CTkEntry): Eingabefeld für den Verlauf.

            """

            schaeden_page = tk.Toplevel()#root
            schaeden_page.title("Schäden eintragen")
            schaeden_page.geometry("819x594+500+300")
            schaeden_page.configure(bg='white')

            schaeden_page.grab_set()

            #Bilder
            self.aktualisieren_img = gui_prototyp.load_image(root_path+"/gui/assets/Button_Aktualisieren.png")
            self.upload_img1 = gui_prototyp.load_image(root_path+"/gui/assets/Button_Drop.png")

            #Informationen
            info_frame = tk.Frame(schaeden_page, bg='white', bd=1)
            verlauf_frame = tk.Frame(schaeden_page, bg='white', bd=1)

            name_label = tk.Label(info_frame, text="Gerätename", bg='white',
                                      font=("Inter", 19))
            name_entry_frame = ctk.CTkFrame(info_frame, width=150, height=40, bg_color='transparent',
                                      fg_color='transparent', border_width=1, border_color='#B8B7B7', corner_radius=8)
            name_entry = ctk.CTkEntry(name_entry_frame, text_color='black', font=("Inter", 15), border_width=0,
                                       fg_color='transparent', width=100)

            tag_label = tk.Label(info_frame, text="Tag", bg='white',
                                  font=("Inter", 19))
            tag_entry_frame = ctk.CTkFrame(info_frame, width=150, height=40, bg_color='transparent',
                                            fg_color='transparent', border_width=1, border_color='#B8B7B7',
                                            corner_radius=8)
            tag_entry = ctk.CTkEntry(tag_entry_frame, text_color='black', font=("Inter", 15), border_width=0,
                                      fg_color='transparent', width=100)

            date_label = tk.Label(info_frame, text="Datum", bg='white',
                                 font=("Inter", 19))
            date_entry_frame = ctk.CTkFrame(info_frame, width=150, height=40, bg_color='transparent',
                                            fg_color='transparent', border_width=1, border_color='#B8B7B7',
                                            corner_radius=8)
            date_entry = datetime.now().strftime("%d.%m.%Y")
            current_date = tk.Label(date_entry_frame, text=date_entry, font=("Inter", 13), bg='white', fg='black', bd=0)


            beschreibung_label = tk.Label(info_frame, text="Beschreibung", bg='white',
                                 font=("Inter", 19))
            beschreibung_entry_frame = ctk.CTkFrame(info_frame, width=380, height=382, bg_color='transparent',fg_color='transparent', border_width=1, border_color='#B8B7B7', corner_radius=8)
            beschreibung_entry = ctk.CTkEntry(beschreibung_entry_frame, fg_color='transparent', text_color='black', font=("Inter", 13), width=380, height=382, border_width=1, border_color='#B8B7B7', corner_radius=8)

            #Verlauf
            verlauf_label = tk.Label(verlauf_frame, text="Verlauf", bg='white',
                                 font=("Inter", 19))
            verlauf_inh_entry =  ctk.CTkEntry(verlauf_frame, fg_color='transparent', text_color='black', font=("Inter", 13), width=380, height=382, border_width=1, border_color='#B8B7B7', corner_radius=8)

            schaeden_button_frame = tk.Frame(schaeden_page, bg='white', bd=1)
            close_button = tk.Button(schaeden_button_frame, image=self.aktualisieren_img, bd=0, bg='white', command=schaeden_page.destroy)
            upload_button = tk.Button(schaeden_button_frame, image=self.upload_img1, bd=0, bg='white', command=lambda: print("Bild hochgeladen"))

            ###### Plazierung #######
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

#######################################################################################################

        schaeden_button = tk.Button(buttons_frame, image=self.schaeden_img, bd=0, bg='white', command=open_schaeden_page)
        schaeden_button.place(x=10, y=10)

        def open_buchen_page():

            """
            Erstellt ein neues Fenster zur Buchung eines Geräts mit Eingabefeldern, Datumsauswahl und Aktionsschaltflächen.

            Diese Funktion initialisiert ein Unterfenster, in dem Benutzer ein Gerät buchen und entsprechende Details sowie Start- und Enddaten eingeben können.

            **Attributes:**

            - aktualisieren_img (PhotoImage): Bild für die Schaltfläche zum Schließen des Fensters.
            - info_frame (tk.Frame): Frame, der Eingabefelder für den Gerätename, Servicetag und Verlauf enthält.
            - date_frame (tk.Frame): Frame für die Datumsauswahl und Anzeige.
            - buchen_button_frame (tk.Frame): Frame, der die Aktionsschaltfläche zum Schließen des Fensters enthält.

            **Verwendet:**

            - name_entry (ctk.CTkEntry), tag_entry (ctk.CTkEntry), verlauf_entry (ctk.CTkEntry): Eingaben zur Erfassung von Gerätename, Servicetag und Verlauf.
            - ask_date_button (ctk.CTkButton): Schaltflächen zur Auswahl von Start- und Enddatum.
            - start_result_label, end_result_label (tk.Label): Labels zur Anzeige der ausgewählten Start- und Enddaten.


            """

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
            name_entry = ctk.CTkEntry(info_frame, fg_color='transparent', text_color='black', font=("Inter", 15), width=150, border_width=1, border_color='#B8B7B7', corner_radius=8)

            tag_label = tk.Label(info_frame, text="Servicetag", bg='white',
                                 font=("Inter", 19))
            tag_entry = ctk.CTkEntry(info_frame, fg_color='transparent', text_color='black', font=("Inter", 15), width=150, border_width=1, border_color='#B8B7B7', corner_radius=8)

            verlauf_label = tk.Label(info_frame, text="Verlauf", bg='white',
                                          font=("Inter", 19))
            verlauf_entry = ctk.CTkEntry(info_frame, fg_color='transparent', text_color='black', font=("Inter", 15), width=380, height=382, border_width=1, border_color='#B8B7B7', corner_radius=8)

            #Datum
            def ask_startdate():
                """
                Die Funktion gibt eine Eingabemöglichkeit für ein Startdatum an.
                Form: 12.12.2012

                Ist das Datum ungültig oder nicht angegeben, wird ein Fehlermeldung angezeigt.
                """
                # Benutzer nach Datum fragen
                entered_date = simpledialog.askstring("Datum", "Startdatum (Format: DD.MM.YYYY:)")
                try:
                    # Datum validieren
                    datetime.strptime(entered_date, "%d.%m.%Y")
                    start_result_label.config(text=f"von: {entered_date}")
                except (ValueError, TypeError):
                    start_result_label.config(text="Ungültiges Datum!")

            # Button zur Datumseingabe
            ask_date_button = ctk.CTkButton(date_frame,text="Startdatum",command=ask_startdate, corner_radius=8, fg_color="#6F6C6C", text_color="white", hover_color="#081424")
            ask_date_button.place(x=0, y=0)

            start_result_label = tk.Label(date_frame, text="Kein Datum ausgewählt", font=("Arial", 14), bg='white')
            start_result_label.place(x=150, y=0)

            def ask_enddate():
                """
                Die Funktion gibt eine Eingabemöglichkeit für ein Enddatum an.
                Form: 12.12.2012

                Ist das Datum ungültig oder nicht angegeben, wird ein Fehlermeldung angezeigt.
                """
                date_frame.focus_set()

                # Benutzer nach Datum fragen
                entered_date = simpledialog.askstring("Datum", "Enddatum (Format: DD.MM.YYYY:)")
                try:
                    # Datum validieren
                    datetime.strptime(entered_date, "%d.%m.%Y")

                    end_result_label.config(text=f"bis: {entered_date}")
                except ValueError:
                    end_result_label.config(text="Ungültiges Datum!")
                # Button zur Datumseingabe

            ask_date_button = ctk.CTkButton(date_frame,text="Enddatum",command=ask_enddate, corner_radius=8, fg_color="#081424", text_color="white", hover_color="#6F6C6C")
            ask_date_button.place(x=0, y=100)
            # Ergebnis-Label
            end_result_label = tk.Label(date_frame, text="Kein Datum ausgewählt", font=("Arial", 14), bg='white')
            end_result_label.place(x=150, y=100)

            # Buttons
            buchen_button_frame = tk.Frame(buchen_page, bg='white', bd=1)
            close_button = tk.Button(buchen_button_frame, image=self.aktualisieren_img, bd=0, bg='white',
                                     command=buchen_page.destroy)


            ###### Plazierung #######
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

#######################################################################################################

        # Button Buchung
        buchung_button = tk.Button(buttons_frame, image=self.buchung_img, bd=0, bg='white',
                                       command=open_buchen_page)
        buchung_button.place(x=10, y=80)

        #Button Speichern
        def button_click():
            """
            Beim Klicken des Buttons *speicher_button* wird man zurück auf Gerateubersicht geleitet und
            eine Messagebox kommt

            :return:
            """
            controller.show_frame(Ubersicht)
            messagebox.showinfo("Erfolgreich","Änderungen erfolgreich gespeichert")

        speichern_button = tk.Button(buttons_frame, image=self.speichern_img, bd=0, bg='white', command=button_click)
        speichern_button.place(x=10, y=150)


        #Verzeichniss
        # "Alle Anzeigen" Button in der Seitenleiste
        all_button = tk.Button(verzeichniss, text="Alle anzeigen", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                               font=("Inter", 20, 'bold'),
                               command=lambda: controller.show_frame(Ubersicht))

        all_button.pack(pady=10, anchor='w')

        # Funktionen für das Verzeichniss, siehe Zeile 114
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

        ###### Plazierung #######
        upload_button.place(x=100, y=0)
        upload_frame.place(x=0, y=520, relwidth=0.40, height=300)
        buttons_frame.place(x=900, y=520, width=480, height=300)

        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)
        verzeichniss.place(relx=0, rely=0.15, relwidth=0.15, relheight=0.85)
        login.place(relx=0.95, rely=0.5, anchor="center")
        profil.place(relx=0.90, rely=0.5, anchor="center")
        mainpage.place(relx=0.16, rely=0.16, anchor='nw')

    #Funktion, die die Daten aus der Tabelle in die Labels und Entrys des Info Frames einträgt
    def update_data(self, data):
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, data[5])

        self.tag_entry.delete(0, tk.END)
        self.tag_entry.insert(0, data[0])

        self.standort_entry.delete(0, tk.END)
        self.standort_entry.insert(0, data[3])

        self.typ_aktuell_label.configure(text=data[1])

        self.status_aktuell_label.configure(text=data[4])

