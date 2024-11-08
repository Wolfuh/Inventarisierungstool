import tkinter as tk
from tkinter import PhotoImage
import gui_prototyp
import Profiles
import Einstellungen
# SRH Farben (Corporate Design)
SRH_Orange = "#df4807"
SRH_Grey = "#d9d9d9"
SRH_Blau = "#10749c"
# Darkmode Farben
Darkmode_Black = "#121212"
Darkmode_Grey = "#2d2d2d"


class ThemeManager(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.switch_value = True  # Initialisiert den Switch-Wert
        try:
            self.light = PhotoImage(file="gui/assets/switchoff.png")
            self.dark = PhotoImage(file="gui/assets/switchon.png")
        except tk.TclError as e:
            print(f"Fehler beim Laden der Bilder: {e}")
            return  # Beende, falls die Bilder nicht geladen werden können

