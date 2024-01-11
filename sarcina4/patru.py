import tkinter as tk
from tkinter import ttk, messagebox

class HillCipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hill Cipher")

        self.label_key = ttk.Label(root, text="Enter key (k):")
        self.label_key.pack(pady=5)

        self.entry_key = ttk.Entry(root)
        self.entry_key.pack(pady=5)

        self.label_text = ttk.Label(root, text="Enter text:")
        self.label_text.pack(pady=5)

        self.entry_text = ttk.Entry(root)
        self.entry_text.pack(pady=5)

        self.encrypt_button = ttk.Button(root, text="Encrypt", command=self.encrypt_button_clicked)
        self.encrypt_button.pack(pady=10)

        self.decrypt_button = ttk.Button(root, text="Decrypt", command=self.decrypt_button_clicked)
        self.decrypt_button.pack(pady=10)

    def number_order(self, s):
        return [ord(char) - ord('A') for char in s]

    def matrix_multiply(self, m, lin):
        return [sum([lin[j] * m[j][i] for j in range(len(lin))]) % 26 for i in range(len(m[0]))]

    def encrypt(self, s, key):
        try:
            k = int(key)
            M_cript = [[int(input(f"Enter M_cript[{i + 1}][{j + 1}]: ")) for j in range(k)] for i in range(k)]
            n_o = self.number_order(s)
            b = len(s)
            i = 0
            tc = ''
            while i <= b - 2:
                lin = n_o[i:i+k]
                result = self.matrix_multiply(M_cript, lin)
                tc += ''.join([chr(result[j] + ord('A')) for j in range(len(result))])
                i += 3
            return tc
        except ValueError:
            messagebox.showerror("Error", "Invalid input for key or matrix elements. Please enter valid integers.")

    def decrypt(self, tc, key):
        try:
            k = int(key)
            M_decript = [[int(input(f"Enter M_decript[{i + 1}][{j + 1}]: ")) for j in range(k)] for i in range(k)]
            n_o = self.number_order(tc)
            b = len(tc)
            i = 0
            s = ''
            while i <= b - 2:
                lin = n_o[i:i+k]
                result = self.matrix_multiply(M_decript, lin)
                s += ''.join([chr(result[j] + ord('A')) for j in range(len(result))])
                i += 3
            return s
        except ValueError:
            messagebox.showerror("Error", "Invalid input for key or matrix elements. Please enter valid integers.")

    def encrypt_button_clicked(self):
        key = self.entry_key.get()
        s = self.entry_text.get()
        ciphertext = self.encrypt(s, key)
        self.show_result(f"Encrypted Text: {ciphertext}")

    def decrypt_button_clicked(self):
        key = self.entry_key.get()
        tc = self.entry_text.get()
        plaintext = self.decrypt(tc, key)
        self.show_result(f"Decrypted Text: {plaintext}")

    def show_result(self, result_text):
        result_label = ttk.Label(self.root, text=result_text)
        result_label.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = HillCipherApp(root)
    root.mainloop()
