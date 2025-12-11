import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    """
    A simple, stylish calculator application using tkinter.
    """
    def __init__(self, master):
        self.master = master
        master.title("Stylish Calculator")
        master.resizable(False, False) # Prevents resizing the window

        # --- Configuration for Styling ---
        self.bg_color = "#2c3e50"     # Dark background (e.g., Anthracite)
        self.btn_color = "#34495e"    # Darker button color
        self.op_color = "#e67e22"     # Orange for operators
        self.eq_color = "#27ae60"     # Green for the equals button
        self.text_color = "#ecf0f1"   # Light text color

        master.configure(bg=self.bg_color)

        # --- Expression Storage ---
        self.current_expression = ""

        # --- Display Screen ---
        # The display frame and settings
        self.display_frame = tk.Frame(master, bg=self.bg_color)
        self.display_frame.pack(expand=True, fill='both')

        # The display widget (Entry)
        self.display = tk.Entry(
            self.display_frame,
            textvariable=tk.StringVar(value=""),
            font=('Arial', 24, 'bold'),
            bd=0, # Border width
            relief=tk.FLAT,
            justify='right',
            bg=self.bg_color,
            fg=self.text_color,
            insertbackground=self.text_color, # Cursor color
            readonlybackground=self.bg_color # In case it is set to readonly
        )
        # We need to set it to read-only so the user can't type
        self.display.config(state=tk.DISABLED)
        self.display.pack(expand=True, fill='both', padx=10, pady=10)


        # --- Buttons Frame ---
        self.buttons_frame = tk.Frame(master, bg=self.bg_color)
        self.buttons_frame.pack()

        # Define the layout of buttons
        # (text, row, col, style_type)
        buttons = [
            ('C', 1, 0, 'op'), ('/', 1, 1, 'op'), ('*', 1, 2, 'op'), ('-', 1, 3, 'op'),
            ('7', 2, 0, 'num'), ('8', 2, 1, 'num'), ('9', 2, 2, 'num'), ('+', 2, 3, 'op'),
            ('4', 3, 0, 'num'), ('5', 3, 1, 'num'), ('6', 3, 2, 'num'),
            ('1', 4, 0, 'num'), ('2', 4, 1, 'num'), ('3', 4, 2, 'num'),
            ('0', 5, 0, 'num'), ('.', 5, 1, 'num')
        ]
        
        # Create and place buttons
        for (text, row, col, style_type) in buttons:
            if style_type == 'op' or text == 'C':
                color = self.op_color
            else:
                color = self.btn_color
                
            self.create_button(text, row, col, color)
        
        # Special buttons (occupy more space)
        # Equals button
        self.create_button('=', 3, 3, self.eq_color, rowspan=3)
        # Backspace button
        self.create_button('←', 5, 2, self.op_color, columnspan=1)
        
    def create_button(self, text, row, col, color, columnspan=1, rowspan=1):
        """Creates and places a button with common styling and command."""
        
        # Set button command based on its text
        if text == '=':
            command = self.calculate
        elif text == 'C':
            command = self.clear_input
        elif text == '←':
            command = self.backspace
        else:
            # All numbers and operators call append_to_expression
            command = lambda t=text: self.append_to_expression(t)

        button = tk.Button(
            self.buttons_frame,
            text=text,
            fg=self.text_color,
            bg=color,
            font=('Arial', 18),
            bd=0, # Border width
            highlightthickness=0,
            padx=20,
            pady=20,
            command=command,
            activebackground=color,
            activeforeground=self.text_color
        )
        button.grid(row=row, column=col, columnspan=columnspan, rowspan=rowspan, sticky='nsew', padx=5, pady=5)
        # Make buttons expand equally
        self.buttons_frame.grid_columnconfigure(col, weight=1)
        self.buttons_frame.grid_rowconfigure(row, weight=1)

    def update_display(self):
        """Updates the display Entry widget with the current expression."""
        self.display.config(state=tk.NORMAL)
        self.display.delete(0, tk.END)
        self.display.insert(0, self.current_expression)
        self.display.config(state=tk.DISABLED)

    def append_to_expression(self, value):
        """Adds a number or operator to the expression."""
        self.current_expression += str(value)
        self.update_display()

    def clear_input(self):
        """Clears the current expression."""
        self.current_expression = ""
        self.update_display()

    def backspace(self):
        """Removes the last character from the expression."""
        self.current_expression = self.current_expression[:-1]
        self.update_display()

    def calculate(self):
        """Evaluates the current expression and updates the display."""
        try:
            # Security Note: Using eval() is acceptable for a simple calculator
            # where input is strictly controlled by buttons.
            result = str(eval(self.current_expression))
            
            # Display the result and prepare for the next operation
            self.current_expression = result
            self.update_display()
            
        except ZeroDivisionError:
            self.current_expression = "Error: Div by Zero"
            self.update_display()
            # Clear the error after a brief moment
            self.master.after(1500, self.clear_input) 
            
        except SyntaxError:
            self.current_expression = "Error"
            self.update_display()
            self.master.after(1500, self.clear_input)
        
# --- Main Execution Block ---
if __name__ == '__main__':
    root = tk.Tk()
    # The calculator object starts the GUI
    calculator = CalculatorApp(root)
    # Start the tkinter event loop
    root.mainloop()