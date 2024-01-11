import tkinter as tk
from tkinter import ttk

def decrypt_caesar(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                decrypted_text += chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
            elif char.isupper():
                decrypted_text += chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text

def auto_decrypt(ciphertext):
    for shift in range(26):
        decrypted_text = decrypt_caesar(ciphertext, shift)
        print(f"Shift={shift}: {decrypted_text}")

class CryptoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Crypto App")

        self.label = ttk.Label(root, text="Enter ciphertext:")
        self.label.pack(pady=10)

        self.ciphertext_entry = ttk.Entry(root)
        self.ciphertext_entry.pack(pady=10)

        self.decrypt_button = ttk.Button(root, text="Auto Decrypt", command=self.decrypt_button_clicked)
        self.decrypt_button.pack(pady=10)

    def decrypt_button_clicked(self):
        ciphertext = self.ciphertext_entry.get()
        auto_decrypt(ciphertext)

if __name__ == "__main__":
    root = tk.Tk()
    app = CryptoApp(root)
    root.mainloop()
