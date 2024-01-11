import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

n = 0
p = []
inv_p = []

def initialize():
    global n, p, inv_p
    n = int(n_entry.get())
    
    p_str = p_entry.get()
    p = [int(x) for x in p_str.split()]  # Utilizăm split() fără argument pentru a separa valorile
    
    inv_p = [0] * n
    for i in range(n):
        inv_p[p[i] - 1] = i + 1

def encrypt():
    initialize()
    
    with open("clar.txt", 'r') as f:
        plaintext = f.read().strip()

    encrypted_text = [''] * n
    for i in range(n):
        encrypted_text[p[i] - 1] = plaintext[i]

    encrypted_str = ''.join(encrypted_text)
    encrypted_label.config(text=f'Encrypted Text: {encrypted_str}')

    with open("cript.txt", 'w') as g:
        g.write(encrypted_str)

def decrypt():
    initialize()

    with open("cript.txt", 'r') as g:
        encrypted_text = g.read().strip()

    decrypted_text = [''] * n
    for i in range(n):
        decrypted_text[inv_p[i] - 1] = encrypted_text[i]

    decrypted_str = ''.join(decrypted_text)
    decrypted_label.config(text=f'Decrypted Text: {decrypted_str}')

    with open("decript.txt", 'w') as f1:
        f1.write(decrypted_str)

# GUI setup
root = tk.Tk()
root.title("Permutation Cipher Application")

# Input pentru n
n_label = ttk.Label(root, text="Enter 'n' value:")
n_label.grid(row=0, column=0, padx=5, pady=5)

n_entry = ttk.Entry(root)
n_entry.grid(row=0, column=1, padx=5, pady=5)

# Input pentru permutare
p_label = ttk.Label(root, text="Enter permutation (comma separated):")
p_label.grid(row=1, column=0, padx=5, pady=5)

p_entry = ttk.Entry(root)
p_entry.grid(row=1, column=1, padx=5, pady=5)

# Buton pentru criptare
encrypt_button = ttk.Button(root, text="Encrypt", command=encrypt)
encrypt_button.grid(row=2, column=0, columnspan=2, pady=5)

# Buton pentru decriptare
decrypt_button = ttk.Button(root, text="Decrypt", command=decrypt)
decrypt_button.grid(row=3, column=0, columnspan=2, pady=5)

# Etichete pentru text criptat și decriptat
encrypted_label = ttk.Label(root, text='Encrypted Text:')
encrypted_label.grid(row=4, column=0, padx=10, pady=10)

decrypted_label = ttk.Label(root, text='Decrypted Text:')
decrypted_label.grid(row=5, column=0, padx=10, pady=10)

root.mainloop()
