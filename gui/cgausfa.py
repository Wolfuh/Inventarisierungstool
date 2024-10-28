import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Klasse für die Haupt-GUI-Anwendung
class GuiTest(tk.Tk):

    # __init__-Funktion für die GUI-Anwendung
    def __init__(self, *args, **kwargs):
        # Initialisiert die Basisklasse Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # Setzt den Fenstertitel und Eigenschaften
        self.title("Prototyp")
        self.resizable(False, False)  # Verhindert das Ändern der Fenstergröße
        self.geometry("1920x1080")  # Setzt die Fenstergröße

        # Container-Frame für das Wechseln zwischen verschiedenen Seiten
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        # Konfiguriert das Grid-System, um das Frame flexibel zu gestalten
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Initialisiert ein leeres Dictionary zum Speichern der Seiten-Frames
        self.frames = {}

        # Iteriert über eine Liste der verschiedenen Fensterklassen
        for F in (logInWindow, mainPage, profil, admin, stats):
            # Erzeugt eine Instanz der jeweiligen Fensterklasse
            frame = F(container, self)

            # Speichert das Frame im Dictionary
            self.frames[F] = frame

            # Positioniert das Frame im Grid-System
            frame.grid(row=0, column=0, sticky="nsew")

        # Zeigt die Hauptseite beim Start an
        self.show_frame(mainPage)

    # Methode zum Anzeigen des aktuellen Frames
    def show_frame(self, cont):
        # Wechselt zu dem Frame, das als Parameter übergeben wird
        frame = self.frames[cont]
        frame.tkraise()  # Bringt das Frame in den Vordergrund


# Klasse für das Login-Fenster
class logInWindow(tk.Frame):

    # Initialisiert das Login-Fenster
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Konfiguriert das Grid für dynamische Platzierung der Widgets
        self.grid_rowconfigure(2, weight=1)  # Platz oberhalb des Frames
        self.grid_rowconfigure(1, weight=2)  # Platz unterhalb des Frames
        self.grid_columnconfigure(0, weight=3)  # Platz links und rechts
        self.configure(bg='white')  # Setzt den Hintergrund auf weiß

        # Header-Label für den Titel
        header = ttk.Label(
            self,
            text="Login",
            anchor="center",
            style="Header.TLabel"
        )

        # Footer als dekoratives Label am unteren Rand
        bottom = ttk.Label(
            self,
            style="Footer.TLabel"
        )

        # Stile für moderne Optik definieren
        style = ttk.Style()
        style.configure("Header.TLabel", foreground='white', background='#DF4807', font=("Inter", 50, 'bold'))
        style.configure("Footer.TLabel", background='#D9D9D9')

        # Funktion für die Login-Überprüfung
        def login():
            username = "1"  # Harcodierter Benutzername
            password = "1"  # Harcodiertes Passwort
            # Überprüft, ob die Eingaben mit den vordefinierten Werten übereinstimmen
            if username_entry.get() == username and password_entry.get() == password:
                controller.show_frame(mainPage)  # Wechselt zur Hauptseite
                password_entry.delete(0, 'end')  # Leert das Passwortfeld
                username_entry.delete(0, 'end')  # Leert das Benutzernamefeld
            else:
                # Zeigt eine Fehlermeldung an, wenn die Eingaben falsch sind
                messagebox.showinfo(title="Fehler", message="Passwort oder Benutzername falsch")
                password_entry.delete(0, 'end')  # Leert nur das Passwortfeld bei Fehler

        # Frame für die Anmelde-Widgets
        login_frame = tk.Frame(self, bg='white')

        # Anmelde-Widgets (Label und Eingabefelder)
        login_label = tk.Label(login_frame, text="", bg='white', font=("Inter", 23, 'bold'))
        username_label = tk.Label(login_frame, text="Benutzername", bg='white', font=("Inter", 19))
        username_entry = tk.Entry(login_frame, bg='white', font=("Inter", 15))
        password_entry = tk.Entry(login_frame, show="*", bg='white', font=("Inter", 15))  # Passwortfeld mit verdecktem Text
        password_label = tk.Label(login_frame, text="Passwort ", bg='white', font=("Inter", 19))
        login_button = tk.Button(
            login_frame, text="Login", bg='#081424', fg='white', font=("Inter", 20, 'bold'), command=login)

        # Positionierung der Anmelde-Widgets im Grid
        login_label.grid(row=5, column=1, columnspan=3, sticky="news", padx=40, pady=40)
        username_label.grid(row=6, column=1)
        username_entry.grid(row=7, column=1, padx=30, pady=10)
        password_label.grid(row=8, column=1)
        password_entry.grid(row=9, column=1, padx=30, pady=10)
        login_button.grid(row=10, column=0, columnspan=2, padx=40, pady=30)

        # Positionierung des Headers und Footers im Fenster
        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)  # Header nimmt 15% der Fensterhöhe ein
        bottom.place(relx=0, rely=0.85, relwidth=1, relheight=0.13)  # Footer unten am Fenster (13% Höhe)

        # Positionierung des Anmelde-Frames im Grid
        login_frame.grid(row=1, column=0)


