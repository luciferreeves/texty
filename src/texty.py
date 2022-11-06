# Texty is a text editor written in Python using the Tkinter. It is a simple
# text editor focused on simplicity and ease of use while being powerful and
# extensible. It is a work in progress and is not yet ready for use.

import logging
import sys
import tkinter as tk

import click
import darkdetect

from config.defaults import DEFAULT_PREFS, KEYBINDS, MAC_KEYBINDS, PREFERENCES_FILE
from helpers.managers import FileManager, PreferenceManager
from helpers.windows import TextyWindow


class Texty(tk.Tk):
    def __init__(self, debug=False):
        super().__init__()
        self.title("Texty")
        self.debug = debug
        self.prefs = PreferenceManager(DEFAULT_PREFS, PREFERENCES_FILE, debug=debug)
        self.fm = FileManager()
        self.system = self.call("tk", "windowingsystem")
        self.log(
            "Running Texty on system: {}, platform: {}".format(
                self.system, sys.platform
            )
        )
        if self.prefs.get("theme") == "system":
            self.theme = "dark" if darkdetect.isDark() else "light"
        else:
            self.theme = self.prefs.get("theme")
        self.windows = 0
        self.withdraw()
        self.create_window()

    def create_window(self):
        self.windows += 1
        window = TextyWindow(self)
        window.grab_set()
        window.focus_set()
        window.mainloop()

    def destroy_window(self, window):
        self.windows -= 1
        window.destroy()
        if self.windows == 0:
            self.destroy()

    def get_window_geometry(self):
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
        self.log(
            "Window geometry set to {}x{}+{}+{}".format(width, height, x_pos, y_pos)
        )
        return f"{width}x{height}+{x_pos}+{y_pos}"

    def get_menubar(self):
        menubar = tk.Menu(self)

        # Setting Keybinds
        meta = "Command" if self.system == "aqua" else "Control"
        keybinds = {k: v.replace("meta", meta) for k, v in KEYBINDS.items()}
        mac_keybinds = {k: v.replace("meta", meta) for k, v in MAC_KEYBINDS.items()}
        self.log("Keybinds set to %s" % keybinds)

        # macOS specific menu items
        if self.system == "aqua":
            self.log("MacOS detected, Additional Keybinds set to %s" % mac_keybinds)
            appmenu = tk.Menu(menubar, name="apple")
            menubar.add_cascade(menu=appmenu)
            appmenu.add_command(label="About Texty")
            appmenu.add_separator()
            self.createcommand("tk::mac::ShowPreferences", self.show_preferences)
            appmenu.add_separator()

        # File Menu
        filemenu = tk.Menu(menubar)
        menubar.add_cascade(menu=filemenu, label="File")
        filemenu.add_command(
            label="New Text File", accelerator=keybinds["New Text File"]
        )
        filemenu.add_command(label="New Window", accelerator=keybinds["New Window"])
        # filemenu.add_command(label="New Tab", accelerator=keybinds["New Tab"])
        filemenu.add_separator()
        filemenu.add_command(label="Open File", accelerator=keybinds["Open File"])
        filemenu.add_command(label="Save", accelerator=keybinds["Save"])
        filemenu.add_command(label="Save As", accelerator=keybinds["Save As"])
        filemenu.add_separator()
        # filemenu.add_command(label="Close Tab", accelerator=keybinds["Close Tab"])
        if self.system == "aqua":
            filemenu.add_command(
                label="Close Window", accelerator=mac_keybinds["Close Window"]
            )
        else:
            filemenu.add_command(label="Quit", accelerator=keybinds["Close"])

        # Configure Menubar for the current window
        return menubar

    # Event Logger
    def log(self, message):
        if self.debug:
            logging.info(message)

    # Save Preferences
    def save_prefs(self, event):
        if not self.debug:
            self.prefs.set("width", self.winfo_width())
            self.prefs.set("height", self.winfo_height())
            self.prefs.set("x_pos", self.winfo_x())
            self.prefs.set("y_pos", self.winfo_y())
            self.prefs.save()

    def show_preferences(self):
        print("Show Preferences")


@click.command()
@click.option("--debug", is_flag=True, help="Enable debug mode.")
def runtexty(debug):
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    if debug:
        logging.info("Running in debug mode. Preferences will not be saved.")
    Texty(debug=debug)


if __name__ == "__main__":
    runtexty()
