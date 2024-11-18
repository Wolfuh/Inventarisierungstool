import tkinter as tk
from tkinter import ttk

import gui_prototyp
import Mainpages
import Overview_pages
import ThemeManager
import Profiles


class Einstellungen(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__()
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
            file="gui/assets/Closeicon.png")
        self.imgmainpage = tk.PhotoImage(
            file="gui/assets/backtosite_icon.png")

        login = tk.Button(self.header, image=self.imglogin, bd=0, bg=ThemeManager.SRH_Orange,
                          command=lambda: controller.show_frame(gui_prototyp.LogInWindow))
        mainpage = tk.Button(self.header, image=self.imgmainpage, bd=0, bg=ThemeManager.SRH_Orange,
                             command=lambda: controller.show_frame(Mainpages.MainPage))
        # login_label = tk.Button(self.header, text="🚪",bd=0, fg='#858383', font=("Inter", 19)
        # , command=lambda: controller.show_frame(LogInWindow))
        # login_label.place(relx=0.70, rely=0.5, anchor="center")
        # Platzierung der Header-Navigationsbuttons, Linksseitige
        # Navigationsbuttons für andere Ansichten (Profil, Admin, Stats, EinstellungenO
        login.place(relx=0.95, rely=0.5, anchor="center")
        mainpage.place(relx=0.90, rely=0.5, anchor="center")

        user_button = tk.Button(verzeichniss, text="User", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=lambda: controller.show_frame(Profiles.Profil))
        user_button.pack(pady=10, anchor='w')

        admin_button = tk.Button(verzeichniss, text="Administration", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                 font=("Inter", 20, 'bold'),
                                 command=lambda: controller.show_frame(Profiles.Admin))
        admin_button.pack(pady=10, anchor='w')

        stats_button = tk.Button(verzeichniss, text="Statistiken", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                 font=("Inter", 20, 'bold'),
                                 command=lambda: controller.show_frame(Profiles.Stats))
        stats_button.pack(pady=10, anchor='w')

        einstellungen_button = tk.Button(verzeichniss, text="Einstellungen", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                         font=("Inter", 20, 'bold'),
                                         command=lambda: controller.show_frame(Einstellungen))
        einstellungen_button.pack(pady=10, anchor='w')

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
            self.light = tk.PhotoImage(file="gui/assets/switchoff.png")
            self.dark = tk.PhotoImage(file="gui/assets/switchon.png")
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

        addSpalten_button = tk.Button(self.einstellung_frame, text="Spalte\t+", bd=0, bg='white', fg='black',
                                      font=("Inter", 16),
                                      command=lambda: print("Spalte hinzugefügt"))
        addSpalten_button.place(relx=0.01, rely=0.64, relheight=0.032)

        addStatus_button = tk.Button(self.einstellung_frame, text="Status\t+", bd=0, bg='white', fg='black',
                                     font=("Inter", 16),
                                     command=lambda: print("Status hinzugefügt"))
        addStatus_button.place(relx=0.01, rely=0.69, relheight=0.032)

        addTyp_button = tk.Button(self.einstellung_frame, text="Typ\t+", bd=0, bg='white', fg='black',
                                  font=("Inter", 16),
                                  command=lambda: print("Typ hinzugefügt"))
        addTyp_button.place(relx=0.01, rely=0.74, relheight=0.032)

        addGerat_button = tk.Button(self.einstellung_frame, text="Gerät\t+", bd=0, bg='white', fg='black',
                                    font=("Inter", 16),
                                    command=lambda: controller.show_frame(Overview_pages.Gerateansicht))
        addGerat_button.place(relx=0.01, rely=0.79, relheight=0.032)

        # Platzierung der Hauptframe-Bereiche
        self.einstellung_frame.place(relx=0.15, rely=0.15, relwidth=1, relheight=0.85)
        self.header.place(relx=0, rely=0, relwidth=1, relheight=0.15)
