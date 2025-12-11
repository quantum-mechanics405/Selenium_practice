import tkinter as tk
from tkinter import messagebox

class ReflectiveCalculatorApp:
    """
    An advanced calculator with a resizable window, 3D buttons, 
    and true hover effects using tkinter event binding.
    """
    def __init__(self, master):
        self.master = master
        master.title("3D Reflective Calculator")
        
        # --- 1. Enable Resizable Window ---
        master.resizable(True, True) 
        
        # --- Enhanced Color Palette ---
        self.main_bg = "#f0f0f0"      # Light Gray Background
        self.display_bg = "#ffffff"   # White Display
        
        # Button Colors
        self.num_btn_base = "#e0e0e0" # Light base for numbers
        self.num_btn_hover = "#d0d0d0" # Slightly darker on hover
        self.num_btn_active = "#c0c0c0" # Darkest on click
        
        # Operator Colors
        self.op_btn_base = "#ff9800"  # Amber/Orange base
        self.op_btn_hover = "#fb8c00" # Slightly darker orange on hover
        self.op_btn_active = "#f57c00" # Darkest orange on click
        
        # Action Colors (C, =)
        self.clear_base = "#03a9f4"   # Light Blue for Clear
        self.eq_base = "#4caf50"      # Green for Equals
        self.clear_hover = "#039be5" 
        self.eq_hover = "#43a047"
        self.clear_active = "#0288d1"
        self.eq_active = "#388e3c"

        self.text_color = "#333333"   # Dark text for contrast

        master.configure(bg=self.main_bg)
        
        # --- Configure Grid for Resizing ---
        # Allow the main frame to expand
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_rowconfigure(0, weight=1)

        # --- Expression Storage ---
        self.current_expression = ""

        # --- Display Screen ---
        # Wrapped in a frame for better control over padding/border
        self.display_frame = tk.Frame(master, bg=self.display_bg, padx=5, pady=5)
        self.display_frame.grid(row=0, column=0, sticky='nsew')
        
        self.display = tk.Entry(
            self.display_frame,
            textvariable=tk.StringVar(value=""),
            font=('Roboto', 36, 'bold'),
            bd=5, # Border thickness for 3D look
            relief=tk.SUNKEN, # Gives the display a sunken, inset look
            justify='right',
            bg=self.display_bg,
            fg=self.text_color,
            readonlybackground=self.display_bg
        )
        self.display.config(state=tk.DISABLED)
        # Display always fills its container
        self.display.pack(expand=True, fill='both')

        # --- Buttons Frame ---
        self.buttons_frame = tk.Frame(master, bg=self.main_bg, padx=2, pady=2)
        self.buttons_frame.grid(row=1, column=0, sticky='nsew')
        
        # Allow the button frame rows/columns to expand
        for i in range(4): # 4 columns
            self.buttons_frame.grid_columnconfigure(i, weight=1)
        for i in range(5): # 5 rows
            self.buttons_frame.grid_rowconfigure(i, weight=1)

        # Define the button layout (text, row, col, style_type)
        buttons_config = [
            ('C', 0, 0, 'clear'), ('/', 0, 1, 'op'), ('*', 0, 2, 'op'), ('←', 0, 3, 'op'),
            ('7', 1, 0, 'num'), ('8', 1, 1, 'num'), ('9', 1, 2, 'num'), ('-', 1, 3, 'op'),
            ('4', 2, 0, 'num'), ('5', 2, 1, 'num'), ('6', 2, 2, 'num'), ('+', 2, 3, 'op'),
            ('1', 3, 0, 'num'), ('2', 3, 1, 'num'), ('3', 3, 2, 'num'),
            ('0', 4, 0, 'num', 2), ('.', 4, 2, 'num')
        ]
        
        for (text, row, col, style_type, *span) in buttons_config:
            columnspan = span[0] if span else 1
            self.create_button(text, row, col, style_type, columnspan=columnspan)
        
        # Equals button (takes up 2 rows)
        self.create_button('=', 3, 3, 'eq', rowspan=2)


    def get_style_colors(self, style_type):
        """Returns the base, hover, and active colors based on style type."""
        if style_type == 'clear':
            return self.clear_base, self.clear_hover, self.clear_active
        elif style_type == 'op':
            return self.op_btn_base, self.op_btn_hover, self.op_btn_active
        elif style_type == 'eq':
            return self.eq_base, self.eq_hover, self.eq_active
        else: # 'num'
            return self.num_btn_base, self.num_btn_hover, self.num_btn_active

    def create_button(self, text, row, col, style_type, columnspan=1, rowspan=1):
        """Creates and places a stylized button with event binding."""
        
        base_color, hover_color, active_color = self.get_style_colors(style_type)
        
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
            fg=self.text_color if style_type == 'num' else "white", # White text on colored buttons
            bg=base_color,
            font=('Roboto', 18, 'bold'),
            bd=3, # Border width for 3D effect
            relief=tk.RAISED, # Gives a lifted, reflective look
            highlightthickness=0,
            command=command,
            # activebackground handles the *click* state
            activebackground=active_color,
            activeforeground=self.text_color if style_type == 'num' else "white"
        )
        
        # --- 3. Implement True Hover Effect using Binding ---
        # When mouse enters the button area
        button.bind("<Enter>", lambda e: self.on_enter(e, hover_color, tk.RIDGE))
        # When mouse leaves the button area
        button.bind("<Leave>", lambda e: self.on_leave(e, base_color, tk.RAISED))
        
        # Grid placement
        button.grid(row=row, column=col, columnspan=columnspan, rowspan=rowspan, sticky='nsew', padx=3, pady=3)

    def on_enter(self, event, hover_color, hover_relief):
        """Changes button appearance on mouse hover (Enter event)."""
        event.widget.config(bg=hover_color, relief=hover_relief)

    def on_leave(self, event, base_color, base_relief):
        """Restores button appearance when mouse leaves (Leave event)."""
        event.widget.config(bg=base_color, relief=base_relief)

    # --- Calculation and Display Logic (Same as before) ---
    def update_display(self):
        self.display.config(state=tk.NORMAL)
        self.display.delete(0, tk.END)
        self.display.insert(0, self.current_expression)
        self.display.config(state=tk.DISABLED)

    def append_to_expression(self, value):
        self.current_expression += str(value)
        self.update_display()

    def clear_input(self):
        self.current_expression = ""
        self.update_display()

    def backspace(self):
        self.current_expression = self.current_expression[:-1]
        self.update_display()

    def calculate(self):
        try:
            result = str(eval(self.current_expression))
            self.current_expression = result
            self.update_display()
        except (ZeroDivisionError, SyntaxError, NameError):
            self.current_expression = "Error"
            self.update_display()
            self.master.after(1500, self.clear_input) 
        
# --- Main Execution Block ---
if __name__ == '__main__':
    root = tk.Tk()
    calculator = ReflectiveCalculatorApp(root)
    root.mainloop()