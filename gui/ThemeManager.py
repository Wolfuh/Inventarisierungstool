import tkinter as tk
from tkinter import PhotoImage
import os
# SRH Farben (Corporate Design)
SRH_Orange = "#df4807"
SRH_Grey = "#d9d9d9"
SRH_Blau = "#10749c"
# Darkmode Farben
Darkmode_Black = "#121212"
Darkmode_Grey = "#2d2d2d"


class ThemeManager(tk.Frame):

    def __init__(self, master=None):
        """
    Initialisiert eine benutzerdefinierte Klasse mit einem Master-Widget und konfiguriert einen Schalter.

    Args:
        master (tk.Widget, optional): Das übergeordnete Widget, in dem diese Instanz eingebettet ist.
                                      Standardmäßig `None`, was bedeutet, dass kein Eltern-Widget festgelegt wurde.

    Attributes:
        master (tk.Widget): Das übergeordnete Widget, das von der Klasse referenziert wird.
        switch_value (bool): Der aktuelle Zustand des Schalters, initial auf `True` gesetzt.
        light (PhotoImage): Bild für den deaktivierten Schalter.
        dark (PhotoImage): Bild für den aktivierten Schalter.

    Raises:
        tk.TclError: Wenn die Bilddateien nicht geladen werden können.
    """
        root_path = os.path.dirname(os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir)))
        super().__init__(master)
        self.master = master
        self.switch_value = True  # Initialisiert den Switch-Wert
        try:
            self.light = PhotoImage(file=root_path+"/gui/assets/switchoff.png")
            self.dark = PhotoImage(file=root_path+"/gui/assets/switchon.png")
        except tk.TclError as e:
            print(f"Fehler beim Laden der Bilder: {e}")
            return  # Beende, falls die Bilder nicht geladen werden können

