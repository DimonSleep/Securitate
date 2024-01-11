import tkinter as tk
from tkinter import ttk

def init_alphabet():
    alphabet = [chr(ord('A') + i) for i in range(26)]
    return alphabet

def number_order(s, alphabet):
    n_o = [alphabet.index(char) if char in alphabet else -1 for char in s]
    return n_o

def encrypt_vigenere(s, ke, alphabet):
    n_o_s = number_order(s, alphabet)
    n_o_k = number_order(ke, alphabet)
    k, k1, j = len(s), len(ke), 1
    ciphertext = ''

    for i in range(k):
        if j > k1:
            j = 1
        if n_o_s[i] != -1:
            c = (n_o_s[i] + n_o_k[j - 1]) % 26
            ciphertext += alphabet[c]
            j += 1
        else:
            ciphertext += ' '

    return ciphertext

def decrypt_vigenere(tc, ke, alphabet, n_o_s):
    n_o_k = number_order(ke, alphabet)
    k, k1, j = len(tc), len(ke), 1
    plaintext = ''

    for i in range(k):
        if j > k1:
            j = 1
        if tc[i] != ' ':
            a = n_o_k[j - 1]
            c = (n_o_s[i] - a) % 26
            plaintext += alphabet[c]
            j += 1
        else:
            plaintext += ' '

    return plaintext

class VigenereApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Vigenere Cipher")

        self.label_ke = ttk.Label(root, text="Enter key:")
        self.label_ke.pack(pady=5)

        self.entry_ke = ttk.Entry(root)
        self.entry_ke.pack(pady=5)

        self.label_s = ttk.Label(root, text="Enter message:")
        self.label_s.pack(pady=5)

        self.entry_s = ttk.Entry(root)
        self.entry_s.pack(pady=5)

        self.encrypt_button = ttk.Button(root, text="Encrypt", command=self.encrypt_button_clicked)
        self.encrypt_button.pack(pady=10)

        self.decrypt_button = ttk.Button(root, text="Decrypt", command=self.decrypt_button_clicked)
        self.decrypt_button.pack(pady=10)

        self.result_label = ttk.Label(root, text="")
        self.result_label.pack(pady=10)

    def encrypt_button_clicked(self):
        ke = self.entry_ke.get().upper()
        s = self.entry_s.get().upper()
        alphabet = init_alphabet()
        n_o_s = number_order(s, alphabet)
        ciphertext = encrypt_vigenere(s, ke, alphabet)
        self.result_label.config(text=f"Encrypted Text: {ciphertext}")

    def decrypt_button_clicked(self):
        ke = self.entry_ke.get().upper()
        tc = self.result_label.cget("text").split(": ")[1]
        alphabet = init_alphabet()
        n_o_s = number_order(self.entry_s.get().upper(), alphabet)
        plaintext = decrypt_vigenere(tc, ke, alphabet, n_o_s)
        self.result_label.config(text=f"Decrypted Text: {plaintext}")

if __name__ == "__main__":
    root = tk.Tk()
    app = VigenereApp(root)
    root.mainloop()
