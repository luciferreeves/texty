import tkinter as tk

from idlelib.tooltip import Hovertip
from tkmacosx import Button


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
        self.draw_layout()

    def on_close(self):
        self.parent.destroy_window(self)

    def draw_layout(self):
        self.parent.log("Drawing layout")
        self.set_toolbar()

        self.parent.log("Drawing Text Editor")
        self.text = tk.Text(
            self,
            undo=True,
            autoseparators=True,
            maxundo=-1,
            wrap=tk.WORD,
            font=("Menlo", 12),
            borderwidth=0,
            highlightthickness=0,
        )
        self.text.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.text.focus_set()

    def set_toolbar(self):
        self.parent.log("Drawing Toolbar")
        background_color = "#303030" if self.parent.theme == "dark" else "#f0f0f0"
        foreground_color = "#f0f0f0" if self.parent.theme == "dark" else "#303030"

        toolbar = tk.Frame(self, bd=1, relief=tk.RAISED, bg=background_color)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.parent.log("Drawing Action Buttons")
        self.draw_action_buttons(toolbar, background_color, foreground_color)

    def draw_action_buttons(self, toolbar, background_color, foreground_color):
        self.parent.log("Drawing New File Button")
        new_btn = Button(
            toolbar,
            image=tk.PhotoImage(file="icons/new.png").subsample(24, 24),
            bg=background_color,
            bd=0,
            borderless=True,
            relief="flat",
            overrelief="flat",
            focusthickness=0,
            bordercolor=background_color,
        )  # New File
        new_btn.pack(side=tk.LEFT, padx=2, pady=2)
        Hovertip(new_btn, "New File")

        self.parent.log("Drawing Open File Button")
        save_btn = Button(
            toolbar,
            image=tk.PhotoImage(file="icons/save.png").subsample(24, 24),
            bg=background_color,
            bd=0,
            borderless=True,
            relief="flat",
            overrelief="flat",
            focusthickness=0,
            bordercolor=background_color,
        )  # Save File
        save_btn.pack(side=tk.LEFT, padx=2, pady=2)
        Hovertip(save_btn, "Save File")

        self.parent.log("Drawing Spacer")
        spacer = tk.Frame(toolbar, width=30, height=30, bg=background_color)
        spacer.pack(side=tk.LEFT, padx=2, pady=2)

        self.parent.log("Drawing Cut Button")
        cut_btn = Button(
            toolbar,
            image=tk.PhotoImage(file="icons/cut.png").subsample(24, 24),
            bg=background_color,
            bd=0,
            borderless=True,
            relief="flat",
            overrelief="flat",
            focusthickness=0,
            bordercolor=background_color,
        )  # Cut
        cut_btn.pack(side=tk.LEFT, padx=2, pady=2)
        Hovertip(cut_btn, "Cut")

        self.parent.log("Drawing Copy Button")
        copy_btn = Button(
            toolbar,
            image=tk.PhotoImage(file="icons/copy.png").subsample(24, 24),
            bg=background_color,
            bd=0,
            borderless=True,
            relief="flat",
            overrelief="flat",
            focusthickness=0,
            bordercolor=background_color,
        )  # Copy
        copy_btn.pack(side=tk.LEFT, padx=2, pady=2)
        Hovertip(copy_btn, "Copy")

        self.parent.log("Drawing Paste Button")
        paste_btn = Button(
            toolbar,
            image=tk.PhotoImage(file="icons/paste.png").subsample(24, 24),
            bg=background_color,
            bd=0,
            borderless=True,
            relief="flat",
            overrelief="flat",
            focusthickness=0,
            bordercolor=background_color,
        )  # Paste
        paste_btn.pack(side=tk.LEFT, padx=2, pady=2)
        Hovertip(paste_btn, "Paste")

        self.parent.log("Drawing Spacer")
        spacer = tk.Frame(toolbar, width=30, height=30, bg=background_color)
        spacer.pack(side=tk.LEFT, padx=2, pady=2)

        self.parent.log("Drawing Print Button")
        print_btn = Button(
            toolbar,
            image=tk.PhotoImage(file="icons/print.png").subsample(24, 24),
            bg=background_color,
            bd=0,
            borderless=True,
            relief="flat",
            overrelief="flat",
            focusthickness=0,
            bordercolor=background_color,
        )  # Print
        print_btn.pack(side=tk.LEFT, padx=2, pady=2)
        Hovertip(print_btn, "Print")
