import tkinter as tk
from tkinter import ttk, messagebox
import os
from tkinter import *

# Farben der SRH (Corporate Design)
SRH_Orange = "#df4807"
SRH_Grey = "#d9d9d9"
SRH_Blau = "#10749c"

# Darkmode
Darkmode_Black = "#121212"
Darkmode_Grey = "#2d2d2d"

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

        for F in (LogInWindow, MainPage, MainPageS2, Ubersicht, Profil, Admin, Stats, Einstellungen):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


def load_image(image_path):
    if os.path.exists(image_path):
        return tk.PhotoImage(file=image_path)
    else:
        print(f"Warnung: Bild '{image_path}' nicht gefunden.")
        return None


class LogInWindow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')


        header = ttk.Label(self, text="Login", anchor="center", style="Header.TLabel")
        bottom = ttk.Label(self, style="Footer.TLabel")

        style = ttk.Style()
        style.configure("Header.TLabel", foreground='white', background=SRH_Orange, font=("Inter", 50, 'bold'))
        style.configure("Footer.TLabel", background=SRH_Grey)

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
        login_button = tk.Button(login_frame, text="Login", bg='#081424', fg='white', font=("Inter", 20, 'bold'),
                                 command=login)

        username_label.grid(row=0, column=0, pady=10)
        username_entry.grid(row=1, column=0, pady=10)
        password_label.grid(row=2, column=0, pady=10)
        password_entry.grid(row=3, column=0, pady=10)
        login_button.grid(row=4, column=0, pady=20)

        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)
        bottom.place(relx=0, rely=0.85, relwidth=1, relheight=0.13)
        login_frame.place(relx=0.5, rely=0.5, anchor="center")

class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')

        header = ttk.Label(self, text="Startseite", anchor="center", style="Header.TLabel")
        bottom = ttk.Label(self, style="Footer.TLabel")
        self.main_frame = tk.Frame(self, bg='white')
        self.main_frame.place(relx=0.21, rely=0.15, relwidth=1, relheight=0.65)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)

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
        bildgr8.place(relx=0.80, rely=0.55, anchor='n')

        all.place(relx=0.01, rely=0.18, anchor='w')
        seitevor.place(relx=0.51, rely=0.80, anchor='n')
        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)
        bottom.place(relx=0, rely=0.85, relwidth=1, relheight=0.13)

class MainPageS2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')

        header = ttk.Label(self, text="Startseite", anchor="center", style="Header.TLabel")
        bottom = ttk.Label(self, style="Footer.TLabel")
        self.main2_frame = tk.Frame(self, bg='white')
        self.main2_frame.place(relx=0.21, rely=0.15, relwidth=1, relheight=0.65)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)

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
        all = tk.Button(self, text="Alle anzeigen", bd=0, bg='white', fg='#1D4478', font=("Inter", 20),
                           command=lambda: controller.show_frame(Ubersicht))
        seitevor = tk.Button(self, image=self.imgseitevor, bd=0, bg='white', fg='#1E1E1E', font=("Inter", 16),
                        command=lambda: controller.show_frame(MainPageS2))
        seiteback = tk.Button(self, image=self.imgseiteback, bd=0, bg='white', fg='#1E1E1E', font=("Inter", 16),
                        command=lambda: controller.show_frame(MainPage))

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

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')
        style = ttk.Style()
        style.configure("Header.TLabel", foreground='white', background=SRH_Orange, font=("Inter", 55, 'bold'))
        style.configure("Footer.TLabel", background=SRH_Grey)
        header = ttk.Label(self, text="Geräteübersicht", anchor="center", style="Header.TLabel")
        verzeichniss = tk.Frame(self, bg=SRH_Grey)
        self.ubersicht_frame = tk.Frame(self, bg='white')
        self.ubersicht_frame.place(relx=0.21, rely=0.15, relwidth=1, relheight=0.85)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)

        self.imglogin = load_image("assets/X.png")
        self.imgprofil = load_image("assets/Y.png")

        login = tk.Button(header, image=self.imglogin, bd=0, bg=SRH_Orange,
                            command=lambda: controller.show_frame(LogInWindow))
        profil = tk.Button(header, image=self.imgprofil, bd=0, bg=SRH_Orange,
                            command=lambda: controller.show_frame(Profil))
        self.imgmainpage = tk.PhotoImage(
            file="assets/Z.png")

        mainpage = tk.Button(header, image=self.imgmainpage, bd=0, bg=SRH_Orange,
                            command=lambda: controller.show_frame(MainPage))

        all_button = tk.Button(verzeichniss, text="Alle anzeigen", bd=0, bg=SRH_Grey, fg='black', font=("Inter", 20, 'bold'),
                                command=lambda: controller.show_frame(Ubersicht))
        all_button.pack(pady=10, anchor='w')
