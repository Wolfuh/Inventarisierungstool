import tkinter as tk
from tkinter import ttk

import configuration
import ThemeManager
import gui_prototyp
import Mainpages
import os

class Profil(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        root_path = os.path.dirname(os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir)))
        self.configure(bg='white')

        # Header für die Hauptseite
        header = ttk.Label(self, text="Profil", anchor="center", style="Header.TLabel")
        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)

        # Seitennavigation und laden der Bilder für Buttons
        verzeichniss = tk.Frame(self, bg=ThemeManager.SRH_Grey)
        verzeichniss.place(relx=0, rely=0.15, relwidth=0.15, relheight=0.85)
        self.profil_frame = tk.Frame(self, bg='white')


        self.imglogin = tk.PhotoImage(
            file=root_path+"/gui/assets/Closeicon.png")
        self.imgmainpage = tk.PhotoImage(
            file=root_path+"/gui/assets/backtosite_icon.png")
        self.imgProfileTest = tk.PhotoImage(file=root_path+"/gui/assets/profile.png")

        # Positionierung der Buttons
        login = tk.Button(header, image=self.imglogin, bd=0, bg=ThemeManager.SRH_Orange,
                          command=lambda: controller.show_frame(gui_prototyp.LogInWindow))
        mainpage = tk.Button(header, image=self.imgmainpage, bd=0, bg=ThemeManager.SRH_Orange,
                             command=lambda: controller.show_frame(Mainpages.MainPage))

        #Seiteninhalt
        profilbild = tk.Button(self.profil_frame, image=self.imgProfileTest, bd=0, bg='white',
                               command=lambda: controller.show_frame(Mainpages.MainPage))
        name = tk.Label(self.profil_frame, text="Name", bd=0, bg='white', fg='#6F6C6C', font=("Poppins", 14))
        username = tk.Label(self.profil_frame, text="xxx xxx", bd=0, bg='white', fg='black', font=("Poppins", 18))

        gruppen = tk.Label(self.profil_frame, text="Gruppen", bd=0, bg='white', fg='#6F6C6C', font=("Poppins", 14))
        usergruppen = tk.Label(self.profil_frame, text="xx, xx", bd=0, bg='white', fg='black', font=("Poppins", 18))

        email = tk.Label(self.profil_frame, text="Email", bd=0, bg='white', fg='#6F6C6C', font=("Poppins", 14))
        useremail = tk.Label(self.profil_frame, text="xxx@srhk.de", bd=0, bg='white', fg='black', font=("Poppins", 18))

        rechte = tk.Label(self.profil_frame, text="Rechte", bd=0, bg='white', fg='#6F6C6C', font=("Poppins", 14))
        rechte_frame = tk.Frame(self.profil_frame, bg='#D9D9D9')
        adminrechte = tk.Label(self.profil_frame, text="Admin", bd=0, bg='white', fg='black', font=("Poppins", 18))
        ausbilderrechte = tk.Label(self.profil_frame, text="Ausbilder", bd=0, bg='white', fg='#6F6C6C', font=("Poppins", 18))
        userrechte = tk.Label(self.profil_frame, text="Schüler", bd=0, bg='white', fg='#6F6C6C', font=("Poppins", 18))



        # Seitennavigations-Buttons für Benutzer, Admin, Statistiken und Einstellungen
        user_button = tk.Button(verzeichniss, text="User", bd=0, bg=ThemeManager.SRH_Grey, fg='black', font=("Inter", 20, 'bold'),
                                command=lambda: controller.show_frame(Profil))

        admin_button = tk.Button(verzeichniss, text="Administration", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                 font=("Inter", 20, 'bold'),
                                 command=lambda: controller.show_frame(Admin))

        stats_button = tk.Button(verzeichniss, text="Statistiken", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                 font=("Inter", 20, 'bold'),
                                 command=lambda: controller.show_frame(Stats))


        einstellungen_button = tk.Button(verzeichniss, text="Einstellungen", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                         font=("Inter", 20, 'bold'),
                                         command=lambda: controller.show_frame(configuration.Einstellungen))


        user_button.pack(pady=10, anchor='w')
        admin_button.pack(pady=10, anchor='w')
        stats_button.pack(pady=10, anchor='w')
        einstellungen_button.pack(pady=10, anchor='w')

        login.place(relx=0.95, rely=0.5, anchor="center")
        mainpage.place(relx=0.90, rely=0.5, anchor="center")

        profilbild.place(x=0, y=0)

        name.place(x=499, y=10)
        username.place(x=502, y=30)

        gruppen.place(x=499, y=80)
        usergruppen.place(x=502, y=105)

        email.place(x=0, y=500)
        useremail.place(x=3, y=520)

        rechte.place(x=0, y=570)
        rechte_frame.place(x=3, y=605, width=1, height=80)
        adminrechte.place(x=13, y=590)
        ausbilderrechte.place(x=13, y=630)
        userrechte.place(x=13, y=670)

        self.profil_frame.place(relx=0.21, rely=0.15, relwidth=1, relheight=0.85)


