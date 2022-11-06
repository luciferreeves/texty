import tkinter as tk


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

    def on_close(self):
        if self.parent.system == "aqua":
            self.destroy()
        else:
            self.quit()