#Gruppe 1
        grp1_button = tk.Button(verzeichniss, text="Gruppe 1", bd=0, bg=SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=lambda: controller.show_frame(Ubersicht))
        grp1_button = tk.Button(verzeichniss, text="Gruppe 1", bd=0, bg=SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=lambda: show_dropdown())
        grp1_button.pack(pady=10, anchor='w')

        def show_dropdown():
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg=SRH_Grey, fg='black')
            dropdown_menu.add_command(label="→ Hardware", command=lambda: controller.show_frame(Admin))
            dropdown_menu.add_command(label="→ Software", command=lambda: controller.show_frame(Stats))
            dropdown_menu.add_command(label="→ Peripherie", command=lambda: controller.show_frame(Profil))
            dropdown_menu.add_command(label="→ Andere", command=lambda: controller.show_frame(Einstellungen))
            dropdown_menu.place(relx=0.21, rely=0.5, relwidth=0.103, relheight=0.032)
            dropdown_menu.post(grp1_button.winfo_rootx(), grp1_button.winfo_rooty() + grp1_button.winfo_height())
#Gruppe 2
        grp2_button = tk.Button(verzeichniss, text="Gruppe 2", bd=0, bg=SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=lambda: controller.show_frame(Ubersicht))
        grp2_button = tk.Button(verzeichniss, text="Gruppe 2", bd=0, bg=SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=lambda: show_dropdown())
        grp2_button.pack(pady=10, anchor='w')

        def show_dropdown():
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg=SRH_Grey, fg='black')
            dropdown_menu.add_command(label="→ Hardware", command=lambda: controller.show_frame(Admin))
            dropdown_menu.add_command(label="→ Software", command=lambda: controller.show_frame(Stats))
            dropdown_menu.add_command(label="→ Peripherie", command=lambda: controller.show_frame(Profil))
            dropdown_menu.add_command(label="→ Andere", command=lambda: controller.show_frame(Einstellungen))

            dropdown_menu.post(grp2_button.winfo_rootx(), grp2_button.winfo_rooty() + grp2_button.winfo_height())
#Gruppe 3
        grp3_button = tk.Button(verzeichniss, text="Gruppe 3", bd=0, bg=SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=lambda: controller.show_frame(Ubersicht))
        grp3_button = tk.Button(verzeichniss, text="Gruppe 3", bd=0, bg=SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=lambda: show_dropdown())
        grp3_button.pack(pady=10, anchor='w')

        def show_dropdown():
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg=SRH_Grey, fg='black')
            dropdown_menu.add_command(label="→ Hardware", command=lambda: controller.show_frame(Admin))
            dropdown_menu.add_command(label="→ Software", command=lambda: controller.show_frame(Stats))
            dropdown_menu.add_command(label="→ Peripherie", command=lambda: controller.show_frame(Profil))
            dropdown_menu.add_command(label="→ Andere", command=lambda: controller.show_frame(Einstellungen))

            dropdown_menu.post(grp3_button.winfo_rootx(), grp3_button.winfo_rooty() + grp3_button.winfo_height())
#Gruppe 4
        grp4_button = tk.Button(verzeichniss, text="Gruppe 4", bd=0, bg=SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=lambda: controller.show_frame(Ubersicht))
        grp4_button = tk.Button(verzeichniss, text="Gruppe 4", bd=0, bg=SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=lambda: show_dropdown())
        grp4_button.pack(pady=10, anchor='w')

        def show_dropdown():
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg=SRH_Grey, fg='black')
            dropdown_menu.add_command(label="→ Hardware", command=lambda: controller.show_frame(Admin))
            dropdown_menu.add_command(label="→ Software", command=lambda: controller.show_frame(Stats))
            dropdown_menu.add_command(label="→ Peripherie", command=lambda: controller.show_frame(Profil))
            dropdown_menu.add_command(label="→ Andere", command=lambda: controller.show_frame(Einstellungen))

            dropdown_menu.post(grp4_button.winfo_rootx(), grp4_button.winfo_rooty() + grp4_button.winfo_height())