class Admin(tk.Frame):

    def __init__(self, parent, controller):
        root_path = os.path.dirname(os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir)))
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')

        # Header-Label für die Profilseite
        header = ttk.Label(self, text="Administration", anchor="center", style="Header.TLabel")
        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)

        # Seitennavigation und laden der Bilder
        verzeichniss = tk.Frame(self, bg=ThemeManager.SRH_Grey)
        self.admin_frame = tk.Frame(self, bg='white')

        self.imglogin = tk.PhotoImage(
            file=root_path+"/gui/assets/Closeicon.png")
        self.imgmainpage = tk.PhotoImage(
            file=root_path+"/gui/assets/backtosite_icon.png")
        self.imgSuche = gui_prototyp.load_image(root_path + "/gui/assets/Search.png")
        self.imgHinzufugen = gui_prototyp.load_image(root_path + "/gui/assets/Adding_Icon.png")

        # Positionierung und Seitennavigations-Buttons für Benutzer, Admin, Statistiken und Einstellungen, Login,
        # Hauptseite und Profilbild
        login = tk.Button(header, image=self.imglogin, bd=0, bg=ThemeManager.SRH_Orange,
                          command=lambda: controller.show_frame(gui_prototyp.LogInWindow))
        mainpage = tk.Button(header, image=self.imgmainpage, bd=0, bg=ThemeManager.SRH_Orange,
                             command=lambda: controller.show_frame(Mainpages.MainPage))

        login.place(relx=0.95, rely=0.5, anchor="center")
        mainpage.place(relx=0.90, rely=0.5, anchor="center")

        user_button = tk.Button(verzeichniss, text="User", bd=0, bg=ThemeManager.SRH_Grey, fg='black', font=("Inter", 20, 'bold'),
                                command=lambda: controller.show_frame(Profil))
        user_button.pack(pady=10, anchor='w')

        admin_button = tk.Button(verzeichniss, text="Administration", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                 font=("Inter", 20, 'bold'),
                                 command=lambda: controller.show_frame(Admin))
        admin_button.pack(pady=10, anchor='w')

        stats_button = tk.Button(verzeichniss, text="Statistiken", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                 font=("Inter", 20, 'bold'),
                                 command=lambda: controller.show_frame(Stats))
        stats_button.pack(pady=10, anchor='w')

        einstellungen_button = tk.Button(verzeichniss, text="Einstellungen", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                         font=("Inter", 20, 'bold'),
                                         command=lambda: controller.show_frame(configuration.Einstellungen))
        einstellungen_button.pack(pady=10, anchor='w')

        #Seiteninhalt
        self.tabelle_frame = tk.Frame(self, bg='white')
        # Suche
        suche_button = tk.Button(self.admin_frame, image=self.imgSuche, bd=0, bg=ThemeManager.SRH_Grey,
                                 command=lambda: print(f"nach {suche_entry} gesucht"))
        suche_entry = tk.Entry(self.admin_frame, bg='#D9D9D9', bd=0, font=("Inter", 12))

        suche_button.place(relx=0.19, rely=0.1, relheight=0.04, relwidth=0.02)
        suche_entry.place(relx=0.21, rely=0.1, width=500, height=37)

        # Hinzufügen
        Hinzufugen_button = tk.Button(self.admin_frame, image=self.imgHinzufugen, bd=0, bg='white',
                                      command=lambda: controller.show_frame(Profil))
        Hinzufugen_button.place(relx=0.5, rely=0.1)
        # Tabelle
        # Styling
        style = ttk.Style()
        # style.theme_use("clam")
        style.configure("Treeview.Heading", font=("Inter", 12), background="#D9D9D9", foreground="#6E6893")
        style.configure("Treeview", font=("Arial", 11), rowheight=35, background="white", foreground="black")
        style.map("Treeview", background=[("selected", "#D9D9D9")], foreground=[("selected", "black")])
        style.configure("evenrow.Treeview", background="#f2f2f2")
        style.configure("oddrow.Treeview", background="white")

        tree = ttk.Treeview(self.tabelle_frame, columns=("c1", "c2", "c3", "c4"), show="headings",
                            height=5)
        scroll = ttk.Scrollbar(self.tabelle_frame, orient='vertical', command=tree.yview)
        tree.configure(yscrollcommand=scroll.set)

        tree.column("#1", anchor='center', width=100)
        tree.heading("#1", text="Name")
        tree.column("#2", anchor='center', width=200)
        tree.heading("#2", text="Email")
        tree.column("#3", anchor='center', width=100)
        tree.heading("#3", text="Rolle")
        tree.column("#4", anchor='center', width=100)
        tree.heading("#4", text="Aktivität")


        for i in range(20):
            color = "#f3f3f3" if i % 2 == 0 else "white"
            tree.insert("", "end", values=(f"Name {i}", f"Email {i}", f"Rolle {i}", f"Aktivität {i}"),
                        tags=("even" if i % 2 == 0 else "odd"))

        # Farben für Tags definieren
        tree.tag_configure("even", background="#f7f7f7")
        tree.tag_configure("odd", background="white")

        tree.place(x=120, y=0, width=1280, height=650)
        scroll.place(x=1400, y=0, height=650)
        self.tabelle_frame.place(relx=0.15, rely=0.3, relwidth=0.85, height=800)
        self.admin_frame.place(relx=0.21, rely=0.15, relwidth=1, relheight=0.85)
        verzeichniss.place(relx=0, rely=0.15, relwidth=0.15, relheight=0.85)


