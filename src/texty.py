# Texty is a text editor written in Python using the Tkinter. It is a simple
# text editor focused on simplicity and ease of use while being powerful and
# extensible. It is a work in progress and is not yet ready for use.

import json
import os
import tkinter as tk

PREFERENCES_FILE = "texty.prefs"
DEFAULT_PREFS = {
    "width": 800,
    "height": 600,
    "x_pos": 0,
    "y_pos": 0,
}


class Texty(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Texty")
        self.load_prefs()
        self.geometry("{}x{}".format(self.prefs["width"], self.prefs["height"]))
        self.minsize(400, 300)

        # set position
        if self.prefs["x_pos"] > 0 and self.prefs["y_pos"] > 0:
            self.geometry("+{}+{}".format(self.prefs["x_pos"], self.prefs["y_pos"]))
        else:
            self.geometry(
                "+{}+{}".format(
                    self.winfo_screenwidth() // 2 - self.prefs["width"] // 2,
                    self.winfo_screenheight() // 2 - self.prefs["height"] // 2,
                )
            )

        self.draw_window()

    def load_prefs(self):
        self.prefs = DEFAULT_PREFS
        if os.path.exists(PREFERENCES_FILE):
            with open(PREFERENCES_FILE) as f:
                self.prefs = json.load(f)
        else:
            with open(PREFERENCES_FILE, "w") as f:
                json.dump(DEFAULT_PREFS, f)

    def save_prefs(self):
        with open(PREFERENCES_FILE, "w") as f:
            json.dump(self.prefs, f)

    def draw_window(self):
        self.text = tk.Text(self)
        self.text.pack(fill="both", expand=True)

    def on_close(self):
        self.prefs["width"] = self.winfo_width()
        self.prefs["height"] = self.winfo_height()
        self.prefs["x_pos"] = self.winfo_x()
        self.prefs["y_pos"] = self.winfo_y()
        self.save_prefs()
        self.destroy()


if __name__ == "__main__":
    app = Texty()
    app.protocol("WM_DELETE_WINDOW", app.on_close)
    app.mainloop()
