import tkinter as tk
from tkinter import ttk, messagebox
import os

# Klasse für die Haupt-GUI-Anwendung
class GuiTest(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Prototyp")
        self.resizable(False, False)
        self.geometry("1920x1080")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (LogInWindow, MainPage, Profil, Admin, Stats):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


def load_image(image_path):
    """Hilfsfunktion zum Laden von Bildern mit Fehlerbehandlung."""
    if os.path.exists(image_path):
        return tk.PhotoImage(file=image_path)
    else:
        print(f"Warnung: Bild '{image_path}' nicht gefunden.")
        return None  # Kein Bild wird zurückgegeben, wenn die Datei fehlt


# Klasse für das Login-Fenster
class LogInWindow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')

        header = ttk.Label(self, text="Login", anchor="center", style="Header.TLabel")
        bottom = ttk.Label(self, style="Footer.TLabel")

        style = ttk.Style()
        style.configure("Header.TLabel", foreground='white', background='#DF4807', font=("Inter", 50, 'bold'))
        style.configure("Footer.TLabel", background='#D9D9D9')

        def login():
            username = "1"
            password = "1"
            if username_entry.get() == username and password_entry.get() == password:
                controller.show_frame(MainPage)
                username_entry.delete(0, 'end')
                password_entry.delete(0, 'end')
            else:
                messagebox.showinfo(title="Fehler", message="Passwort oder Benutzername falsch")
                password_entry.delete(0, 'end')

        login_frame = tk.Frame(self, bg='white')
        username_label = tk.Label(login_frame, text="Benutzername", bg='white', font=("Inter", 19))
        username_entry = tk.Entry(login_frame, bg='white', font=("Inter", 15))
        password_label = tk.Label(login_frame, text="Passwort", bg='white', font=("Inter", 19))
        password_entry = tk.Entry(login_frame, show="*", bg='white', font=("Inter", 15))
        login_button = tk.Button(login_frame, text="Login", bg='#081424', fg='white', font=("Inter", 20, 'bold'), command=login)

        username_label.grid(row=0, column=0, pady=10)
        username_entry.grid(row=1, column=0, pady=10)
        password_label.grid(row=2, column=0, pady=10)
        password_entry.grid(row=3, column=0, pady=10)
        login_button.grid(row=4, column=0, pady=20)

        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)
        bottom.place(relx=0, rely=0.85, relwidth=1, relheight=0.13)
        login_frame.place(relx=0.5, rely=0.5, anchor="center")


# Klasse für die Hauptseite nach dem Login
class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')

        header = ttk.Label(self, text="Startseite", anchor="center", style="Header.TLabel")

        self.imgButton1 = load_image("assets/X.png")
        self.imgButton2 = load_image("assets/Y.png")

        button1 = tk.Button(header, image=self.imgButton1, bd=0, bg='#DF4807', command=lambda: controller.show_frame(LogInWindow))
        button2 = tk.Button(header, image=self.imgButton2, bd=0, bg='#DF4807', command=lambda: controller.show_frame(Profil))

        style = ttk.Style()
        style.configure("Header.TLabel", foreground='white', background='#DF4807', font=("Inter", 55, 'bold'))
        style.configure("Footer.TLabel", background='#D9D9D9')

        button1.grid(row=0, column=0, padx=10, pady=10)
        button2.grid(row=0, column=1, padx=10, pady=10)

        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)


# Klasse für die Profil-Seite
# Klasse für die Profil-Seite
class Profil(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Setzt den Hintergrund und konfiguriert das Grid-System
        self.configure(bg='white')

        # Header für die Hauptseite
        header = ttk.Label(self, text="Profil", anchor="center", style="Header.TLabel")
        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)

        # Verwende einen Frame anstelle eines Labels für das Verzeichnis
        verzeichniss = tk.Frame(self, bg='#D9D9D9')  # Auffällige Farbe für Debugging

        # Buttons mit Bildern, um zwischen den Seiten zu wechseln
        self.imgButton1 = tk.PhotoImage(file="H:/Ausbildung/Programmierung/trashpanda/assets/X.png")  # Bild für Button 1
        self.imgButton2 = tk.PhotoImage(file="H:/Ausbildung/Programmierung/trashpanda/assets/Z.png")  # Bild für Button 2
        self.imgProfileTest = tk.PhotoImage(file="H:/Ausbildung/Programmierung/trashpanda/assets/profile.png")

        button1 = tk.Button(header, image=self.imgButton1, bd=0, bg='#DF4807',
                            command=lambda: controller.show_frame(LogInWindow))
        button2 = tk.Button(header, image=self.imgButton2, bd=0, bg='#DF4807',
                            command=lambda: controller.show_frame(MainPage))
        profilbild = tk.Button(header, image=self.imgProfileTest, bd=0, bg='#DF4807',
                            command=lambda: controller.show_frame(MainPage))
        # Positionierung der Buttons im Header
        button1.place(relx=0.9, rely=0.5, anchor="center")
        button2.place(relx=0.8, rely=0.5, anchor="center")
        profilbild.grid(row=2, column=2, padx=0, pady=65)

        # Verzeichniss-Buttons im Frame hinzufügen
        user_button = tk.Button(verzeichniss, text="User", bd=0, bg='#D9D9D9', fg='black', font=("Inter", 20, 'bold'),
                                command=lambda: controller.show_frame(Profil))
        user_button.pack(pady=10, anchor='w')

        admin_button = tk.Button(verzeichniss, text="Administration", bd=0, bg='#D9D9D9', fg='black', font=("Inter", 20, 'bold'),
                                 command=lambda: controller.show_frame(Admin))
        admin_button.pack(pady=10, anchor='w')

        stats_button = tk.Button(verzeichniss, text="Statistiken", bd=0, bg='#D9D9D9', fg='black',
                                 font=("Inter", 20, 'bold'),
                                 command=lambda: controller.show_frame(Stats))
        stats_button.pack(pady=10, anchor='w')

        # Verzeichniss Frame anzeigen
        verzeichniss.place(relx=0, rely=0.15, relwidth=0.2, relheight=0.85)