# Klasse für die Hauptseite nach dem Login
class mainPage(tk.Frame):

    # Initialisiert die Hauptseite
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Setzt den Hintergrund und konfiguriert das Grid-System
        self.configure(bg='white')
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)

        # Header für die Hauptseite
        header = ttk.Label(
            self,
            text="Startseite",
            anchor="center",
            style="Header.TLabel"
        )

        # Konfiguriert das Grid für den Header
        header.grid_columnconfigure(0, weight=1)
        header.grid_columnconfigure(1, weight=1)
        header.grid_rowconfigure(0, weight=1)

        # Buttons mit Bildern, um zwischen den Seiten zu wechseln
        self.imgButton1 = tk.PhotoImage(file="assets/X.png")  # Bild für Button 1
        self.imgButton2 = tk.PhotoImage(file="assets/Y.png")  # Bild für Button 2

        button1 = tk.Button(header, image=self.imgButton1, bd=0, bg='#DF4807', command=lambda: controller.show_frame(logInWindow))
        button2 = tk.Button(header, image=self.imgButton2, bd=0, bg='#DF4807', command=lambda: controller.show_frame(profil))

        # Footer-Label für dekoratives Element unten
        bottom = ttk.Label(
            self,
            style="Footer.TLabel"
        )

        # TTK-Style für moderne Optik
        style = ttk.Style()
        style.configure("Header.TLabel", foreground='white', background='#DF4807', font=("Inter", 55, 'bold'))
        style.configure("Footer.TLabel", background='#D9D9D9')

        # Positionierung der Buttons im Grid
        button1.grid(row=2, column=3, padx=30, pady=65)
        button2.grid(row=2, column=2, padx=0, pady=65)

        # Platzierung von Header und Footer relativ zur Fenstergröße
        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)
        bottom.place(relx=0, rely=0.85, relwidth=1, relheight=0.13)


# Klasse für die Profil-Seite
class profil(tk.Frame):

    # Initialisiert die Profilseite
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

    # Rahmen
        # Setzt den Hintergrund auf weiß
        self.configure(bg='white')

        # Label für den Profilname (ist nur Platzhalter)
        profilName = ttk.Label(
            self, text="Helen Zimmer", font=("Inter", 20, 'bold')
        )


        # Header-Label für die Profilseite
        header = ttk.Label(
            self,
            text="Profil",
            anchor="center",
            style="Header.TLabel"
        )

        verzeichniss = ttk.Label(
            self,
            anchor='w',
            style="Footer.TLabel"
        )
        # Konfiguriert das Grid für den Header
        header.grid_columnconfigure(0, weight=1)
        header.grid_columnconfigure(1, weight=1)
        header.grid_rowconfigure(0, weight=1)

        # Buttons mit Bildern, um zwischen den Seiten zu wechseln
        self.imgButton1 = tk.PhotoImage(file="assets/X.png")  # Bild für Button 1
        self.imgButton2 = tk.PhotoImage(file="assets/Z.png")  # Bild für Button 2
        self.imgProfileTest = tk.PhotoImage(file="assets/profile.png")  # Bild fÃ¼r User
        imgBitteBesserBenennen = tk.Label(self, image=self.imgProfileTest)
        imgBitteBesserBenennen.pack()
        # self.imgProfileTest = tk.PhotoImage(file="assets/profile.png") #Bild für User

        button1 = tk.Button(header, image=self.imgButton1, bd=0, bg='#DF4807',command=lambda: controller.show_frame(logInWindow))
        button2 = tk.Button(header, image=self.imgButton2, bd=0, bg='#DF4807', command=lambda: controller.show_frame(mainPage))

        # # Inhalt der Seite
        # nameDesMitarbeiters = tk.Label(text="Hammi", bg='white', font=("Inter", 19))
        #     name_label = tk.Label(text="Name", bg='white', font=("Inter", 19))
        #     name_entry = tk.Entry(bg='white', font=("Inter", 15))
        #     name_label.grid(row=6, column=1)
        #     name_entry.grid(row=7, column=1, padx=30, pady=10)
        # nameDesMitarbeiters.grid()


        # Positionierung der Buttons im Grid
        button1.grid(row=2, column=3, padx=30, pady=65)
        button2.grid(row=2, column=2, padx=0, pady=65)
        imgBitteBesserBenennen.grid(row=3, column=6, padx=310, pady=180)

        profilName.grid(row=4, column=6, padx=500, pady=80)
        #Verzeichniss
        user_button = tk.Button(verzeichniss, text="User",bd=0, bg='#D9D9D9', fg='black', font=("Inter", 20, 'bold'),
                            command=lambda: controller.show_frame(profil))
        user_button.grid(row=2, column=3, padx=1, pady=65, sticky='w')

        admin_button = tk.Button(verzeichniss, text="Administration",bd=0, bg='#D9D9D9', fg='black', font=("Inter", 20, 'bold'),
                            command=lambda: controller.show_frame(admin))
        admin_button.grid(row=3, column=3, padx=1, pady=65, sticky='w')

        stats_button = tk.Button(verzeichniss, text="Statistiken",bd=0, bg='#D9D9D9', fg='black', font=("Inter", 20, 'bold'),
                            command=lambda: controller.show_frame(stats))
        stats_button.grid(row=4, column=3, padx=1, pady=65, sticky='w')

        # Positionierung des Headers im Fenster
        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)
        verzeichniss.place(relx=0, rely=0.15, relwidth=0.15, relheight=0.85)