class Stats(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        root_path = os.path.dirname(os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir)))
        self.configure(bg='white')

        # Header-Label für die Statistikseite
        header = ttk.Label(self, text="Statistiken", anchor="center", style="Header.TLabel")
        header.place(relx=0, rely=0, relwidth=1, relheight=0.15)

        # Navigationsleiste auf der linken Seite
        verzeichniss = tk.Frame(self, bg=ThemeManager.SRH_Grey)
        self.stats_frame = tk.Frame(self, bg='white')

        # Bilder für die Login- und Hauptseite-Buttons laden
        self.imglogin = tk.PhotoImage(
            file=root_path+"/gui/assets/Closeicon.png")
        self.imgmainpage = tk.PhotoImage(
            file=root_path+"/gui/assets/backtosite_icon.png")

        # Header-Navigationsbuttons (Login und Hauptseite), Platzierung der Header-Buttons
        login = tk.Button(header, image=self.imglogin, bd=0, bg=ThemeManager.SRH_Orange,
                          command=lambda: controller.show_frame(gui_prototyp.LogInWindow))
        mainpage = tk.Button(header, image=self.imgmainpage, bd=0, bg=ThemeManager.SRH_Orange,
                             command=lambda: controller.show_frame(Mainpages.MainPage))

        login.place(relx=0.95, rely=0.5, anchor="center")
        mainpage.place(relx=0.90, rely=0.5, anchor="center")

        # Linksseitige Navigationsbutton für verschiedene Ansichten
        user_button = tk.Button(verzeichniss, text="User", bd=0, bg=ThemeManager.SRH_Grey, fg='black', font=("Inter", 20, 'bold'),
                                command=lambda: controller.show_frame(Profil))
        user_button.pack(pady=10, anchor='w')

        admin_button = tk.Button(verzeichniss, text="Administration", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                 font=("Inter", 20, 'bold'),
                                 command=lambda: controller.show_frame(Admin))
        admin_button.pack(pady=10, anchor='w')

        stats_button = tk.Button(verzeichniss, text="Statistiken", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                 font=("Inter", 20, 'bold'),
                                 command=lambda: controller.show_frame(Stats))
        stats_button.pack(pady=10, anchor='w')

        einstellungen_button = tk.Button(verzeichniss, text="Einstellungen", bd=0, bg=ThemeManager.SRH_Grey, fg='black',
                                         font=("Inter", 20, 'bold'),
                                         command=lambda: controller.show_frame(configuration.Einstellungen))
        einstellungen_button.pack(pady=10, anchor='w')

        # Platzierung des Hauptinhaltsbereichs und der Navigationsleiste
        self.stats_frame.place(relx=0.21, rely=0.15, relwidth=1, relheight=0.85)
        verzeichniss.place(relx=0, rely=0.15, relwidth=0.15, relheight=0.85)
