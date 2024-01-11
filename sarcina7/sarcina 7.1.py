import tkinter as tk
from tkinter import ttk

class ModuloInverseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Modulo Inverse Calculator")

        self.label_n = ttk.Label(root, text="Enter n:")
        self.label_n.pack(pady=5)

        self.entry_n = ttk.Entry(root)
        self.entry_n.pack(pady=5)

        self.label_a = ttk.Label(root, text="Enter a:")
        self.label_a.pack(pady=5)

        self.entry_a = ttk.Entry(root)
        self.entry_a.pack(pady=5)

        self.calculate_button = ttk.Button(root, text="Calculate", command=self.calculate_button_clicked)
        self.calculate_button.pack(pady=10)

        self.result_label = ttk.Label(root, text="")
        self.result_label.pack(pady=10)

    def calculate_inverse(self, n, a):
        n0, b0 = n, a
        t0, t = 0, 1
        q = n0 // b0
        r = n0 - q * b0

        while r > 0:
            temp = t0 - q * t
            if temp >= 0:
                temp = temp % n
            else:
                temp = n - ((-temp) % n)

            n0, b0 = b0, r
            t0, t = t, temp

            q = n0 // b0
            r = n0 - q * b0

        if b0 != 1:
            return None
        else:
            return t

    def calculate_button_clicked(self):
        n = int(self.entry_n.get())
        a = int(self.entry_a.get())

        inverse = self.calculate_inverse(n, a)

        if inverse is not None:
            result_text = f"Inverse modulo {n}: {inverse}"
        else:
            result_text = f"{a} does not have an inverse modulo {n}"

        self.result_label.config(text=result_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = ModuloInverseApp(root)
    root.mainloop()
