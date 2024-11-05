import tkinter as tk
from tkinter import ttk, messagebox
import os
from tkinter import *

# Farben der SRH (Corporate Design)
SRH_Orange = "#df4807"
SRH_Grey = "#d9d9d9"
SRH_Blau = "#10749c"

# Darkmode_Farben
Darkmode_Black = "#121212"
Darkmode_Grey = "#2d2d2d"

class GuiTest(tk.Tk):

    def __init__(self, *args, **kwargs):
        """Intialisiert das Hauptfenster und erstellt alle Seiten-Frames"""
        super().__init__(*args, **kwargs)

        self.title("Prototyp")
        self.resizable(False, False)
        self.geometry("1920x1080")

        # Hauptcontainer für alle Frames
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # Erstellung und Speicherung der Instanzen aller Seiten
        for F in (LogInWindow, MainPage, MainPageS2, Ubersicht, Gerateansicht, Profil, Admin, Stats, Einstellungen):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

def load_image(image_path):
    """Lädt ein Bild aus dem Pfad, gibt ein PhotoImage-Objekt zurück oder None bei fehlendem Bild."""
    if os.path.exists(image_path):
        return tk.PhotoImage(file=image_path)
    else:
        print(f"Warnung: Bild '{image_path}' nicht gefunden.")
        return None

