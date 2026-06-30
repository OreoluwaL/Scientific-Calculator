import tkinter as tk
import math
import numpy as np
mode = "scientific"

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("400x400") 
window.resizable(False, False) 
window.configure(bg="#FAF0FF")

# Display screen
display = tk.Entry(window, font=("Algerian", 20), bg="White", justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#Matrix
def open_matrix():
    matrix_window = tk.Toplevel(window)
    matrix_window.title("Matrix Calculator")
    matrix_window.geometry("500x500")
    matrix_window.configure(bg="#FAF0FF")

    tk.Label(matrix_window, text="Matrix Calculator", bg="#FAF0FF", font=("Arial", 14, "bold")).grid(row=0, column=1, padx=10, pady=5)


    # -------- MATRIX INPUTS --------
    tk.Label(matrix_window, text="Matrix A", bg="#FAF0FF",
             font=("Arial", 11, "bold")).grid(row=1, column=0, padx=10, pady=5)

    matrix_a = tk.Text(matrix_window, width=10, height=5)
    matrix_a.grid(row=2, column=0, padx=10, pady=5)

    tk.Label(matrix_window, text="Matrix B", bg="#FAF0FF",
             font=("Arial", 11, "bold")).grid(row=1, column=1, padx=10, pady=5)

    matrix_b = tk.Text(matrix_window, width=10, height=5)
    matrix_b.grid(row=2, column=1, padx=10, pady=5)

    result_label = tk.Label(matrix_window,
                            text="Result",
                            bg="white",
                            width=40,
                            height=6,
                            relief="sunken",
                            justify="left")
    result_label.grid(row=3, column=0, columnspan=2, pady=10)

    # -------- HELPER FUNCTION --------
    def get_matrix(textbox):
        text = textbox.get("1.0", tk.END).strip()
        rows = text.split("\n")
        matrix = []

        for row in rows:
            if row.strip():
                matrix.append(list(map(float, row.split())))

        return np.array(matrix)

    # -------- MATRIX OPERATIONS --------
    def matrix_add():
        try:
            A = get_matrix(matrix_a)
            B = get_matrix(matrix_b)
            if A.shape != B.shape:
                result_label.config(text="Matrices must have same dimensions")
                return
            result_label.config(text=str(A + B))
        except:
            result_label.config(text="Invalid Matrix")

    def matrix_sub():
        try:
            A = get_matrix(matrix_a)
            B = get_matrix(matrix_b)
            if A.shape != B.shape:
                result_label.config(text="Matrices must have same dimensions")
                return
            result_label.config(text=str(A - B))
        except:
            result_label.config(text="Invalid Matrix")

    def matrix_mul():
        try:
            A = get_matrix(matrix_a)
            B = get_matrix(matrix_b)
            if A.shape[1] != B.shape[0]:
                result_label.config(text=f"Cannot Multiply: A columns ({A.shape[1]}) != B rows ({B.shape[0]})")
                return
            result_label.config(text=str(np.dot(A, B)))
        except:
            result_label.config(text="Cannot Multiply")

    def determinant():
        try:
            A = get_matrix(matrix_a)
            if A.shape[0] != A.shape[1]:
                result_label.config(text="Matrix must be square")
                return
            result_label.config(text=str(np.linalg.det(A)))
        except:
            result_label.config(text="Invalid Matrix")

    def inverse():
        try:
            A = get_matrix(matrix_a)
            if A.shape[0] != A.shape[1]:
                result_label.config(text="Matrix must be square")
                return
            result_label.config(text=str(np.linalg.inv(A)))
        except:
            result_label.config(text="No Inverse")

    def transpose():
        try:
            A = get_matrix(matrix_a)
            result_label.config(text=str(A.T))
        except:
            result_label.config(text="Invalid Matrix")

    # -------- MATRIX BUTTONS --------
    frame = tk.Frame(matrix_window, bg="#FAF0FF")
    frame.grid(row=4, column=0, columnspan=2, pady=10)

    tk.Button(frame, text="A + B", width=12, bg="Thistle",
                  command=matrix_add).grid(row=0, column=0, padx=5, pady=5)

    tk.Button(frame, text="A - B", width=5, bg="Thistle",
                  command=matrix_sub).grid(row=0, column=1, padx=5, pady=5)

    tk.Button(frame, text="A × b", width=5, bg="Thistle",
                  command=matrix_mul).grid(row=0, column=2, padx=5, pady=5)

    tk.Button(frame, text="Det(A)", width=5, bg="Plum",
                  command=determinant).grid(row=1, column=0, padx=5, pady=5)

    tk.Button(frame, text="Inverse", width=5, bg="Plum",
                  command=inverse).grid(row=1, column=1, padx=5, pady=5)

    tk.Button(frame, text="Transpose", width=5, bg="Plum",
                  command=transpose).grid(row=1, column=2, padx=5, pady=5)

    tk.Button(frame, text="Close", width=5, bg="LightPink",
                  command=matrix_window.destroy).grid(row=2, column=1, padx=5, pady=10)

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
        value = float(display.get())
        if value < 0:
            display.delete(0, tk.END)
            display.insert(0, "Error")
        else:
            result = math.sqrt(value)
            display.delete(0, tk.END)
            display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def square():
    try:
        value = float(display.get())
        result = value ** 2
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def power():
    try:
        # Expects format: base,exp or base^exp
        text = display.get()
        if "," in text:
            base, exp = map(float, text.split(","))
        elif "^" in text:
            parts = text.split("^")
            base = float(parts[0])
            exp = float(parts[1])
        else:
            display.delete(0, tk.END)
            display.insert(0, "Error")
            return
        result = base ** exp
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
        
def sinh():
    try:
        result = math.sinh(float(display.get()))
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def cosh():
    try:
        result = math.cosh(float(display.get()))
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def tanh():
    try:
        result = math.tanh(float(display.get()))
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")
    
def permutation():
    try:
        n, r = map(int, display.get().split(","))
        result = math.perm(n, r)
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def combination():
    try:
        n, r = map(int, display.get().split(","))
        result = math.comb(n, r)
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def factorial():
    try:
        result = math.factorial(int(float(display.get())))
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
tk.Button(window, text=".", width=8, height=3, bg="Thistle", command=lambda: click(".")).grid(row=4, column=0)

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
          command=square_root).grid(row=2, column=5)