#Gruppe 5
        grp5_button = tk.Button(verzeichniss, text="Gruppe 5", bd=0, bg=SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=lambda: controller.show_frame(Ubersicht))
        grp5_button = tk.Button(verzeichniss, text="Gruppe 5", bd=0, bg=SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=lambda: show_dropdown())
        grp5_button.pack(pady=10, anchor='w')

        def show_dropdown():
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg=SRH_Grey, fg='black')
            dropdown_menu.add_command(label="→ Hardware", command=lambda: controller.show_frame(Admin))
            dropdown_menu.add_command(label="→ Software", command=lambda: controller.show_frame(Stats))
            dropdown_menu.add_command(label="→ Peripherie", command=lambda: controller.show_frame(Profil))
            dropdown_menu.add_command(label="→ Andere", command=lambda: controller.show_frame(Einstellungen))

            dropdown_menu.post(grp5_button.winfo_rootx(), grp5_button.winfo_rooty() + grp5_button.winfo_height())
#Grupe 6
        grp6_button = tk.Button(verzeichniss, text="Gruppe 6", bd=0, bg=SRH_Grey, fg='black',
                                 font=("Inter", 20, 'bold'),
                                 command=lambda: controller.show_frame(Ubersicht))
        grp6_button = tk.Button(verzeichniss, text="Gruppe 6", bd=0, bg=SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=lambda: show_dropdown())
        grp6_button.pack(pady=10, anchor='w')

        def show_dropdown():
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg=SRH_Grey, fg='black')
            dropdown_menu.add_command(label="→ Hardware", command=lambda: controller.show_frame(Admin))
            dropdown_menu.add_command(label="→ Software", command=lambda: controller.show_frame(Stats))
            dropdown_menu.add_command(label="→ Peripherie", command=lambda: controller.show_frame(Profil))
            dropdown_menu.add_command(label="→ Andere", command=lambda: controller.show_frame(Einstellungen))

            dropdown_menu.post(grp6_button.winfo_rootx(), grp6_button.winfo_rooty() + grp6_button.winfo_height())
#Gruppe 7
        grp7_button = tk.Button(verzeichniss, text="Gruppe 7", bd=0, bg=SRH_Grey, fg=SRH_Grey,
                                 font=("Inter", 20, 'bold'),
                                 command=lambda: controller.show_frame(Ubersicht))

        grp7_button = tk.Button(verzeichniss, text="Gruppe 7", bd=0, bg=SRH_Grey, fg='black',
                                 font=("Inter", 20, 'bold'),
                                 command=lambda: controller.show_frame(Ubersicht))
        grp7_button = tk.Button(verzeichniss, text="Gruppe 7", bd=0, bg=SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=lambda: show_dropdown())  # Button öffnet Dropdown-Menü
        grp7_button.pack(pady=10, anchor='w')

        # Funktion zur Anzeige des Dropdown-Menüs
        def show_dropdown():
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg=SRH_Grey, fg='black')
            dropdown_menu.add_command(label="→ Hardware", command=lambda: controller.show_frame(Admin))
            dropdown_menu.add_command(label="→ Software", command=lambda: controller.show_frame(Stats))
            dropdown_menu.add_command(label="→ Peripherie", command=lambda: controller.show_frame(Profil))
            dropdown_menu.add_command(label="→ Andere", command=lambda: controller.show_frame(Einstellungen))

            # Dropdown-Menü unterhalb des Buttons "Gruppe 8" anzeigen
            dropdown_menu.post(grp7_button.winfo_rootx(), grp7_button.winfo_rooty() + grp7_button.winfo_height())

        grp7_button = tk.Button(verzeichniss, text="Gruppe 7", bd=0, bg=SRH_Grey, fg=SRH_Grey,
                                 font=("Inter", 20, 'bold'),
                                 command=lambda: controller.show_frame(Ubersicht))
        #grp8_button.pack(pady=10, anchor='w')