class admin(tk.Frame):

    # Initialisiert die Hauptseite
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Setzt den Hintergrund und konfiguriert das Grid-System
        self.configure(bg='white')
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)

        # Header für die Hauptseite
        header = ttk.Label(
            self,
            text="Administration",
            anchor="center",
            style="Header.TLabel"
        )
        verzeichniss = ttk.Label(
            self,
            anchor='w',
            style="Footer.TLabel"
        )

        # Buttons mit Bildern, um zwischen den Seiten zu wechseln
        self.imgButton1 = tk.PhotoImage(file="assets/X.png")  # Bild für Button 1
        self.imgButton2 = tk.PhotoImage(file="assets/Z.png")  # Bild für Button 2

        button1 = tk.Button(header, image=self.imgButton1, bd=0, bg='#DF4807',
                            command=lambda: controller.show_frame(logInWindow))
        button2 = tk.Button(header, image=self.imgButton2, bd=0, bg='#DF4807',
                            command=lambda: controller.show_frame(mainPage))

        # Positionierung der Buttons im Grid
        button1.grid(row=2, column=3, padx=30, pady=65)
        button2.grid(row=2, column=2, padx=0, pady=65)

        #Verzeichniss
        user_button = tk.Button(verzeichniss, text="User",bd=0, bg='#D9D9D9', fg='black', font=("Inter", 20, 'bold'),
                            command=lambda: controller.show_frame(profil))
        user_button.grid(row=2, column=3, padx=1, pady=65, sticky='w')

        admin_button = tk.Button(verzeichniss, text="Administration",bd=0, bg='#D9D9D9', fg='black', font=("Inter", 20, 'bold'),
                            )
        admin_button.grid(row=3, column=3, padx=1, pady=65, sticky='w')

        stats_button = tk.Button(verzeichniss, text="Statistiken",bd=0, bg='#D9D9D9', fg='black', font=("Inter", 20, 'bold'),
                            command=lambda: controller.show_frame(stats))
        stats_button.grid(row=4, column=3, padx=1, pady=65, sticky='w')

        # Konfiguriert das Grid für den Header
        header.grid_columnconfigure(0, weight=1)
        header.grid_columnconfigure(1, weight=1)
        header.grid_rowconfigure(0, weight=1)

        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)
        verzeichniss.place(relx=0, rely=0.15, relwidth=0.15, relheight=0.85)



class stats(tk.Frame):

    # Initialisiert die Hauptseite
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Setzt den Hintergrund und konfiguriert das Grid-System
        self.configure(bg='white')
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)

        # Header für die Hauptseite
        header = ttk.Label(
            self,
            text="Statistiken",
            anchor="center",
            style="Header.TLabel"
        )
        verzeichniss = ttk.Label(
            self,
            anchor='w',
            style="Footer.TLabel"
        )

        # Buttons mit Bildern, um zwischen den Seiten zu wechseln
        self.imgButton1 = tk.PhotoImage(file="assets/X.png")  # Bild für Button 1
        self.imgButton2 = tk.PhotoImage(file="assets/Z.png")  # Bild für Button 2

        button1 = tk.Button(header, image=self.imgButton1, bd=0, bg='#DF4807',
                            command=lambda: controller.show_frame(logInWindow))
        button2 = tk.Button(header, image=self.imgButton2, bd=0, bg='#DF4807',
                            command=lambda: controller.show_frame(mainPage))

        # Positionierung der Buttons im Grid
        button1.grid(row=2, column=3, padx=30, pady=65)
        button2.grid(row=2, column=2, padx=0, pady=65)

        #Verzeichniss
        user_button = tk.Button(verzeichniss, text="User",bd=0, bg='#D9D9D9', fg='black', font=("Inter", 20, 'bold'),
                            command=lambda: controller.show_frame(profil))
        user_button.grid(row=2, column=3, padx=1, pady=65, sticky='w')

        admin_button = tk.Button(verzeichniss, text="Administration",bd=0, bg='#D9D9D9', fg='black', font=("Inter", 20, 'bold'),
                            command=lambda: controller.show_frame(admin))
        admin_button.grid(row=3, column=3, padx=1, pady=65, sticky='w')

        stats_button = tk.Button(verzeichniss, text="Statistiken",bd=0, bg='#D9D9D9', fg='black', font=("Inter", 20, 'bold'),
                            )
        stats_button.grid(row=4, column=3, padx=1, pady=65, sticky='w')

        # Konfiguriert das Grid für den Header
        header.grid_columnconfigure(0, weight=1)
        header.grid_columnconfigure(1, weight=1)
        header.grid_rowconfigure(0, weight=1)

        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)
        verzeichniss.place(relx=0, rely=0.15, relwidth=0.15, relheight=0.85)



# Treiber-Code zum Starten der Anwendung
app = GuiTest()  #


app.mainloop()