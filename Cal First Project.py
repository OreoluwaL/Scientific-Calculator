import tkinter as tk
import math

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("350x390")
window.resizable(False, False) 
window. configure(bg="#FAF0FF")
 
# Display screen
display = tk.Entry(window, font=("Algerian", 20), bg="White", justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function to display numbers
def click(number):
    display.insert(tk.END, str(number))

def clear():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def square_root():
    try:
        result = math.sqrt(float(display.get()))
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


def sine():
    try:
        result = math.sin(math.radians(float(display.get())))
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


def cosine():
    try:
        result = math.cos(math.radians(float(display.get())))
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


def tangent():
    try:
        result = math.tan(math.radians(float(display.get())))
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


def logarithm():
    try:
        result = math.log10(float(display.get()))
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")
 

def operator(symbol):
    display.insert(tk.END, symbol)
# Number buttons
tk.Button(window, text="7", width=8, height=3, bg="Thistle", command=lambda: click(7)).grid(row=1, column=0)
tk.Button(window, text="8", width=8, height=3, bg="Thistle", command=lambda: click(8)).grid(row=1, column=1)
tk.Button(window, text="9", width=8, height=3, bg="Thistle", command=lambda: click(9)).grid(row=1, column=2)

tk.Button(window, text="4", width=8, height=3, bg="Thistle", command=lambda: click(4)).grid(row=2, column=0)
tk.Button(window, text="5", width=8, height=3, bg="Thistle", command=lambda: click(5)).grid(row=2, column=1)
tk.Button(window, text="6", width=8, height=3, bg="Thistle", command=lambda: click(6)).grid(row=2, column=2)

tk.Button(window, text="1", width=8, height=3, bg="Thistle", command=lambda: click(1)).grid(row=3, column=0)
tk.Button(window, text="2", width=8, height=3, bg="Thistle", command=lambda: click(2)).grid(row=3, column=1)
tk.Button(window, text="3", width=8, height=3, bg="Thistle", command=lambda: click(3)).grid(row=3, column=2)

tk.Button(window, text="0", width=8, height=3, bg="Thistle", command=lambda: click(0)).grid(row=4, column=1)
# Operator Buttons
tk.Button(window, text="+", width=8, height=3, bg="Plum",
          command=lambda: operator("+")).grid(row=1, column=3)

tk.Button(window, text="-", width=8, height=3, bg="Plum",
          command=lambda: operator("-")).grid(row=2, column=3)

tk.Button(window, text="×", width=8, height=3, bg="Plum",
          command=lambda: operator("*")).grid(row=3, column=3)

tk.Button(window, text="÷", width=8, height=3, bg="Plum",
          command=lambda: operator("/")).grid(row=4, column=3)

tk.Button(window, text="√", width=8, height=2, bg="Plum",
          command=square_root).grid(row=5, column=0)

tk.Button(window, text="sin", width=8, height=2, bg="Plum",
          command=sine).grid(row=5, column=1)

tk.Button(window, text="cos", width=8, height=2, bg="plum",
          command=cosine).grid(row=5, column=2)

tk.Button(window, text="tan", width=8, height=2, bg="plum",
          command=tangent).grid(row=5, column=3)

tk.Button(window, text="log", width=8, height=2, bg="plum",
          command=logarithm).grid(row=6, column=0)

# Equal Button
tk.Button(window, text="=", width=8, height=3, bg="Orchid",
          command=calculate).grid(row=4, column=2)

# Clear Button
tk.Button(window, text="C", width=8, height=3, bg="Lavender",
          command=clear).grid(row=4, column=0)
window.mainloop()