# Texty is a text editor written in Python using the Tkinter. It is a simple
# text editor focused on simplicity and ease of use while being powerful and
# extensible. It is a work in progress and is not yet ready for use.

import logging
import sys
import tkinter as tk

import click

from config.defaults import DEFAULT_PREFS, KEYBINDS, MAC_KEYBINDS, PREFERENCES_FILE
from helpers.preferences import PreferenceManager

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class Texty(tk.Tk):
    def __init__(self, debug=False):
        super().__init__()
        self.title("Texty")
        self.debug = debug
        self.prefs = PreferenceManager(DEFAULT_PREFS, PREFERENCES_FILE)
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.system = self.call("tk", "windowingsystem")
        self.log("Running Texty on %s" % self.system)

        self.option_add("*tearOff", False)
        self.log("Tearoff disabled")

        # Bind Resize, Move, and Close
        self.bind("<Configure>", self.save_prefs)
        self.bind("<Destroy>", self.save_prefs)
        self.log("Resize, Move, and Close bindings set to save preferences.")

        # Set Geometry
        self.set_geometry()

        # Create Menu Bar
        self.bind_menu()

    def log(self, message):
        if self.debug:
            logging.info(message)

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
        self.log(
            "Window geometry set to {}x{}+{}+{}".format(width, height, x_pos, y_pos)
        )

    def save_prefs(self, event):
        if not self.debug:
            self.prefs.set("width", self.winfo_width())
            self.prefs.set("height", self.winfo_height())
            self.prefs.set("x_pos", self.winfo_x())
            self.prefs.set("y_pos", self.winfo_y())
            self.prefs.save()

    def bind_menu(self):
        menubar = tk.Menu(self)

        meta = "Command" if self.system == "aqua" else "Control"
        keybinds = {k: v.replace("meta", meta) for k, v in KEYBINDS.items()}
        mac_keybinds = {k: v.replace("meta", meta) for k, v in MAC_KEYBINDS.items()}
        self.log("Keybinds set to %s" % keybinds)

        if self.system == "aqua":
            self.log("MacOS detected, Additional Keybinds set to %s" % mac_keybinds)
            appmenu = tk.Menu(menubar, name="apple")
            menubar.add_cascade(menu=appmenu)
            appmenu.add_command(label="About Texty")
            appmenu.add_separator()
            self.createcommand("tk::mac::ShowPreferences", self.show_preferences)

        self.config(menu=menubar)

    def show_preferences(self):
        print("Show Preferences")

    def on_close(self):
        if self.system == "aqua":
            self.destroy()
        else:
            self.quit()


@click.command()
@click.option("--debug", is_flag=True, help="Enable debug mode.")
def main(debug):
    if debug:
        logging.info("Running in debug mode. Preferences will not be saved.")
    texty = Texty(debug=debug)
    texty.protocol("WM_DELETE_WINDOW", texty.on_close)
    texty.mainloop()


if __name__ == "__main__":
    main()
