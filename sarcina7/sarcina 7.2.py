import tkinter as tk
from tkinter import ttk

class ModularExponentiationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Modular Exponentiation")

        self.label_n = ttk.Label(root, text="Enter n:")
        self.label_n.pack(pady=5)

        self.entry_n = ttk.Entry(root)
        self.entry_n.pack(pady=5)

        self.label_x = ttk.Label(root, text="Enter x:")
        self.label_x.pack(pady=5)

        self.entry_x = ttk.Entry(root)
        self.entry_x.pack(pady=5)

        self.encrypt_button = ttk.Button(root, text="Encrypt", command=self.encrypt_button_clicked)
        self.encrypt_button.pack(pady=10)

        self.decrypt_button = ttk.Button(root, text="Decrypt", command=self.decrypt_button_clicked)
        self.decrypt_button.pack(pady=10)

        self.result_label = ttk.Label(root, text="")
        self.result_label.pack(pady=10)

    def trans_base(self, n1):
        cif = []
        i = 0
        while n1 != 0:
            i += 1
            cif.append(n1 % 2)
            n1 = n1 // 2
        k = i
        return cif[::-1], k

    def inv(self, n, b):
        n0, b0 = n, b
        t0, t = 0, 1
        q1 = n0 // b
        r = n0 - q1 * b
        while r > 0:
            temp = t0 - q1 * t
            if temp >= 0:
                temp = temp % n
            else:
                temp = n - ((-temp) % n)
            n0, b0 = b0, r
            t0, t = t, temp
            q1 = n0 // b0
            r = n0 - q1 * b0
        if b0 != 1:
            t = 0
        return t

    def encrypt(self, n, x, c):
        cif, m = self.trans_base(c)
        z = 1
        for q in range(m, 0, -1):
            if cif[q - 1] == 0:
                z = (z * z) % n
            else:
                z = (z * z) % n
                z = (z * x) % n
        return z

    def decrypt(self, n, y, c):
        a = self.inv(n - 1, c)
        cif, m = self.trans_base(a)
        z = 1
        for q in range(m, 0, -1):
            if cif[q - 1] == 0:
                z = (z * z) % n
            else:
                z = (z * z) % n
                z = (z * y) % n
        return z

    def encrypt_button_clicked(self):
        n = int(self.entry_n.get())
        x = int(self.entry_x.get())
        c = int(input("Enter c: "))
        y = self.encrypt(n, x, c)
        self.show_result(f"Encrypted Message: {y}")

    def decrypt_button_clicked(self):
        n = int(self.entry_n.get())
        y = int(input("Enter y: "))
        c = int(input("Enter c: "))
        x = self.decrypt(n, y, c)
        self.show_result(f"Decrypted Message: {x}")

    def show_result(self, result_text):
        self.result_label.config(text=result_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = ModularExponentiationApp(root)
    root.mainloop()
