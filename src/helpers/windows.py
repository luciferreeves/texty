import os
import tkinter as tk

from config.defaults import ICONS_FOLDER


class TextyWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.tabs = []
        geometry = self.parent.get_window_geometry()
        self.geometry(geometry)
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.option_add("*tearOff", False)
        self.parent.log("Tearoff disabled")

        # Bind Resize, Move, and Close
        self.bind("<Configure>", self.parent.save_prefs)
        self.bind("<Destroy>", self.parent.save_prefs)
        self.parent.log("Resize, Move, and Close bindings set to save preferences.")

        self.config(menu=self.parent.get_menubar())
        self.set_toolbar()

    def on_close(self):
        self.parent.destroy_window(self)

    def draw_layout(self):
        self.parent.log("Drawing layout")

    def set_toolbar(self):
        self.parent.log("Drawing Toolbar")

        toolbar = tk.Frame(self, bd=1, relief=tk.RAISED)

        # add icon 16x16 buttons
        def get_icon(name):
            return tk.PhotoImage(file=os.path.join(ICONS_FOLDER, name))

        new_icon = get_icon("new.png")
        save_icon = get_icon("save.png")
        cut_icon = get_icon("cut.png")
        copy_icon = get_icon("copy.png")
        paste_icon = get_icon("paste.png")
        print_icon = get_icon("print.png")
