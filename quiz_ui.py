import tkinter as tk

BG = "#ED7D31"
TEXT = "#111111"
BUTTON_TEXT = "#2d7496"


def build_name_screen(app):
    """
    Builds the name entry screen onto the app window.
    """
    app.clear_screen()

    tk.Label(
        app,
        text="VAS Knife Safety Waiver",
        bg=BG,
        fg=TEXT,
        font=("Arial", 36)
    ).pack(pady=10)

    tk.Label(
        app,
        text="Please enter your name in the box below",
        bg=BG,
        fg=TEXT,
        font=("Arial", 20)
    ).pack(pady=10)

    app.name_entry = tk.Entry(
        app,
        textvariable=app.name,
        font=("Arial", 20),
        fg=TEXT
    )
    app.name_entry.pack(pady=10)

    tk.Button(
        app,
        text="Submit",
        command=app.btn_press,
        font=("Arial", 20),
        fg=BUTTON_TEXT
    ).pack(pady=10)

    app.output_box = tk.Label(
        app,
        text="",
        bg=BG,
        font=("Arial", 20)
    )
    app.output_box.pack(pady=10)


def build_question_screen(app):
    """
    Builds the current question screen onto the app window.
    """
    app.clear_screen()

    tk.Label(
        app,
        text=f"Question {app.current_question + 1} of {len(app.questions)}",
        bg=BG,
        fg=TEXT,
        font=("Arial", 14)
    ).pack(pady=(40, 5))

    tk.Label(
        app,
        text=app.questions[app.current_question],
        bg=BG,
        fg=TEXT,
        font=("Arial", 20),
        wraplength=600,
        justify="center"
    ).pack(pady=(5, 40))

    button_frame = tk.Frame(app, bg=BG)
    button_frame.pack(pady=10)

    tk.Button(
        button_frame,
        text="Yes",
        font=("Arial", 20),
        fg=BUTTON_TEXT,
        width=8,
        command=app.handle_yes
    ).pack(side="left", padx=30)

    tk.Button(
        button_frame,
        text="No",
        font=("Arial", 20),
        fg=BUTTON_TEXT,
        width=8,
        command=app.handle_no
    ).pack(side="left", padx=30)


def build_thank_you_screen(app):
    """
    Builds the final confirmation screen onto the app window.
    """
    app.clear_screen()

    tk.Label(
        app,
        text="Thank you for your responses!",
        font=("Arial", 22),
        bg=BG
    ).pack(pady=60)

    tk.Label(
        app,
        text=f"{app.student_name}, your answers have been recorded.",
        font=("Arial", 20),
        wraplength=600,
        justify="center",
        bg=BG
    ).pack(pady=10)

    tk.Button(
        app,
        text="Close",
        font=("Arial", 20),
        fg=BUTTON_TEXT,
        command=app.destroy
    ).pack(pady=40)