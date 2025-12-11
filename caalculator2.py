import tkinter as tk
from tkinter import messagebox

class StylishCalculatorApp:
    """
    A stylish and responsive calculator application using tkinter.
    Features modern color combinations and click effects.
    """
    def __init__(self, master):
        self.master = master
        master.title("Styled Calculator")
        master.resizable(False, False)

        # --- Enhanced Color Palette ---
        self.main_bg = "#2f3640"      # Dark background (e.g., Deep Slate)
        self.display_bg = "#1e272e"   # Even darker display background
        
        # Primary Buttons (Numbers)
        self.num_btn_bg = "#535c68"   # Neutral button color
        self.num_btn_active = "#47525e" # Darker on click
        
        # Operator Buttons (+, -, *, /)
        self.op_btn_bg = "#e84118"    # Bright Orange/Red
        self.op_btn_active = "#c23616" # Darker Orange/Red on click
        
        # Action Buttons (C, =)
        self.clear_bg = "#3498db"     # Blue for Clear
        self.clear_active = "#2980b9" # Darker Blue on click
        self.eq_bg = "#27ae60"        # Green for Equals
        self.eq_active = "#2ecc71"    # Lighter Green on click

        self.text_color = "#f5f6fa"   # Off-white text

        master.configure(bg=self.main_bg)

        # --- Expression Storage ---
        self.current_expression = ""

        # --- Display Screen ---
        self.display_frame = tk.Frame(master, bg=self.display_bg)
        self.display_frame.pack(expand=True, fill='both', padx=5, pady=5)

        self.display = tk.Entry(
            self.display_frame,
            textvariable=tk.StringVar(value=""),
            font=('Segoe UI', 30, 'bold'),
            bd=0,
            relief=tk.FLAT,
            justify='right',
            bg=self.display_bg,
            fg=self.text_color,
            insertbackground=self.text_color,
            readonlybackground=self.display_bg,
            # Padding within the display entry
            width=15
        )
        self.display.config(state=tk.DISABLED)
        self.display.pack(expand=True, fill='both', padx=10, pady=10)

        # --- Buttons Frame ---
        self.buttons_frame = tk.Frame(master, bg=self.main_bg)
        self.buttons_frame.pack()

        # Define the button layout (text, row, col, style_type)
        buttons_config = [
            ('C', 1, 0, 'clear'), ('/', 1, 1, 'op'), ('*', 1, 2, 'op'), ('←', 1, 3, 'op'),
            ('7', 2, 0, 'num'), ('8', 2, 1, 'num'), ('9', 2, 2, 'num'), ('-', 2, 3, 'op'),
            ('4', 3, 0, 'num'), ('5', 3, 1, 'num'), ('6', 3, 2, 'num'), ('+', 3, 3, 'op'),
            ('1', 4, 0, 'num'), ('2', 4, 1, 'num'), ('3', 4, 2, 'num'),
            ('0', 5, 0, 'num', 2), ('.', 5, 2, 'num')
        ]
        
        for (text, row, col, style_type, *span) in buttons_config:
            columnspan = span[0] if span else 1
            self.create_button(text, row, col, style_type, columnspan=columnspan)
        
        # Equals button (takes up 2 rows)
        self.create_button('=', 4, 3, 'eq', rowspan=2)


    def get_style_colors(self, style_type):
        """Returns the background and active background colors based on style type."""
        if style_type == 'clear':
            return self.clear_bg, self.clear_active
        elif style_type == 'op':
            return self.op_btn_bg, self.op_btn_active
        elif style_type == 'eq':
            return self.eq_bg, self.eq_active
        else: # 'num'
            return self.num_btn_bg, self.num_btn_active

    def create_button(self, text, row, col, style_type, columnspan=1, rowspan=1):
        """Creates and places a stylized button."""
        
        bg_color, active_color = self.get_style_colors(style_type)
        
        # Set command based on button text
        if text == '=':
            command = self.calculate
        elif text == 'C':
            command = self.clear_input
        elif text == '←':
            command = self.backspace
        else:
            command = lambda t=text: self.append_to_expression(t)

        button = tk.Button(
            self.buttons_frame,
            text=text,
            fg=self.text_color,
            bg=bg_color,
            font=('Segoe UI', 16, 'bold'),
            bd=0,
            relief=tk.FLAT, # Flat look
            highlightthickness=0, # Remove border highlighting
            padx=20,
            pady=20,
            command=command,
            # The click/hover effect: activebackground changes when clicked
            activebackground=active_color,
            activeforeground=self.text_color 
        )
        
        # Grid placement
        button.grid(row=row, column=col, columnspan=columnspan, rowspan=rowspan, sticky='nsew', padx=4, pady=4)
        
        # Ensure rows and columns expand to fill the available space
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
            # Use expression evaluation (eval)
            result = str(eval(self.current_expression))
            
            # Display result
            self.current_expression = result
            self.update_display()
            
        except (ZeroDivisionError, SyntaxError, NameError):
            # Handle all calculation errors
            self.current_expression = "Error"
            self.update_display()
            
            # Clear the error after 1.5 seconds for user to see
            self.master.after(1500, self.clear_input) 
        
# --- Main Execution Block ---
if __name__ == '__main__':
    root = tk.Tk()
    calculator = StylishCalculatorApp(root)
    root.mainloop()