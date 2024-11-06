import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
import os
from tkinter import *



from gui.gui_prototyp import GuiTest, MainPage, MainPageS2, Ubersicht, Gerateansicht, Profil, Admin, Stats, Einstellungen



# Farben der SRH (Corporate Design)
SRH_Orange = "#df4807"
SRH_Grey = "#d9d9d9"
SRH_Blau = "#10749c"

# Darkmode_Farben
Darkmode_Black = "#121212"
Darkmode_Grey = "#2d2d2d"


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
            my_db = sqlite3.connect('./db/users.db')     # verbindung db
            my_dbc = my_db.cursor()                     # cursor erstellen

            username = username_entry.get()  # strip = leerzeichen werden entfernt
            password = password_entry.get()
            password_hex = password                                                 # verschlüsseltes passwort
            
            my_dbc.execute("""
                           SELECT * FROM users WHERE user_first_name = ? AND password = ?
                           """, (username, password_hex))
            
            res = my_dbc.fetchone()

            if res[5] is None:
                if res[5] == password:
                    controller.show_frame(MainPage)
                    username_entry.delete(0, 'end')
                    password_entry.delete(0, 'end')
                else:
                    messagebox.showinfo(title="Fehler", message="Passwort oder Benutzername falsch")
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

app = GuiTest()
app.mainloop()