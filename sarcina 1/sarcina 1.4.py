import tkinter as tk
from tkinter import ttk

def cezar_brut(s):
    results.delete(1.0, tk.END)  # Șterge textul existent în fereastra de rezultate
    for k in range(26):
        t = ''
        for char in s:
            if char.isalpha():
                a = ord(char.upper()) - 65
                t += chr(((a - k + 26) % 26) + 65)
            else:
                t += char
        result_text = f'k={k}: {t}\n'
        results.insert(tk.END, result_text)

def decrypt_button_click():
    encrypted_text = input_entry.get()
    cezar_brut(encrypted_text)

# Interfață grafică
root = tk.Tk()
root.title("Cezar_brut Decryptor")

main_frame = ttk.Frame(root, padding="10")
main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

input_label = ttk.Label(main_frame, text="Text criptat:")
input_label.grid(column=0, row=0, sticky=tk.W)

input_entry = ttk.Entry(main_frame, width=50)
input_entry.grid(column=1, row=0, sticky=(tk.W, tk.E))

decrypt_button = ttk.Button(main_frame, text="Decriptează", command=decrypt_button_click)
decrypt_button.grid(column=2, row=0, sticky=tk.W)

results_label = ttk.Label(main_frame, text="Rezultate:")
results_label.grid(column=0, row=1, sticky=tk.W)

results = tk.Text(main_frame, height=10, width=50, wrap=tk.WORD)
results.grid(column=0, row=2, columnspan=3)

root.mainloop()