#Gruppe 8
        grp8_button = tk.Button(verzeichniss, text="Gruppe 8", bd=0, bg=SRH_Grey, fg='black',
                                font=("Inter", 20, 'bold'),
                                command=lambda: show_dropdown())
        grp8_button.pack(pady=10, anchor='w')

        def show_dropdown():
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=0, bg=SRH_Grey, fg='black')
            dropdown_menu.add_command(label="→ Hardware", command=lambda: controller.show_frame(Admin))
            dropdown_menu.add_command(label="→ Software", command=lambda: controller.show_frame(Stats))
            dropdown_menu.add_command(label="→ Peripherie", command=lambda: controller.show_frame(Profil))
            dropdown_menu.add_command(label="→ Andere", command=lambda: controller.show_frame(Einstellungen))

            dropdown_menu.post(grp8_button.winfo_rootx(), grp8_button.winfo_rooty() + grp8_button.winfo_height())

        login.place(relx=0.95, rely=0.5, anchor="center")
        profil.place(relx=0.90, rely=0.5, anchor="center")
        mainpage.place(relx=0.85, rely=0.5, anchor="center")
        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)
        verzeichniss.place(relx=0, rely=0.15, relwidth=0.2, relheight=0.85)


class Profil(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg='white')

        # Header für die Hauptseite
        header = ttk.Label(self, text="Profil", anchor="center", style="Header.TLabel")
        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)


        verzeichniss = tk.Frame(self, bg=SRH_Grey)
        verzeichniss.place(relx=0, rely=0.15, relwidth=0.2, relheight=0.85)
        self.profil_frame = tk.Frame(self, bg='white')
        self.profil_frame.place(relx=0.21, rely=0.15, relwidth=1, relheight=0.85)

        self.imglogin = tk.PhotoImage(
            file="assets/X.png")
        self.imgmainpage = tk.PhotoImage(
            file="assets/Z.png")
        self.imgProfileTest = tk.PhotoImage(file="assets/profile.png")


        login = tk.Button(header, image=self.imglogin, bd=0, bg=SRH_Orange,
                            command=lambda: controller.show_frame(LogInWindow))
        mainpage = tk.Button(header, image=self.imgmainpage, bd=0, bg=SRH_Orange,
                            command=lambda: controller.show_frame(MainPage))
        profilbild = tk.Button(self, image=self.imgProfileTest, bd=0, bg='white',
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

        profilbild.place(relx=0.2, rely=0.15, anchor='nw')



class Admin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg='white')

        header = ttk.Label(self, text="Administration", anchor="center", style="Header.TLabel")
        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)

        verzeichniss = tk.Frame(self, bg=SRH_Grey)
        self.admin_frame = tk.Frame(self, bg='white')

        self.imglogin = tk.PhotoImage(
            file="assets/X.png")
        self.imgmainpage = tk.PhotoImage(
            file="assets/Z.png")

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
        verzeichniss.place(relx=0, rely=0.15, relwidth=0.2, relheight=0.85)



class Stats(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg='white')

        header = ttk.Label(self, text="Statistiken", anchor="center", style="Header.TLabel")
        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)

        verzeichniss = tk.Frame(self, bg=SRH_Grey)
        self.stats_frame = tk.Frame(self, bg='white')

        self.imglogin = tk.PhotoImage(
            file="assets/X.png")
        self.imgmainpage = tk.PhotoImage(
            file="assets/Z.png")

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

        self.stats_frame.place(relx=0.21, rely=0.15, relwidth=1, relheight=0.85)
        verzeichniss.place(relx=0, rely=0.15, relwidth=0.2, relheight=0.85)

class Einstellungen(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__()
        tk.Frame.__init__(self, parent)

        self.configure(bg='white')

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)

        self.header = ttk.Label(self, text="Einstellungen", anchor="center", style="Header.TLabel")
        self.header.place(relx=0, rely=0, relwidth=1, relheight=0.15)
        verzeichniss = tk.Frame(self, bg=SRH_Grey)

        self.einstellung_frame = tk.Frame(self, bg='white')


        einstellungen_frame = ttk.Label(self, text="Einstellungen", anchor="center", style="Einstellungen.TLabel")

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

        verzeichniss.place(relx=0, rely=0.15, relwidth=0.2, relheight=0.85)

