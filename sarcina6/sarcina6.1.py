import tkinter as tk
from tkinter import ttk
import secrets

class SynchronousKeyFluidsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Synchronous Fluid Keys")

        self.label_text = ttk.Label(root, text="Enter text:")
        self.label_text.pack(pady=5)

        self.entry_text = ttk.Entry(root)
        self.entry_text.pack(pady=5)

        self.label_key_size = ttk.Label(root, text="Enter key size:")
        self.label_key_size.pack(pady=5)

        self.entry_key_size = ttk.Entry(root)
        self.entry_key_size.pack(pady=5)

        self.encrypt_button = ttk.Button(root, text="Encrypt", command=self.encrypt_button_clicked)
        self.encrypt_button.pack(pady=10)

        self.decrypt_button = ttk.Button(root, text="Decrypt", command=self.decrypt_button_clicked)
        self.decrypt_button.pack(pady=10)

        self.Im = []  # Vectorul Im
        self.gen = None  # Generatorul pentru cheie

    def generate_key(self, size):
        return [secrets.randbelow(256) for _ in range(size)]  # Generare cheie aleatoare între 0 și 255

    def encrypt_button_clicked(self):
        text = self.entry_text.get()
        key_size = int(self.entry_key_size.get())

        if key_size > len(text):
            self.show_result("Invalid key size.")
            return

        self.Im = self.generate_key(key_size)
        self.gen = iter(self.Im)

        ciphertext = self.encrypt(text)
        key_str = ", ".join(map(str, self.Im))  # Conversie cheie la șir de caractere
        result_text = f"Encrypted Text: {ciphertext}\nKey: {key_str}"
        self.show_result(result_text)
        print(result_text)  # Afișare în terminal

    def decrypt_button_clicked(self):
        text = self.entry_text.get()

        if self.gen is None:
            self.show_result("Invalid key or key not generated.")
            return

        try:
            plaintext = self.decrypt(text)
            result_text = f"Decrypted Text: {plaintext}"
            self.show_result(result_text)
            print(result_text)  # Afișare în terminal
        except StopIteration:
            self.show_result("Key exhausted. Regenerate a new key.")
            self.gen = iter(self.Im)  # Regenerarea cheii

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
    app = SynchronousKeyFluidsApp(root)
    root.mainloop()
