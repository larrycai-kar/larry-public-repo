import tkinter as tk
from tkinter import ttk

class TemperatureConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Temperature Converter")
        self.root.geometry("300x150")
        
        # Create main frame
        self.frame = ttk.Frame(root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Input field
        self.temperature = tk.StringVar()
        self.temp_entry = ttk.Entry(self.frame, width=15, textvariable=self.temperature)
        self.temp_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Dropdown for temperature unit selection
        self.from_unit = tk.StringVar()
        self.unit_combo = ttk.Combobox(self.frame, textvariable=self.from_unit, width=12)
        self.unit_combo['values'] = ('Fahrenheit', 'Celsius')
        self.unit_combo.set('Fahrenheit')
        self.unit_combo.grid(row=0, column=2, padx=5, pady=5)
        
        # Convert button
        self.convert_button = ttk.Button(self.frame, text="Convert", command=self.convert)
        self.convert_button.grid(row=1, column=1, columnspan=2, pady=10)
        
        # Result label
        self.result_var = tk.StringVar()
        self.result_label = ttk.Label(self.frame, textvariable=self.result_var)
        self.result_label.grid(row=2, column=0, columnspan=3, pady=5)
        
    def convert(self):
        try:
            temp = float(self.temperature.get())
            if self.from_unit.get() == 'Fahrenheit':
                celsius = (temp - 32) * 5/9
                self.result_var.set(f"{temp}°F = {celsius:.2f}°C")
            else:
                fahrenheit = (temp * 9/5) + 32
                self.result_var.set(f"{temp}°C = {fahrenheit:.2f}°F")
        except ValueError:
            self.result_var.set("Please enter a valid number")

def main():
    root = tk.Tk()
    app = TemperatureConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
