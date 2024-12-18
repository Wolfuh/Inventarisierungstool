import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import os

from gui import Mainpages


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
        from ThemeManager import ThemeManager

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

        def logout():
            from gui_prototyp import LogInWindow
            controller.show_frame(LogInWindow)

        login = ctk.CTkButton(self.header, image=self.imglogin, fg_color=ThemeManager.SRH_Orange,
                              bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                              hover=True, hover_color='#e25a1f', text="",
                              command=logout)

        def show_mainpage():
            from Mainpages import MainPage
            controller.show_frame(MainPage)

        mainpage = ctk.CTkButton(self.header, image=self.imgmainpage, fg_color=ThemeManager.SRH_Orange,
                                 bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                                 hover=True, hover_color='#e25a1f', text="",
                                 command=show_mainpage())

        def show_help():
            from Profiles import Help
            controller.show_frame(Help)

        help = ctk.CTkButton(self.header, image=self.imghelp, fg_color=ThemeManager.SRH_Orange,
                             bg_color=ThemeManager.SRH_Orange, corner_radius=40, height=10, width=10,
                             hover=True, hover_color='#e25a1f', text="",
                             command=show_help)

        login.place(relx=0.95, rely=0.5, anchor="center")
        mainpage.place(relx=0.90, rely=0.5, anchor="center")
        help.place(relx=0.85, rely=0.5, anchor="center")

        def show_profile():
            from Profiles import Profil
            controller.show_frame(Profil)

        user_button = tk.Button(verzeichniss, text="User", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=show_profile)
        user_button.pack(pady=10, anchor='w')

        def show_admin():
            from Profiles import Admin
            controller.show_frame(Admin)

        admin_button = tk.Button(verzeichniss, text="Administration", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                 font=("Inter", 20, 'bold'),
                                 command=show_admin)
        admin_button.pack(pady=10, anchor='w')

        def show_stats():
            from Profiles import Stats
            controller.show_frame(Stats)

        stats_button = tk.Button(verzeichniss, text="Statistiken", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                 font=("Inter", 20, 'bold'),
                                 command=show_stats)
        stats_button.pack(pady=10, anchor='w')

        def show_config():
            controller.show_frame(Einstellungen)

        einstellungen_button = tk.Button(verzeichniss, text="Einstellungen", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                         font=("Inter", 20, 'bold'),
                                         command=show_config)
        einstellungen_button.pack(pady=10, anchor='w')

        verzeichniss_help_button = tk.Button(verzeichniss, text="Hilfe", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                             font=("Inter", 20, 'bold'),
                                             command=show_help)
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
            from gui_prototyp import load_image
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
            from gui_prototyp import load_image
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
            from gui_prototyp import load_image
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

        def show_device_view():
            from Overview_pages import Gerateansicht
            controller.show_frame(Gerateansicht)

        addGerat_button = tk.Button(self.einstellung_frame, text="Gerät\t+", bd=0, bg='white', fg='black',
                                    font=("Inter", 16),
                                    command=show_device_view)
        addGerat_button.place(relx=0.01, rely=0.79, relheight=0.032)

        # Platzierung der Hauptframe-Bereiche
        self.einstellung_frame.place(relx=0.15, rely=0.15, relwidth=1, relheight=0.85)
        self.header.place(relx=0, rely=0, relwidth=1, relheight=0.15)
