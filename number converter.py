import tkinter as tk
from tkinter import messagebox

def convert_number(number, from_base, to_base):
    try:
        decimal_number = int(number, from_base)
    except ValueError:
        return "Invalid number format for the base!"
    
    if to_base == 2:
        return bin(decimal_number)[2:] 
    elif to_base == 8:
        return oct(decimal_number)[2:] 
    elif to_base == 10:
        return str(decimal_number)     
    elif to_base == 16:
        return hex(decimal_number)[2:].upper()  
    else:
        return "Invalid target base!"

def handle_conversion():
    number = entry_number.get()
    from_base = int(entry_from_base.get())
    to_base = int(entry_to_base.get())
    
    result = convert_number(number, from_base, to_base)
    
    if result.startswith("Invalid"):
        messagebox.showerror("Error", result)
    else:
        label_result.config(text=f"Converted number: {result}")

root = tk.Tk()
root.title("Base Converter")

label_number = tk.Label(root, text="Enter the number:")
label_number.grid(row=0, column=0, padx=10, pady=10)

entry_number = tk.Entry(root)
entry_number.grid(row=0, column=1, padx=10, pady=10)

label_from_base = tk.Label(root, text="From base (2, 8, 10, 16):")
label_from_base.grid(row=1, column=0, padx=10, pady=10)

entry_from_base = tk.Entry(root)
entry_from_base.grid(row=1, column=1, padx=10, pady=10)

label_to_base = tk.Label(root, text="To base (2, 8, 10, 16):")
label_to_base.grid(row=2, column=0, padx=10, pady=10)

entry_to_base = tk.Entry(root)
entry_to_base.grid(row=2, column=1, padx=10, pady=10)

button_convert = tk.Button(root, text="Convert", command=handle_conversion)
button_convert.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

label_result = tk.Label(root, text="Converted number will appear here")
label_result.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Run the main event loop
root.mainloop()