# Seiteninhalt

        details_label = tk.Label(self.einstellung_frame, text="Details", bg='white', fg='#858383', font=("Inter", 19))
        details_label.place(relx=0.0, rely=0.15)

        format_drop = tk.Button(self.einstellung_frame, text="Format exportieren in", bd=0, bg='white', fg=SRH_Grey,
                                font=("Inter", 20, 'bold'),
                                command=lambda: controller.show_frame())

        format_drop = tk.Button(self.einstellung_frame, text="Format exportieren in", bd=0, bg='white', fg='black',
                                font=("Inter", 20, 'bold'),
                                command=lambda: controller.show_frame())
        format_drop = tk.Button(self.einstellung_frame, text="Format exportieren in ↴", bd=1, bg='white', fg='black',
                                font=("Inter", 12),
                                command=lambda: show_dropdown())  # Button öffnet Dropdown-Menü
        format_drop.place(relx=0.0, rely=0.20)

        # Funktion zur Anzeige des Dropdown-Menüs
        def show_dropdown():
            dropdown_menu = tk.Menu(verzeichniss, tearoff=0, bd=1, bg='white', fg='black')
            dropdown_menu.add_command(label="→ Excel", command=lambda: print("Excel ausgewählt"))
            dropdown_menu.add_command(label="→ SQL", command=lambda: print("SQL ausgewählt"))
            dropdown_menu.add_command(label="→ CSS", command=lambda: print("CSS ausgewählt"))
            dropdown_menu.add_command(label="→ Andere", command=lambda: print("Andere ausgewählt"))

            dropdown_menu.post(format_drop.winfo_rootx(), format_drop.winfo_rooty() + format_drop.winfo_height())


        darstellung_label = tk.Label(self.einstellung_frame, text="Darstellung", bg='white', fg='#858383', font=("Inter", 19))
        darstellung_label.place(relx=0.0, rely=0.32)


        # Store the images as instance variables to avoid garbage collection
        self.light = PhotoImage(file="assets/switchoff.png")
        self.dark = PhotoImage(file="assets/switchon.png")

        # Use an instance variable for switch_value
        self.switch_value = True

        # Defining a function to toggle between light and dark theme
        def toggle():
            # Access the instance variable using self
            if self.switch_value:
                self.switch.config(image=self.dark, bg=Darkmode_Black,
                                   activebackground=Darkmode_Black)
                # Changes the window and frame to dark theme
                self.config(bg=Darkmode_Black)  # Change the background of the main window
                self.einstellung_frame.config(bg=Darkmode_Black)
                self.config(bg=Darkmode_Grey)
                verzeichniss.config(bg=Darkmode_Grey)
                user_button.config(bg=Darkmode_Grey, fg="white")
                admin_button.config(bg=Darkmode_Grey, fg="white")
                stats_button.config(bg=Darkmode_Grey, fg="white")
                einstellungen_button.config(bg=Darkmode_Grey, fg="white")

                details_label.config(bg=Darkmode_Black, fg="white")
                darstellung_label.config(bg=Darkmode_Black, fg="white")
                datenbank_label.config(bg=Darkmode_Black, fg="white")
                # Change the background of the frame
                self.switch_value = False

            else:
                self.switch.config(image=self.light, bg="white",
                                   activebackground="white")

                # Changes the window and frame to light theme
                self.config(bg="white")  # Change the background of the main window

                self.einstellung_frame.config(bg="white")
                self.config(bg=SRH_Grey)
                verzeichniss.config(bg=SRH_Grey)
                user_button.config(bg=SRH_Grey, fg="black")
                admin_button.config(bg=SRH_Grey, fg="black")
                stats_button.config(bg=SRH_Grey, fg="black")
                einstellungen_button.config(bg=SRH_Grey, fg="black")

                details_label.config(bg="white", fg="black")
                darstellung_label.config(bg="white", fg="black")
                datenbank_label.config(bg="white", fg="black")

                # Change the background of the frame
                self.switch_value = True

        # Creating a button to toggle between light and dark themes
        self.switch = Button(self, image=self.light,
                             bd=0, bg="white",
                             activebackground="white",
                             command=toggle)
        self.switch.place(relx=0.21, rely=0.46)

        def change_header_color(event):
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

        # Creating a dropdown menu to select header color
        color_options = ["Orange", "Blau", "Lila"]
        color_dropdown = ttk.Combobox(self, values=color_options, state="readonly")
        color_dropdown.set("Farbeschema")  # Default text
        color_dropdown.place(relx=0.21, rely=0.5, relwidth=0.103, relheight=0.032)  # Adjust positioning as needed
        color_dropdown.bind("<<ComboboxSelected>>", change_header_color)




        datenbank_label = tk.Label(self.einstellung_frame, text="Datenbank", bg='white', fg='#858383', font=("Inter", 19))
        datenbank_label.place(relx=0.0, rely=0.59)
        self.einstellung_frame.place(relx=0.21, rely=0.15, relwidth=1, relheight=0.85)
        self.header.place(relx=0, rely=0, relwidth=1, relheight=0.15)

app = GuiTest()
app.mainloop()
