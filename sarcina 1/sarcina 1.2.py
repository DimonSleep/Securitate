import tkinter as tk
from tkinter import ttk

def calculate_inverse():
    n = int(n_entry.get())
    b = int(b_entry.get())

    n0, b0, t0, t = n, b, 0, 1
    q, r = divmod(n0, b0)

    while r > 0:
        temp = t0 - q * t
        if temp >= 0:
            temp = temp % n
        else:
            temp = n - (-temp) % n

        n0, b0, t0, t = b0, r, t, temp
        q, r = divmod(n0, b0)

    inverse_label.config(text=f'Inversa: {temp}')

# Interfață grafică
root = tk.Tk()
root.title("Calculator Invers Modular")

main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

n_label = ttk.Label(main_frame, text="Introdu n:")
n_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

n_entry = ttk.Entry(main_frame)
n_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

b_label = ttk.Label(main_frame, text="Introdu a:")
b_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

b_entry = ttk.Entry(main_frame)
b_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

calculate_button = ttk.Button(main_frame, text="Calculează Inversa", command=calculate_inverse)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

inverse_label = ttk.Label(main_frame, text="Inversa: ")
inverse_label.grid(row=3, column=0, columnspan=2, pady=5)

root.mainloop()
