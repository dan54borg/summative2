import tkinter as tk
from tkinter import messagebox
from question_data import load_questions, save_response
from quiz_validations import presence_check, length_check, character_check
from quiz_ui import build_name_screen, build_question_screen, build_thank_you_screen

BG = "#ED7D31"
BUTTON_TEXT = "#2d7496"


class KnifeSafety(tk.Tk):

    """
    The class that represents the quiz app
    """

    def __init__(self):
        super().__init__()
        self.title("Knife Safety and PPE")
        self.configure(bg=BG)
        self.geometry("800x450")
        self.name = tk.StringVar()
        self.questions = load_questions()
        self.current_question = 0
        self.student_name = ""

        build_name_screen(self)

    """
    Builds the name entry screen
    """

    def btn_press(self):
        my_name = self.name_entry.get().strip()
        self.display_output(my_name)

    def display_output(self, name):
        if not presence_check(name):
            self.error_handler("Name cannot be left blank")
            return
        if not length_check(name):
            self.error_handler("The name should be between 2 and 19 characters")
            return
        if not character_check(name):
            self.error_handler("The name should not have any numbers")
            return

        self.student_name = name.title()
        self.current_question = 0
        build_question_screen(self)

    """
    Builds the question screen
    """

    def handle_yes(self):
        """
        Move to the next question, or finish if all answered Yes.
        """
        self.current_question += 1
        if self.current_question >= len(self.questions):
            save_response(self.student_name, stopped_at=None)
            build_thank_you_screen(self)
        else:
            build_question_screen(self)

    def handle_no(self):
        """
        Submit immediately when the user answers No.
        """
        save_response(self.student_name, stopped_at=self.current_question)
        build_thank_you_screen(self)

    def error_handler(self, error_message):
        try:
            messagebox.showerror("Error", error_message)
        except Exception as e:
            print(f"Something went wrong: {e}")

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    app = KnifeSafety()
    app.mainloop()