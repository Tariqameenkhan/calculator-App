# A modern calculator application built with Python and tkinter.
import tkinter as tk
from tkinter import ttk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        
        # Configure style
        style = ttk.Style()
        style.configure("TButton", padding=5, font=('Arial', 12))
        
        # Result variable
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        
        # Expression variable
        self.expression = ""
        
        # Create display
        self.create_display()
        
        # Create buttons
        self.create_buttons()
    
    def create_display(self):
        display_frame = ttk.Frame(self.root)
        display_frame.pack(fill=tk.BOTH, padx=5, pady=5)
        
        result_label = ttk.Label(
            display_frame,
            textvariable=self.result_var,
            font=('Arial', 24),
            anchor='e'
        )
        result_label.pack(fill=tk.BOTH, padx=5, pady=5)
    
    def create_buttons(self):
        button_frame = ttk.Frame(self.root)
        button_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 0, 0), ('±', 0, 1), ('%', 0, 2), ('←', 0, 3)
        ]
        
        for (text, row, col) in buttons:
            button = ttk.Button(
                button_frame,
                text=text,
                command=lambda t=text: self.button_click(t)
            )
            button.grid(row=row, column=col, padx=2, pady=2, sticky='nsew')
        
        # Configure grid weights
        for i in range(5):
            button_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)
    
    def button_click(self, button_text):
        if button_text == 'C':
            self.expression = ""
            self.result_var.set("0")
        elif button_text == '←':
            self.expression = self.expression[:-1]
            self.result_var.set(self.expression if self.expression else "0")
        elif button_text == '=':
            try:
                result = str(eval(self.expression))
                self.result_var.set(result)
                self.expression = result
            except:
                self.result_var.set("Error")
                self.expression = ""
        elif button_text == '±':
            if self.expression and self.expression[0] == '-':
                self.expression = self.expression[1:]
            else:
                self.expression = '-' + self.expression
            self.result_var.set(self.expression)
        elif button_text == '%':
            try:
                result = str(eval(self.expression) / 100)
                self.result_var.set(result)
                self.expression = result
            except:
                self.result_var.set("Error")
                self.expression = ""
        else:
            self.expression += button_text
            self.result_var.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