class LogInWindow(tk.Frame):
    """Errstellung des Login-Fensters mit Benutername- und Passwort-Eingabefeldern.
        Zeigt die Hauptseite bei erfolgreichem Login an und gibt eine Fehlermeldung bei falschem"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')

        # Konfiguration des Kopf- und Fußbereich
        header = ttk.Label(self, text="Login", anchor="center", style="Header.TLabel")
        bottom = ttk.Label(self, style="Footer.TLabel")

        style = ttk.Style()
        style.configure("Header.TLabel", foreground='white', background=SRH_Orange, font=("Inter", 50, 'bold'))
        style.configure("Footer.TLabel", background=SRH_Grey)

        def login():
            # Überprüfung der Anmeldedaten und zeigt die Hauptseite bei Erfolg an
            username = "1"
            password = "1"
            if username_entry.get() == username and password_entry.get() == password:
                controller.show_frame(MainPage)
                username_entry.delete(0, 'end')
                password_entry.delete(0, 'end')
            else:
                messagebox.showinfo(title="Fehler", message="Passwort oder Benutzername falsch")
                password_entry.delete(0, 'end')

        # Erstellung der Login-Elemente
        login_frame = tk.Frame(self, bg='white')
        username_label = tk.Label(login_frame, text="Benutzername", bg='white', font=("Inter", 19))
        username_entry = tk.Entry(login_frame, bg='white', font=("Inter", 15))
        password_label = tk.Label(login_frame, text="Passwort", bg='white', font=("Inter", 19))
        password_entry = tk.Entry(login_frame, show="*", bg='white', font=("Inter", 15))
        login_button = tk.Button(login_frame, text="Login", bg='#081424', fg='white', font=("Inter", 20, 'bold'),
                                 command=login)
        # Layout der Login-Elemente
        username_label.grid(row=0, column=0, pady=10)
        username_entry.grid(row=1, column=0, pady=10)
        password_label.grid(row=2, column=0, pady=10)
        password_entry.grid(row=3, column=0, pady=10)
        login_button.grid(row=4, column=0, pady=20)

        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)
        bottom.place(relx=0, rely=0.85, relwidth=1, relheight=0.13)
        login_frame.place(relx=0.5, rely=0.5, anchor="center")

class MainPage(tk.Frame):
    """Erstellt die Startseite mit Navigations- und Funktionsbuttons sowie Bildgurppen
       Ermöglicht den Zugriff auf Login, Profil und Übersichtsseiten"""
    def __init__(self, parent, controller):
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
        self.imglogin = load_image("assets/X.png")
        self.imgprofil = load_image("assets/Y.png")
        self.imgbildgr1 = tk.PhotoImage(file="assets/Gruppe1.png")
        self.imgbildgr2 = tk.PhotoImage(file="assets/Gruppe2.png")
        self.imgbildgr3 = tk.PhotoImage(file="assets/Gruppe3.png")
        self.imgbildgr4 = tk.PhotoImage(file="assets/Gruppe4.png")
        self.imgbildgr5 = tk.PhotoImage(file="assets/Gruppe5.png")
        self.imgbildgr6 = tk.PhotoImage(file="assets/Gruppe6.png")
        self.imgbildgr7 = tk.PhotoImage(file="assets/Gruppe7.png")
        self.imgbildgr8 = tk.PhotoImage(file="assets/Gruppe8.png")
        self.imgseitevor = tk.PhotoImage(file="assets/Seitevor.png")

        # Platzierung der Buttons
        login = tk.Button(header, image=self.imglogin, bd=0, bg=SRH_Orange,
                            command=lambda: controller.show_frame(LogInWindow))
        profil = tk.Button(header, image=self.imgprofil, bd=0, bg=SRH_Orange,
                            command=lambda: controller.show_frame(Profil))
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
        bildgr8 = tk.Button(self, image=self.imgbildgr8, bd=0, bg='white',
                               command=lambda: controller.show_frame(Ubersicht))
        all = tk.Button(self, text="Alle anzeigen", bd=0, bg='white', fg='#1D4478', font=("Inter", 20),
                           command=lambda: controller.show_frame(Ubersicht))
        seitevor = tk.Button(self, image=self.imgseitevor, bd=0, bg='white', fg='#1E1E1E', font=("Inter", 16),
                        command=lambda: controller.show_frame(MainPageS2))

        # Festlegung des Styles für Header- und Footer Labels, Positionierung der Navigationsbuttons im Header, die
        # Anordnung der Bildgruppen-Buttons in einem Rasterlayout, sowie Platzierungen.
        style = ttk.Style()
        style.configure("Header.TLabel", foreground='white', background='#DF4807', font=("Inter", 55, 'bold'))
        style.configure("Footer.TLabel", background=SRH_Grey)

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
        self.imglogin = load_image("assets/X.png")
        self.imgprofil = load_image("assets/Y.png")
        self.imgbildgr1 = tk.PhotoImage(file="assets/Gruppe1.png")
        self.imgbildgr2 = tk.PhotoImage(file="assets/Gruppe2.png")
        self.imgbildgr3 = tk.PhotoImage(file="assets/Gruppe3.png")
        self.imgbildgr4 = tk.PhotoImage(file="assets/Gruppe4.png")
        self.imgbildgr5 = tk.PhotoImage(file="assets/Gruppe5.png")
        self.imgbildgr6 = tk.PhotoImage(file="assets/Gruppe6.png")
        self.imgbildgr7 = tk.PhotoImage(file="assets/Gruppe7.png")
        #self.imgbildgr8 = tk.PhotoImage(file="assets/Gruppe8.png")
        self.imgseitevor = tk.PhotoImage(file="assets/Seitevor.png")
        self.imgseiteback = tk.PhotoImage(file="assets/Seiteback.png")
        login = tk.Button(header, image=self.imglogin, bd=0, bg=SRH_Orange,
                            command=lambda: controller.show_frame(LogInWindow))
        profil = tk.Button(header, image=self.imgprofil, bd=0, bg=SRH_Orange,
                            command=lambda: controller.show_frame(Profil))
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
        #bildgr8 = tk.Button(self, image=self.imgbildgr8, bd=0, bg='white',
                              # command=lambda: controller.show_frame(Ubersicht))

        # Buttons zum Wechseln zwischen den Hauptseiten und "Alle anzeigen" Button für die Übersichtsseite
        all = tk.Button(self, text="Alle anzeigen", bd=0, bg='white', fg=SRH_Blau, font=("Inter", 20),
                           command=lambda: controller.show_frame(Ubersicht))
        seitevor = tk.Button(self, image=self.imgseitevor, bd=0, bg='white', fg='#1E1E1E', font=("Inter", 16),
                        command=lambda: controller.show_frame(MainPageS2))
        seiteback = tk.Button(self, image=self.imgseiteback, bd=0, bg='white', fg='#1E1E1E', font=("Inter", 16),
                        command=lambda: controller.show_frame(MainPage))

        # Style Konfiguration für Header und Footer, Platzierung der Buttons, Header und Footer
        style = ttk.Style()
        style.configure("Header.TLabel", foreground='white', background=SRH_Orange, font=("Inter", 55, 'bold'))
        style.configure("Footer.TLabel", background=SRH_Grey)

        login.place(relx=0.95, rely=0.5, anchor="center")
        profil.place(relx=0.90, rely=0.5, anchor="center")

        bildgr1.place(relx=0.20, rely=0.25, anchor='n')
        bildgr2.place(relx=0.40, rely=0.25, anchor='n')
        bildgr3.place(relx=0.60, rely=0.25, anchor='n')
        bildgr4.place(relx=0.80, rely=0.25, anchor='n')

        bildgr5.place(relx=0.20, rely=0.55, anchor='n')
        bildgr6.place(relx=0.40, rely=0.55, anchor='n')
        bildgr7.place(relx=0.60, rely=0.55, anchor='n')
        #bildgr8.place(relx=0.80, rely=0.55, anchor='n')

        all.place(relx=0.01, rely=0.18, anchor='w')
        seitevor.place(relx=0.51, rely=0.80, anchor='n')
        seiteback.place(relx=0.49, rely=0.80, anchor='n')
        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)
        bottom.place(relx=0, rely=0.85, relwidth=1, relheight=0.13)

class Ubersicht(tk.Frame):
    """Repraesentiert die Geraeteuebersichtsseite der Anwendung. Zeigt eine Liste oder Tabelle der verfügbaren
       Geräte und bietet Optionen für die Navigation zurück zur Hauptseite, zum Login und zu Benutzerprofilen """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')

        # Stilkonfiguration für Header und Footer, Erstellung vom Header und des Überschriftbereiches.
        style = ttk.Style()
        style.configure("Header.TLabel", foreground='white', background=SRH_Orange, font=("Inter", 55, 'bold'))
        style.configure("Footer.TLabel", background=SRH_Grey)
        header = ttk.Label(self, text="Geräteübersicht", anchor="center", style="Header.TLabel")
        verzeichniss = tk.Frame(self, bg=SRH_Grey)
        self.ubersicht_frame = tk.Frame(self, bg='white')
        self.tabelle_frame = tk.Frame(self, bg='white')
        self.ubersicht_frame.place(relx=0.21, rely=0.15, relwidth=1, relheight=0.85)

        # Layout Festlegung der flexiblen Skalierung der Übersichtsseite
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)

        # Laden der Bilder für die Navigation und Header Buttons
        self.imglogin = load_image("assets/X.png")
        self.imgprofil = load_image("assets/Y.png")

        # Login und Profil Buttons im Header-Bereich, Platzierung der Buttons, Header und Sidebar
        login = tk.Button(header, image=self.imglogin, bd=0, bg=SRH_Orange,
                            command=lambda: controller.show_frame(LogInWindow))
        profil = tk.Button(header, image=self.imgprofil, bd=0, bg=SRH_Orange,
                            command=lambda: controller.show_frame(Profil))
        self.imgmainpage = tk.PhotoImage(
            file="assets/Z.png")

        login.place(relx=0.95, rely=0.5, anchor="center")
        profil.place(relx=0.90, rely=0.5, anchor="center")

        mainpage = tk.Button(header, image=self.imgmainpage, bd=0, bg=SRH_Orange,
                            command=lambda: controller.show_frame(MainPage))

        # "Alle Anzeigen" Button in der Seitenleiste
        all_button = tk.Button(verzeichniss, text="Alle anzeigen", bd=0, bg=SRH_Grey, fg='black', font=("Inter", 20, 'bold'),
                                command=lambda: controller.show_frame(Ubersicht))

        all_button.pack(pady=10, anchor='w')


#Gruppe 1
        def show_dropdown_grp1():
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg=SRH_Grey, fg='black')
            dropdown_menu.add_command(label="→ Hardware", command=lambda: controller.show_frame(Admin))
            dropdown_menu.add_command(label="→ Software", command=lambda: controller.show_frame(Stats))
            dropdown_menu.add_command(label="→ Peripherie", command=lambda: controller.show_frame(Profil))
            dropdown_menu.add_command(label="→ Andere", command=lambda: controller.show_frame(Einstellungen))
            dropdown_menu.post(grp1_button.winfo_rootx(), grp1_button.winfo_rooty() + grp1_button.winfo_height())

        grp1_button = tk.Button(verzeichniss, text="Gruppe 1   ", bd=0, bg=SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=show_dropdown_grp1)
        grp1_button.pack(pady=10, anchor='w')

#Gruppe 2
        def show_dropdown_grp2():
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg=SRH_Grey, fg='black')
            dropdown_menu.add_command(label="→ Hardware", command=lambda: controller.show_frame(Admin))
            dropdown_menu.add_command(label="→ Software", command=lambda: controller.show_frame(Stats))
            dropdown_menu.add_command(label="→ Peripherie", command=lambda: controller.show_frame(Profil))
            dropdown_menu.add_command(label="→ Andere", command=lambda: controller.show_frame(Einstellungen))
            dropdown_menu.post(grp2_button.winfo_rootx(), grp2_button.winfo_rooty() + grp2_button.winfo_height())

        grp2_button = tk.Button(verzeichniss, text="Gruppe 2   ", bd=0, bg=SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=show_dropdown_grp2)
        grp2_button.pack(pady=10, anchor='w')

# Gruppe 3
        def show_dropdown_grp3():
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg=SRH_Grey, fg='black')
            dropdown_menu.add_command(label="→ Hardware", command=lambda: controller.show_frame(Admin))
            dropdown_menu.add_command(label="→ Software", command=lambda: controller.show_frame(Stats))
            dropdown_menu.add_command(label="→ Peripherie", command=lambda: controller.show_frame(Profil))
            dropdown_menu.add_command(label="→ Andere", command=lambda: controller.show_frame(Einstellungen))
            dropdown_menu.post(grp3_button.winfo_rootx(), grp3_button.winfo_rooty() + grp3_button.winfo_height())

        grp3_button = tk.Button(verzeichniss, text="Gruppe 3   ", bd=0, bg=SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=show_dropdown_grp3)
        grp3_button.pack(pady=10, anchor='w')

#Gruppe 4
        def show_dropdown_grp4():
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg=SRH_Grey, fg='black')
            dropdown_menu.add_command(label="→ Hardware", command=lambda: controller.show_frame(Admin))
            dropdown_menu.add_command(label="→ Software", command=lambda: controller.show_frame(Stats))
            dropdown_menu.add_command(label="→ Peripherie", command=lambda: controller.show_frame(Profil))
            dropdown_menu.add_command(label="→ Andere", command=lambda: controller.show_frame(Einstellungen))
            dropdown_menu.post(grp4_button.winfo_rootx(), grp4_button.winfo_rooty() + grp4_button.winfo_height())

        grp4_button = tk.Button(verzeichniss, text="Gruppe 4   ", bd=0, bg=SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=show_dropdown_grp4)
        grp4_button.pack(pady=10, anchor='w')

# Gruppe 5
        def show_dropdown_grp5():
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg=SRH_Grey, fg='black')
            dropdown_menu.add_command(label="→ Hardware", command=lambda: controller.show_frame(Admin))
            dropdown_menu.add_command(label="→ Software", command=lambda: controller.show_frame(Stats))
            dropdown_menu.add_command(label="→ Peripherie", command=lambda: controller.show_frame(Profil))
            dropdown_menu.add_command(label="→ Andere", command=lambda: controller.show_frame(Einstellungen))
            dropdown_menu.post(grp5_button.winfo_rootx(), grp5_button.winfo_rooty() + grp5_button.winfo_height())

        grp5_button = tk.Button(verzeichniss, text="Gruppe 5   ", bd=0, bg=SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=show_dropdown_grp5)
        grp5_button.pack(pady=10, anchor='w')

# Gruppe 6
        def show_dropdown_grp6():
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg=SRH_Grey, fg='black')
            dropdown_menu.add_command(label="→ Hardware", command=lambda: controller.show_frame(Admin))
            dropdown_menu.add_command(label="→ Software", command=lambda: controller.show_frame(Stats))
            dropdown_menu.add_command(label="→ Peripherie", command=lambda: controller.show_frame(Profil))
            dropdown_menu.add_command(label="→ Andere", command=lambda: controller.show_frame(Einstellungen))
            dropdown_menu.post(grp6_button.winfo_rootx(), grp6_button.winfo_rooty() + grp6_button.winfo_height())

        grp6_button = tk.Button(verzeichniss, text="Gruppe 6   ", bd=0, bg=SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=show_dropdown_grp6)
        grp6_button.pack(pady=10, anchor='w')

# Gruppe 7
        def show_dropdown_grp7():
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg=SRH_Grey, fg='black')
            dropdown_menu.add_command(label="→ Hardware", command=lambda: controller.show_frame(Admin))
            dropdown_menu.add_command(label="→ Software", command=lambda: controller.show_frame(Stats))
            dropdown_menu.add_command(label="→ Peripherie", command=lambda: controller.show_frame(Profil))
            dropdown_menu.add_command(label="→ Andere", command=lambda: controller.show_frame(Einstellungen))
            dropdown_menu.post(grp7_button.winfo_rootx(), grp7_button.winfo_rooty() + grp7_button.winfo_height())

        grp7_button = tk.Button(verzeichniss, text="Gruppe 7   ", bd=0, bg=SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=show_dropdown_grp7)
        grp7_button.pack(pady=10, anchor='w')

# Gruppe 8
        def show_dropdown_grp8():
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg=SRH_Grey, fg='black')
            dropdown_menu.add_command(label="→ Hardware", command=lambda: controller.show_frame(Admin))
            dropdown_menu.add_command(label="→ Software", command=lambda: controller.show_frame(Stats))
            dropdown_menu.add_command(label="→ Peripherie", command=lambda: controller.show_frame(Profil))
            dropdown_menu.add_command(label="→ Andere", command=lambda: controller.show_frame(Einstellungen))
            dropdown_menu.post(grp8_button.winfo_rootx(), grp8_button.winfo_rooty() + grp8_button.winfo_height())

        grp8_button = tk.Button(verzeichniss, text="Gruppe 8   ", bd=0, bg=SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=show_dropdown_grp8)
        grp8_button.pack(pady=10, anchor='w')

#Seiteninhalt
        #switch_button = tk.Button(self, text="switch", bg='#081424', fg='white',
                                  #font=("Inter", 20, 'bold'),
                                  #command=lambda: controller.show_frame(Gerateansicht))
        #switch_button.grid(row=4, column=0, pady=20)
        #Bilder
        self.imgFilter = load_image("assets/Filter_Button.png")
        self.imgSuche = load_image("assets/Search.png")
        self.imgHinzufugen = load_image("assets/Hinzufügen_Button.png")
        self.imgAktionen = load_image("assets/Aktionen_Button.png")

        #Filterfunktion
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
        #Suche
        suche_button = tk.Button(self.ubersicht_frame, image=self.imgSuche, bd=0, bg=SRH_Grey, command=lambda: print(f"nach {suche_entry} gesucht"))
        suche_entry = tk.Entry(self.ubersicht_frame, bg='#D9D9D9', bd=0, font=("Inter", 12))

        suche_button.place(relx=0.1, rely=0.1, relheight=0.04, relwidth=0.02)
        suche_entry.place(relx=0.12, rely=0.1, relwidth=0.33, relheight=0.04)

        #Hinzufügen
        Hinzufugen_button = tk.Button(self.ubersicht_frame, image=self.imgHinzufugen, bd=0, bg='white', command=lambda: controller.show_frame(Gerateansicht))
        Hinzufugen_button.place(relx=0.5, rely=0.1)

        #Aktionen
        Aktionen_button = tk.Button(self.ubersicht_frame, image=self.imgAktionen, bd=0, bg='white', command=lambda: print("Aktionen werden ausgeführt"))
        Aktionen_button.place(relx=0.6, rely=0.1)

        #Tabelle
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
        self.imglogin = tk.PhotoImage(file="assets/X.png")
        self.imgmainpage = tk.PhotoImage(file="assets/greyback.png")
        self.imgprofil = load_image("assets/Y.png")

        # Stil für Header und Footer anpassen
        style = ttk.Style()
        style.configure("Header.TLabel", foreground='white', background=SRH_Orange, font=("Inter", 50, 'bold'))
        style.configure("Footer.TLabel", background=SRH_Grey)

        # Buttons hinzufügen
        login = tk.Button(header, image=self.imglogin, bd=0, bg=SRH_Orange,
                          command=lambda: controller.show_frame(LogInWindow))
        profil = tk.Button(header, image=self.imgprofil, bd=0, bg=SRH_Orange,
                           command=lambda: controller.show_frame(Profil))

        # Mainpage-Button innerhalb von gerateansicht_frame, an der gleichen Position wie das profilbild in Profil
        mainpage = tk.Button(self, image=self.imgmainpage, bd=0, bg='white',
                             command=lambda: controller.show_frame(Ubersicht))
        #Seiteninhalt
        tree = ttk.Treeview(self.gerateansicht_frame, columns=("c1", "c2", "c3", "c4", "c5", "c6"), show="headings", height=5)
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


class Profil(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg='white')


        # Header für die Hauptseite
        header = ttk.Label(self, text="Profil", anchor="center", style="Header.TLabel")
        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)

        # Seitennavigation und laden der Bilder für Buttons
        verzeichniss = tk.Frame(self, bg=SRH_Grey)
        verzeichniss.place(relx=0, rely=0.15, relwidth=0.15, relheight=0.85)
        self.profil_frame = tk.Frame(self, bg='white')
        self.profil_frame.place(relx=0.21, rely=0.15, relwidth=1, relheight=0.85)

        self.imglogin = tk.PhotoImage(
            file="assets/X.png")
        self.imgmainpage = tk.PhotoImage(
            file="assets/Z.png")
        self.imgProfileTest = tk.PhotoImage(file="assets/profile.png")

        # Positionierung der Buttons
        login = tk.Button(header, image=self.imglogin, bd=0, bg=SRH_Orange,
                            command=lambda: controller.show_frame(LogInWindow))
        mainpage = tk.Button(header, image=self.imgmainpage, bd=0, bg=SRH_Orange,
                            command=lambda: controller.show_frame(MainPage))
        profilbild = tk.Button(self, image=self.imgProfileTest, bd=0, bg='white',
                               command=lambda: controller.show_frame(MainPage))

        login.place(relx=0.95, rely=0.5, anchor="center")
        mainpage.place(relx=0.90, rely=0.5, anchor="center")

        # Seitennavigations-Buttons für Benutzer, Admin, Statistiken und Einstellungen
        user_button = tk.Button(verzeichniss, text="User", bd=0, bg=SRH_Grey, fg='black', font=("Inter", 20, 'bold'),
                                command=lambda: controller.show_frame(Profil))
        user_button.pack(pady=10, anchor='w')

        admin_button = tk.Button(verzeichniss, text="Administration", bd=0, bg=SRH_Grey, fg='black',
                                 font=("Inter", 20, 'bold'),
                                 command=lambda: controller.show_frame(Admin))
        admin_button.pack(pady=10, anchor='w')

        stats_button = tk.Button(verzeichniss, text="Statistiken", bd=0, bg=SRH_Grey, fg='black',
                                 font=("Inter", 20, 'bold'),
                                 command=lambda: controller.show_frame(Stats))
        stats_button.pack(pady=10, anchor='w')

        einstellungen_button = tk.Button(verzeichniss, text="Einstellungen", bd=0, bg=SRH_Grey, fg='black',
                                 font=("Inter", 20, 'bold'),
                                 command=lambda: controller.show_frame(Einstellungen))
        einstellungen_button.pack(pady=10, anchor='w')

        profilbild.place(relx=0.16, rely=0.16, anchor='nw')

class Admin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')

        # Header-Label für die Profilseite
        header = ttk.Label(self, text="Administration", anchor="center", style="Header.TLabel")
        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)

        # Seitennavigation und laden der Bilder
        verzeichniss = tk.Frame(self, bg=SRH_Grey)
        self.admin_frame = tk.Frame(self, bg='white')

        self.imglogin = tk.PhotoImage(
            file="assets/X.png")
        self.imgmainpage = tk.PhotoImage(
            file="assets/Z.png")

        # Positionierung und Seitennavigations-Buttons für Benutzer, Admin, Statistiken und Einstellungen, Login,
        # Hauptseite und Profilbild
        login = tk.Button(header, image=self.imglogin, bd=0, bg=SRH_Orange,
                            command=lambda: controller.show_frame(LogInWindow))
        mainpage = tk.Button(header, image=self.imgmainpage, bd=0, bg=SRH_Orange,
                            command=lambda: controller.show_frame(MainPage))

        login.place(relx=0.95, rely=0.5, anchor="center")
        mainpage.place(relx=0.90, rely=0.5, anchor="center")

        user_button = tk.Button(verzeichniss, text="User", bd=0, bg=SRH_Grey, fg='black', font=("Inter", 20, 'bold'),
                                command=lambda: controller.show_frame(Profil))
        user_button.pack(pady=10, anchor='w')

        admin_button = tk.Button(verzeichniss, text="Administration", bd=0, bg=SRH_Grey, fg='black',
                                 font=("Inter", 20, 'bold'),
                                 command=lambda: controller.show_frame(Admin))
        admin_button.pack(pady=10, anchor='w')

        stats_button = tk.Button(verzeichniss, text="Statistiken", bd=0, bg=SRH_Grey, fg='black',
                                 font=("Inter", 20, 'bold'),
                                 command=lambda: controller.show_frame(Stats))
        stats_button.pack(pady=10, anchor='w')

        einstellungen_button = tk.Button(verzeichniss, text="Einstellungen", bd=0, bg=SRH_Grey, fg='black',
                                 font=("Inter", 20, 'bold'),
                                 command=lambda: controller.show_frame(Einstellungen))
        einstellungen_button.pack(pady=10, anchor='w')

        self.admin_frame.place(relx=0.21, rely=0.15, relwidth=1, relheight=0.85)
        verzeichniss.place(relx=0, rely=0.15, relwidth=0.15, relheight=0.85)

class Stats(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg='white')

        # Header-Label für die Statistikseite
        header = ttk.Label(self, text="Statistiken", anchor="center", style="Header.TLabel")
        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)

        # Navigationsleiste auf der linken Seite
        verzeichniss = tk.Frame(self, bg=SRH_Grey)
        self.stats_frame = tk.Frame(self, bg='white')

        # Bilder für die Login- und Hauptseite-Buttons laden
        self.imglogin = tk.PhotoImage(
            file="assets/X.png")
        self.imgmainpage = tk.PhotoImage(
            file="assets/Z.png")

        # Header-Navigationsbuttons (Login und Hauptseite), Platzierung der Header-Buttons
        login = tk.Button(header, image=self.imglogin, bd=0, bg=SRH_Orange,
                            command=lambda: controller.show_frame(LogInWindow))
        mainpage = tk.Button(header, image=self.imgmainpage, bd=0, bg=SRH_Orange,
                            command=lambda: controller.show_frame(MainPage))

        login.place(relx=0.95, rely=0.5, anchor="center")
        mainpage.place(relx=0.90, rely=0.5, anchor="center")

        # Linksseitige Navigationsbutton für verschiedene Ansichten
        user_button = tk.Button(verzeichniss, text="User", bd=0, bg=SRH_Grey, fg='black', font=("Inter", 20, 'bold'),
                                command=lambda: controller.show_frame(Profil))
        user_button.pack(pady=10, anchor='w')

        admin_button = tk.Button(verzeichniss, text="Administration", bd=0, bg=SRH_Grey, fg='black',
                                 font=("Inter", 20, 'bold'),
                                 command=lambda: controller.show_frame(Admin))
        admin_button.pack(pady=10, anchor='w')

        stats_button = tk.Button(verzeichniss, text="Statistiken", bd=0, bg=SRH_Grey, fg='black',
                                 font=("Inter", 20, 'bold'),
                                 command=lambda: controller.show_frame(Stats))
        stats_button.pack(pady=10, anchor='w')

        einstellungen_button = tk.Button(verzeichniss, text="Einstellungen", bd=0, bg=SRH_Grey, fg='black',
                                 font=("Inter", 20, 'bold'),
                                 command=lambda: controller.show_frame(Einstellungen))
        einstellungen_button.pack(pady=10, anchor='w')

        # Platzierung des Hauptinhaltsbereichs und der Navigationsleiste
        self.stats_frame.place(relx=0.21, rely=0.15, relwidth=1, relheight=0.85)
        verzeichniss.place(relx=0, rely=0.15, relwidth=0.15, relheight=0.85)

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
        verzeichniss = tk.Frame(self, bg=SRH_Grey)
        self.einstellung_frame = tk.Frame(self, bg='white')

        einstellungen_frame = ttk.Label(self, text="Einstellungen", anchor="center", style="Einstellungen.TLabel")

        # Navigationsbuttons im Header (Login und Mainpage)
        self.imglogin = tk.PhotoImage(
            file="assets/X.png")
        self.imgmainpage = tk.PhotoImage(
            file="assets/Z.png")

        login = tk.Button(self.header, image=self.imglogin, bd=0,bg=SRH_Orange,
                            command=lambda: controller.show_frame(LogInWindow))
        mainpage = tk.Button(self.header, image=self.imgmainpage, bd=0,bg=SRH_Orange,
                            command=lambda: controller.show_frame(MainPage))
        #login_label = tk.Button(self.header, text="🚪",bd=0, fg='#858383', font=("Inter", 19), command=lambda: controller.show_frame(LogInWindow))
        #login_label.place(relx=0.70, rely=0.5, anchor="center")
        # Platzierung der Header-Navigationsbuttons, Linksseitige Navigationsbuttons für andere Ansichten (Profil, Admin, Stats, EinstellungenO
        login.place(relx=0.95, rely=0.5, anchor="center")
        mainpage.place(relx=0.90, rely=0.5, anchor="center")

        user_button = tk.Button(verzeichniss, text="User", bd=0, bg=SRH_Grey, fg='black', font=("Inter", 20, 'bold'),
                                command=lambda: controller.show_frame(Profil))
        user_button.pack(pady=10, anchor='w')

        admin_button = tk.Button(verzeichniss, text="Administration", bd=0, bg=SRH_Grey, fg='black',
                                 font=("Inter", 20, 'bold'),
                                 command=lambda: controller.show_frame(Admin))
        admin_button.pack(pady=10, anchor='w')

        stats_button = tk.Button(verzeichniss, text="Statistiken", bd=0, bg=SRH_Grey, fg='black',
                                 font=("Inter", 20, 'bold'),
                                 command=lambda: controller.show_frame(Stats))
        stats_button.pack(pady=10, anchor='w')

        einstellungen_button = tk.Button(verzeichniss, text="Einstellungen", bd=0, bg=SRH_Grey, fg='black',
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
        format_drop = tk.Button(self.einstellung_frame, text="Format exportieren in", bd=0, bg='white', fg=SRH_Grey,
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
        darstellung_label = tk.Label(self.einstellung_frame, text="Darstellung", bg='white', fg='#858383', font=("Inter", 19))
        darstellung_label.place(relx=0.0, rely=0.32)


        # Bildvariablen zur Theme-Umschaltung
        try:
            self.light = PhotoImage(file="assets/switchoff.png")
            self.dark = PhotoImage(file="assets/switchon.png")
        except EXCEPTION as e:
            print(f"Fehler beim laden der Bilder: {e}")
            return # Beende falls die Bilder nicht geladen werden können

        def toggle():
            if self.switch_value:
                apply_darkmode()
                self.switch.config(image=self.dark, bg="black", activebackground="black")
                self.switch_value = False
            else:
                apply_lightmode()
                self.switch.config(image=self.light, bg="white", activebackground="white")
                self.switch_value = True

        #Funktion zum Anwenden des Darkmodes
        def apply_darkmode():
            self.config(bg=Darkmode_Black)
            self.einstellung_frame.config(bg=Darkmode_Black)
            verzeichniss.config(bg=Darkmode_Grey)
            user_button.config(bg=Darkmode_Grey, fg="white")
            admin_button.config(bg=Darkmode_Grey, fg="white")
            stats_button.config(bg=Darkmode_Grey, fg="white")
            einstellungen_button.config(bg=Darkmode_Grey, fg="white")

            addSpalten_button.config(bg=Darkmode_Black, fg="white")
            addTyp_button.config(bg=Darkmode_Black, fg="white")
            addGerat_button.config(bg=Darkmode_Black, fg="white")
            addStatus_button.config(bg=Darkmode_Black, fg="white")

            details_label.config(bg=Darkmode_Black, fg="white")
            darstellung_label.config(bg=Darkmode_Black, fg="white")
            datenbank_label.config(bg=Darkmode_Black, fg="white")
        #Funktion zum Anwenden des Lightmodes
        def apply_lightmode():
            self.config(bg="white")
            self.einstellung_frame.config(bg="white")
            verzeichniss.config(bg=SRH_Grey)
            user_button.config(bg=SRH_Grey, fg="black")
            admin_button.config(bg=SRH_Grey, fg="black")
            stats_button.config(bg=SRH_Grey, fg="black")
            einstellungen_button.config(bg=SRH_Grey, fg="black")

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
                self.header.configure(background=SRH_Orange)
                login.config(bg=SRH_Orange)
                mainpage.config(bg=SRH_Orange)
            elif selected_color == "Blau":
                self.header.configure(background=SRH_Blau)
                login.config(bg=SRH_Blau)
                mainpage.config(bg=SRH_Blau)
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
        datenbank_label = tk.Label(self.einstellung_frame, text="Datenbank", bg='white', fg='#858383', font=("Inter", 19))
        datenbank_label.place(relx=0.0, rely=0.59)

        addSpalten_button = tk.Button(self.einstellung_frame, text="Spalte\t+",  bd=0, bg='white', fg='black', font=("Inter", 16),
                                command=lambda: print("Spalte hinzugefügt"))
        addSpalten_button.place(relx=0.01, rely=0.64, relheight=0.032)

        addStatus_button = tk.Button(self.einstellung_frame, text="Status\t+",  bd=0, bg='white', fg='black', font=("Inter", 16),
                                command=lambda: print("Status hinzugefügt"))
        addStatus_button.place(relx=0.01, rely=0.69, relheight=0.032)

        addTyp_button = tk.Button(self.einstellung_frame, text="Typ\t+",  bd=0, bg='white', fg='black', font=("Inter", 16),
                                command=lambda: print("Typ hinzugefügt"))
        addTyp_button.place(relx=0.01, rely=0.74, relheight=0.032)

        addGerat_button = tk.Button(self.einstellung_frame, text="Gerät\t+",  bd=0, bg='white', fg='black', font=("Inter", 16),
                                command=lambda: controller.show_frame(Gerateansicht))
        addGerat_button.place(relx=0.01, rely=0.79, relheight=0.032)

        # Platzierung der Hauptframe-Bereiche
        self.einstellung_frame.place(relx=0.15, rely=0.15, relwidth=1, relheight=0.85)
        self.header.place(relx=0, rely=0, relwidth=1, relheight=0.15)

app = GuiTest()
app.mainloop()