tk.Button(window, text="sin", width=8, height=2, bg="Plum",
          command=sine).grid(row=5, column=0)

tk.Button(window, text="cos", width=8, height=2, bg="plum",
          command=cosine).grid(row=5, column=1)

tk.Button(window, text="tan", width=8, height=2, bg="plum",
          command=tangent).grid(row=5, column=2)

tk.Button(window, text="log", width=8, height=2, bg="plum",
          command=logarithm).grid(row=5, column=3)

tk.Button(window, text="sinh", width=8, height=2, bg="plum", command=sinh).grid(row=6, column=0)
tk.Button(window, text="cosh", width=8, height=2, bg="plum", command=cosh).grid(row=6, column=1)
tk.Button(window, text="tanh", width=8, height=2, bg="plum", command=tanh).grid(row=6, column=2)

tk.Button(window, text="x²", width=8, height=3, bg="Orchid", command=square).grid(row=2, column=4)
tk.Button(window, text="xʸ", width=8, height=3, bg="Orchid", command=power).grid(row=3, column=4)
tk.Button(window, text="nCr", width=8, height=3, bg="Orchid", command=combination).grid(row=4, column=4)
tk.Button(window, text="nPr", width=8, height=2, bg="Orchid", command=permutation).grid(row=6, column=3)
tk.Button(window, text="!", width=8, height=2, bg="Orchid", command=factorial).grid(row=6, column=4)
tk.Button(window, text="Matrix",  bg="Plum", fg="Black", command=open_matrix).grid(row=0, column=4, padx=5)

# Equal Button
tk.Button(window, text="=", width=8, height=3, bg="Lavender",
          command=calculate).grid(row=4, column=2)

# Clear Button
tk.Button(window, text="C", width=8, height=3, bg="Lavender",
          command=clear).grid(row=1, column=4)

window.mainloop()
