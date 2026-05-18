import tkinter as tk # for creating the GUI
from tkinter import messagebox # to import the messagebox
import csv # to write to csv from main
from datetime import datetime # to record a timestamp
from quiz_validations import presence_check,length_check,character_check # importing validations

BG = "#ED7D31"
TEXT = "#111111"
BUTTON_TEXT = "#2d7496"

class KnifeSafety(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Knife Safety and PPE")
        self.configure(bg=BG)
        self.geometry("700x1000")
        self.name = tk.StringVar()
    
        self.name_label = tk.Label(
            self,
            text="Please enter your name in the box below",
            bg=BG,
            fg=TEXT,
            font=("Arial", 20)
        )
        self.name_label.pack(pady=10)

        self.name_entry = tk.Entry(
            self,
            textvariable = self.name,
            font = ("Arial", 20),
            fg=TEXT
        )
        self.name_entry.pack(pady=10)

        self.btn_submit = tk.Button(
            self,
            text = "Submit",
            command=self.btn_press,
            font = ("Arial", 20),
            fg=BUTTON_TEXT
        )
        self.btn_submit.pack(pady=10)

        self.output_box = tk.Label(self,
                                    text="",
                                    bg=BG,
                                    font=('Arial', 20))
        self.output_box.pack(pady=10)
        
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
        else: 
            '''
            Temporary output to test functionality, need to update with correct displays
            '''
            output = f"Hello, {name.title()}" 
            self.output_box.config(text=output)
            return("OK")

    def error_handler(self, error_message):
        try: 
            messagebox.showerror("Error", error_message)
        except Exception as e: 
            print(f"Something went wrong: {e}")
        
    def presence_check(self, name):
        return bool(name)
    
    def length_check(self, name):
        return 2<len(name)<=20
    
    def character_check(self, name): 
        return bool(re.fullmatch(r"[a-zA-Z-\s']+", name))


if __name__ == "__main__":
    app = KnifeSafety()
    app.mainloop()