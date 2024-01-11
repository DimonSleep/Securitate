import tkinter as tk
from tkinter import ttk
import random

class FluidKeyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fluid Keys")

        self.label_text = ttk.Label(root, text="Enter text:")
        self.label_text.pack(pady=5)

        self.entry_text = ttk.Entry(root)
        self.entry_text.pack(pady=5)

        self.encrypt_button = ttk.Button(root, text="Encrypt", command=self.encrypt_button_clicked)
        self.encrypt_button.pack(pady=10)

        self.decrypt_button = ttk.Button(root, text="Decrypt", command=self.decrypt_button_clicked)
        self.decrypt_button.pack(pady=10)

        self.key_label = ttk.Label(root, text="Key:")
        self.key_label.pack(pady=5)

        self.Im = []  # Vectorul Im pentru a stoca ordinea caracterelor în alfabet
        self.gen = None  # Inițializarea la None pentru a genera cheia ulterior

    def generate_key(self):
        self.Im = [i for i in range(256)]  # Exemplu simplificat pentru alfabet ASCII
        random.shuffle(self.Im)
        return self.Im

    def encrypt_button_clicked(self):
        text = self.entry_text.get()

        if not self.gen:
            self.Im = self.generate_key()
            self.gen = self.generator(len(self.Im))
            key_text = " ".join(map(str, self.Im))
            self.key_label.config(text=f"Key: {key_text}")

        ciphertext = self.encrypt(text)
        self.show_result(f"Encrypted Text: {ciphertext}")

    def decrypt_button_clicked(self):
        text = self.entry_text.get()

        if not self.gen:
            self.show_result("Invalid key or key not generated.")
            return

        plaintext = self.decrypt(text)
        self.show_result(f"Decrypted Text: {plaintext}")

    def generator(self, q):
        F1 = 1
        F2 = 1
        for _ in range(3, q + 1):
            F = F1 + F2
            F = F % len(self.Im)
            yield F
            F1, F2 = F2, F

    def encrypt(self, s):
        k = len(s)
        c = [(ord(s[i]) + next(self.gen)) % 256 for i in range(k)]
        encrypted_text = ''.join([chr(j) for j in c])
        return encrypted_text

    def decrypt(self, tc):
        k = len(tc)
        c = [(ord(tc[i]) - next(self.gen)) % 256 for i in range(k)]
        decoded_text = ''.join([chr(j) for j in c])
        return decoded_text

    def show_result(self, result_text):
        result_label = ttk.Label(self.root, text=result_text)
        result_label.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = FluidKeyApp(root)
    root.mainloop()
