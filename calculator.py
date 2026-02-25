import tkinter as tk

# Create window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Entry box
entry = tk.Entry(root, width=20, font=("Arial", 20), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function to insert numbers
def click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

# Function to clear
def clear():
    entry.delete(0, tk.END)

# Function to calculate result
def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row = 1
col = 0

for button in buttons:
    if button == "C":
        tk.Button(root, text=button, padx=20, pady=20, command=clear).grid(row=row, column=col)
    elif button == "=":
        tk.Button(root, text=button, padx=20, pady=20, command=equal).grid(row=row, column=col)
    else:
        tk.Button(root, text=button, padx=20, pady=20,
                  command=lambda b=button: click(b)).grid(row=row, column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()