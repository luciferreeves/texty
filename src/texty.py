# Texty is a text editor written in Python using the Tkinter. It is a simple
# text editor focused on simplicity and ease of use while being powerful and
# extensible. It is a work in progress and is not yet ready for use.

import logging
import sys
import tkinter as tk

import click

from config.defaults import DEFAULT_PREFS, PREFERENCES_FILE
from helpers.preferences import PreferenceManager

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class Texty(tk.Tk):
    def __init__(self, debug=False):
        super().__init__()
        self.title("Texty")
        self.debug = debug
        self.prefs = PreferenceManager(DEFAULT_PREFS, PREFERENCES_FILE)

        if self.debug:
            logging.info("Running in debug mode. Preferences will not be saved.")
            self.prefs.reset()
        self.set_geometry()
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.system = self.call("tk", "windowingsystem")
        if self.system == "aqua":
            self.option_add("*tearOff", False)

        # Bind Resize, Move, and Close
        self.bind("<Configure>", self.save_prefs)
        self.bind("<Destroy>", self.save_prefs)

        # Create Menu Bar
        self.bind_menu()

    def set_geometry(self):
        width = self.prefs.get("width")
        height = self.prefs.get("height")
        x_pos = (
            (self.winfo_screenwidth() // 2) - (width // 2)
            if self.prefs.get("x_pos") == "center"
            else self.prefs.get("x_pos")
        )
        y_pos = (
            (self.winfo_screenheight() // 2) - (height // 2)
            if self.prefs.get("y_pos") == "center"
            else self.prefs.get("y_pos")
        )
        self.geometry(f"{width}x{height}+{x_pos}+{y_pos}")

    def save_prefs(self, event):
        if not self.debug:
            self.prefs.set("width", self.winfo_width())
            self.prefs.set("height", self.winfo_height())
            self.prefs.set("x_pos", self.winfo_x())
            self.prefs.set("y_pos", self.winfo_y())
            self.prefs.save()

    def bind_menu(self):
        pass

    def on_close(self):
        if self.system == "aqua":
            self.destroy()
        else:
            self.quit()


@click.command()
@click.option("--debug", is_flag=True, help="Enable debug mode.")
def main(debug):
    texty = Texty(debug=debug)
    texty.protocol("WM_DELETE_WINDOW", texty.on_close)
    texty.mainloop()


if __name__ == "__main__":
    main()