# Klasse für die Admin-Seite
class Admin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Setzt den Hintergrund und konfiguriert das Grid-System
        self.configure(bg='white')

        # Header für die Hauptseite
        header = ttk.Label(self, text="Administration", anchor="center", style="Header.TLabel")
        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)

        # Verwende einen Frame anstelle eines Labels für das Verzeichnis
        verzeichniss = tk.Frame(self, bg='#D9D9D9')  # Auffällige Farbe für Debugging

        # Buttons mit Bildern, um zwischen den Seiten zu wechseln
        self.imgButton1 = tk.PhotoImage(file="H:/Ausbildung/Programmierung/trashpanda/assets/X.png")  # Bild für Button 1
        self.imgButton2 = tk.PhotoImage(file="H:/Ausbildung/Programmierung/trashpanda/assets/Z.png")  # Bild für Button 2

        button1 = tk.Button(header, image=self.imgButton1, bd=0, bg='#DF4807',
                            command=lambda: controller.show_frame(LogInWindow))
        button2 = tk.Button(header, image=self.imgButton2, bd=0, bg='#DF4807',
                            command=lambda: controller.show_frame(MainPage))

        # Positionierung der Buttons im Header
        button1.place(relx=0.9, rely=0.5, anchor="center")
        button2.place(relx=0.8, rely=0.5, anchor="center")

        # Verzeichniss-Buttons im Frame hinzufügen
        user_button = tk.Button(verzeichniss, text="User", bd=0, bg='#D9D9D9', fg='black', font=("Inter", 20, 'bold'),
                                command=lambda: controller.show_frame(Profil))
        user_button.pack(pady=10, anchor='w')

        admin_button = tk.Button(verzeichniss, text="Administration", bd=0, bg='#D9D9D9', fg='black', font=("Inter", 20, 'bold'),
                                 command=lambda: controller.show_frame(Admin))
        admin_button.pack(pady=10, anchor='w')

        stats_button = tk.Button(verzeichniss, text="Statistiken", bd=0, bg='#D9D9D9', fg='black',
                                 font=("Inter", 20, 'bold'),
                                 command=lambda: controller.show_frame(Stats))
        stats_button.pack(pady=10, anchor='w')

        # Verzeichniss Frame anzeigen
        verzeichniss.place(relx=0, rely=0.15, relwidth=0.2, relheight=0.85)


# Klasse für die Stats-Seite
class Stats(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Setzt den Hintergrund und konfiguriert das Grid-System
        self.configure(bg='white')

        # Header für die Hauptseite
        header = ttk.Label(self, text="Statistiken", anchor="center", style="Header.TLabel")
        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)

        # Verwende einen Frame anstelle eines Labels für das Verzeichnis
        verzeichniss = tk.Frame(self, bg='#D9D9D9')  # Auffällige Farbe für Debugging

        # Buttons mit Bildern, um zwischen den Seiten zu wechseln
        self.imgButton1 = tk.PhotoImage(file="H:/Ausbildung/Programmierung/trashpanda/assets/X.png")  # Bild für Button 1
        self.imgButton2 = tk.PhotoImage(file="H:/Ausbildung/Programmierung/trashpanda/assets/Z.png")  # Bild für Button 2

        button1 = tk.Button(header, image=self.imgButton1, bd=0, bg='#DF4807',
                            command=lambda: controller.show_frame(LogInWindow))
        button2 = tk.Button(header, image=self.imgButton2, bd=0, bg='#DF4807',
                            command=lambda: controller.show_frame(MainPage))

        # Positionierung der Buttons im Header
        button1.place(relx=0.9, rely=0.5, anchor="center")
        button2.place(relx=0.8, rely=0.5, anchor="center")

        # Verzeichniss-Buttons im Frame hinzufügen
        # Verzeichniss-Buttons im Frame hinzufügen
        user_button = tk.Button(verzeichniss, text="User", bd=0, bg='#D9D9D9', fg='black', font=("Inter", 20, 'bold'),
                                command=lambda: controller.show_frame(Profil))
        user_button.pack(pady=10, anchor='w')

        admin_button = tk.Button(verzeichniss, text="Administration", bd=0, bg='#D9D9D9', fg='black', font=("Inter", 20, 'bold'),
                                command=lambda: controller.show_frame(Admin))
        admin_button.pack(pady=10, anchor='w')

        stats_button = tk.Button(verzeichniss, text="Statistiken", bd=0, bg='#D9D9D9', fg='black',
                                 font=("Inter", 20, 'bold'),
                                 command=lambda: controller.show_frame(Stats))
        stats_button.pack(pady=10, anchor='w')

        # Verzeichniss Frame anzeigen
        verzeichniss.place(relx=0, rely=0.15, relwidth=0.2, relheight=0.85)


# Treiber-Code zum Starten der Anwendung
app = GuiTest()
app.mainloop()

