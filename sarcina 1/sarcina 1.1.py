import tkinter as tk
from tkinter import ttk

def inv(n, b):
    n0, b0, r, q1, t0, temp = n, b, 0, 0, 0, 0
    t = 1

    while r > 0:
        q1 = n0 // b0
        r = n0 - q1 * b0

        temp = t0 - q1 * t
        if temp >= 0:
            temp = temp % n
        else:
            temp = n - ((-temp) % n)

        n0, b0, t0, t = b0, r, t, temp

    if b0 != 1:
        t = 0
        print(b, ' nu are inversa mod ', n)
    else:
        print('inversa=', t)
    return t

def init_alphabet():
    with open("alfabet.txt", 'r') as alphabet_file:
        alphabet = alphabet_file.read().strip()
        return list(alphabet)

def numar_ordine(s, alfabet):
    n_o = [alfabet.index(char) for char in s]
    print(n_o)

def cript(a, b2, n_o, alfabet):
    c = [(a * i + b2) % len(alfabet) for i in n_o]
    tc = ''.join([alfabet[i] for i in c])
    return tc

def decript(t1, b2, n_o, alfabet):
    c = [(t1 * i + (t1 * (len(alfabet) - b2)) % len(alfabet)) % len(alfabet) for i in n_o]
    tc = ''.join([alfabet[i] for i in c])
    return tc

def create_alphabet():
    global alphabet
    alphabet = init_alphabet()
    alphabet_label.config(text=f'Alphabet created with {len(alphabet)} characters.')

def encrypt():
    try:
        a_value = int(a_entry.get())
        b_value = int(b_entry.get())
    except ValueError:
        encrypt_label.config(text='Invalid input for a or b. Please enter numeric values.')
        return

    key_phrase = input_entry.get().upper()
    n_o = [alphabet.index(char) for char in key_phrase]

    with open("clar.txt", 'r') as f:
        plaintext = f.read().strip()

    ciphertext = cript(a_value, b_value, n_o, alphabet)

    with open("cript.txt", 'w') as g:
        g.write(ciphertext)

    encrypt_label.config(text='Encryption completed.')

def decrypt():
    try:
        t_value = int(t_entry.get())
        b_value = int(b_entry.get())
    except ValueError:
        decrypt_label.config(text='Invalid input for t or b. Please enter numeric values.')
        return

    key_phrase = input_entry.get().upper()
    n_o = [alphabet.index(char) for char in key_phrase]

    with open("cript.txt", 'r') as g:
        ciphertext = g.read().strip()

    decrypted_text = decript(t_value, b_value, n_o, alphabet)

    with open("decript.txt", 'w') as f1:
        f1.write(decrypted_text)

    decrypt_label.config(text='Decryption completed.')


# GUI setup
root = tk.Tk()
root.title("Encryption Application")

# Create Alphabet Frame
create_alphabet_frame = ttk.LabelFrame(root, text="Create Alphabet")
create_alphabet_frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")

input_label = ttk.Label(create_alphabet_frame, text="Enter Key Phrase:")
input_label.grid(row=0, column=0, padx=5, pady=5)

input_entry = ttk.Entry(create_alphabet_frame)
input_entry.grid(row=0, column=1, padx=5, pady=5)

create_alphabet_button = ttk.Button(create_alphabet_frame, text="Create Alphabet", command=create_alphabet)
create_alphabet_button.grid(row=0, column=2, padx=5, pady=5)

alphabet_label = ttk.Label(create_alphabet_frame, text='')
alphabet_label.grid(row=1, column=0, columnspan=3, pady=5)

# Encrypt and Decrypt Frames
encrypt_frame = ttk.LabelFrame(root, text="Encrypt")
encrypt_frame.grid(row=1, column=0, padx=10, pady=10, sticky="w")

a_label = ttk.Label(encrypt_frame, text="Enter 'a' value:")
a_label.grid(row=0, column=0, padx=5, pady=5)

a_entry = ttk.Entry(encrypt_frame)
a_entry.grid(row=0, column=1, padx=5, pady=5)

b_label = ttk.Label(encrypt_frame, text="Enter 'b' value:")
b_label.grid(row=1, column=0, padx=5, pady=5)

b_entry = ttk.Entry(encrypt_frame)
b_entry.grid(row=1, column=1, padx=5, pady=5)

encrypt_button = ttk.Button(encrypt_frame, text="Encrypt", command=encrypt)
encrypt_button.grid(row=2, column=0, columnspan=2, pady=5)

encrypt_label = ttk.Label(encrypt_frame, text='')
encrypt_label.grid(row=3, column=0, columnspan=2, pady=5)

decrypt_frame = ttk.LabelFrame(root, text="Decrypt")
decrypt_frame.grid(row=2, column=0, padx=10, pady=10, sticky="w")

t_label = ttk.Label(decrypt_frame, text="Enter 't' value:")
t_label.grid(row=0, column=0, padx=5, pady=5)

t_entry = ttk.Entry(decrypt_frame)
t_entry.grid(row=0, column=1, padx=5, pady=5)

decrypt_button = ttk.Button(decrypt_frame, text="Decrypt", command=decrypt)
decrypt_button.grid(row=1, column=0, columnspan=2, pady=5)

decrypt_label = ttk.Label(decrypt_frame, text='')
decrypt_label.grid(row=2, column=0, columnspan=2, pady=5)

root.mainloop()
