import tkinter as tk
from tkinter import ttk

class SecretSharingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Secret Sharing")

        self.label_secret = ttk.Label(root, text="Enter secret:")
        self.label_secret.pack(pady=5)

        self.entry_secret = ttk.Entry(root)
        self.entry_secret.pack(pady=5)

        self.label_parts = ttk.Label(root, text="Enter number of parts:")
        self.label_parts.pack(pady=5)

        self.entry_parts = ttk.Entry(root)
        self.entry_parts.pack(pady=5)

        self.label_threshold = ttk.Label(root, text="Enter threshold (k):")
        self.label_threshold.pack(pady=5)

        self.entry_threshold = ttk.Entry(root)
        self.entry_threshold.pack(pady=5)

        self.encrypt_button = ttk.Button(root, text="Split Secret", command=self.encrypt_button_clicked)
        self.encrypt_button.pack(pady=10)

        self.decrypt_button = ttk.Button(root, text="Recover Secret", command=self.decrypt_button_clicked)
        self.decrypt_button.pack(pady=10)

        self.result_label = ttk.Label(root, text="")
        self.result_label.pack(pady=10)

    def split_secret(self, secret, num_parts, threshold):
        a = [int(input(f"Enter coefficient a[{i}]: ")) for i in range(1, threshold)]
        s = secret
        n = num_parts
        k = threshold

        b = [s + sum([a[j - 1] * (i ** j) for j in range(1, k)]) for i in range(1, n + 1)]

        return b

    def recover_secret(self, x, y, threshold):
        p1 = 0
        for i in range(threshold):
            l = 1
            for j in range(threshold):
                if j != i:
                    l *= (-x[j]) / (x[i] - x[j])
            l *= y[i]
            p1 += l
        return p1

    def encrypt_button_clicked(self):
        secret = int(self.entry_secret.get())
        num_parts = int(self.entry_parts.get())
        threshold = int(self.entry_threshold.get())

        b = self.split_secret(secret, num_parts, threshold)

        result_text = "Secret has been split into parts:\n" + "\n".join([f"{i}: {b[i-1]}" for i in range(1, num_parts + 1)])
        self.show_result(result_text)

    def decrypt_button_clicked(self):
        threshold = int(self.entry_threshold.get())
        x = [int(input(f"Enter x[{i}]: ")) for i in range(threshold)]
        y = [int(input(f"Enter y[{i}]: ")) for i in range(threshold)]

        secret = self.recover_secret(x, y, threshold)

        result_text = f"Recovered secret: {secret}"
        self.show_result(result_text)

    def show_result(self, result_text):
        self.result_label.config(text=result_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = SecretSharingApp(root)
    root.mainloop()
