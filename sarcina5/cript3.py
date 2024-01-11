import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

# Global variables for alphabet and alphabet table
alphabet = []
alphabet_table = []
alphabet_table_flat = []
table_text_frame = None
table_text = None

def create_alphabet():
    fraza = input_entry.get().upper()
    alphabet = set(fraza)

    with open("alfabet1.txt", 'w') as alphabet_file:
        for char in alphabet:
            print(char, end='', file=alphabet_file)

        with open("alfabet.txt", 'r') as existing_alphabet:
            for char in existing_alphabet.read():
                if char not in alphabet:
                    print(char, end='', file=alphabet_file)

    alphabet_label.config(text=f'Alphabet created with {len(alphabet)} characters.')

def initialize_table():
    global alphabet, alphabet_table, alphabet_table_flat, table_text, table_text_frame
    num_lines = int(lines_entry.get())
    num_columns = int(columns_entry.get())

    eliminated_chars = eliminate_entry.get().split(',')
    eliminated_chars = set(map(str.strip, eliminated_chars))

    alphabet = []
    with open("alfabet1.txt", 'r') as alphabet_file:
        for _ in range(num_lines):
            row = []
            for _ in range(num_columns):
                char = alphabet_file.read(1)
                while char in eliminated_chars:
                    char = alphabet_file.read(1)
                row.append(char)
            alphabet.append(row)

    alphabet_table = ["".join(row) for row in alphabet]
    alphabet_table_flat = "".join(alphabet_table)

    # Adaugă această linie pentru a crea și afișa Text widget-ul
    table_text_frame = ttk.LabelFrame(root, text="Table Display")
    table_text_frame.grid(row=0, column=1, rowspan=3, padx=10, pady=10, sticky="nsew")

    table_text = tk.Text(table_text_frame, height=num_lines, width=num_columns*3, state=tk.NORMAL)
    table_text.pack(expand=True, fill="both")

    table_text.delete("1.0", tk.END)
    for i in range(num_lines):
        for j in range(num_columns):
            table_text.insert(tk.END, f"{alphabet[i][j]:3}")
        table_text.insert(tk.END, '\n')
    table_text.config(state=tk.DISABLED)

    init_label.config(text='Table initialized.')

def process_text(action):
    global alphabet_table_flat
    text = input_text.get("1.0", tk.END).upper().replace("\n", "")
    result = ""

    for char in text:
        if char in alphabet_table_flat:
            index = alphabet_table_flat.index(char)
            row = index // len(alphabet_table[0])
            col = index % len(alphabet_table[0])

            if action == "Encrypt":
                # Your encryption logic here
                result += f"{row}{col} "
            elif action == "Decrypt":
                # Your decryption logic here
                result += alphabet_table[row][col]

    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)
    output_text.config(state=tk.DISABLED)

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

# Initialize Table Frame
init_table_frame = ttk.LabelFrame(root, text="Initialize Table")
init_table_frame.grid(row=1, column=0, padx=10, pady=10, sticky="w")

lines_label = ttk.Label(init_table_frame, text="Number of Lines:")
lines_label.grid(row=0, column=0, padx=5, pady=5)

lines_entry = ttk.Entry(init_table_frame)
lines_entry.grid(row=0, column=1, padx=5, pady=5)

columns_label = ttk.Label(init_table_frame, text="Number of Columns:")
columns_label.grid(row=0, column=2, padx=5, pady=5)

columns_entry = ttk.Entry(init_table_frame)
columns_entry.grid(row=0, column=3, padx=5, pady=5)

eliminate_label = ttk.Label(init_table_frame, text="Eliminate Characters (comma-separated):")
eliminate_label.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

eliminate_entry = ttk.Entry(init_table_frame)
eliminate_entry.grid(row=1, column=2, padx=5, pady=5, columnspan=2)

initialize_table_button = ttk.Button(init_table_frame, text="Initialize Table", command=initialize_table)
initialize_table_button.grid(row=2, column=0, columnspan=4, pady=5)

init_label = ttk.Label(init_table_frame, text='')
init_label.grid(row=3, column=0, columnspan=4, pady=5)

# Process Text Frame
process_frame = ttk.LabelFrame(root, text="Process Text")
process_frame.grid(row=2, column=0, padx=10, pady=10, sticky="w")

input_text_label = ttk.Label(process_frame, text="Enter Text:")
input_text_label.grid(row=0, column=0, padx=5, pady=5)

input_text = tk.Text(process_frame, height=3, width=30, wrap=tk.WORD)
input_text.grid(row=0, column=1, padx=5, pady=5)

encrypt_button = ttk.Button(process_frame, text="Encrypt", command=lambda: process_text("Encrypt"))
encrypt_button.grid(row=1, column=0, padx=5, pady=5)

decrypt_button = ttk.Button(process_frame, text="Decrypt", command=lambda: process_text("Decrypt"))
decrypt_button.grid(row=1, column=1, padx=5, pady=5)

output_text_label = ttk.Label(process_frame, text="Result:")
output_text_label.grid(row=2, column=0, columnspan=2, pady=5)

output_text = tk.Text(process_frame, height=3, width=30, wrap=tk.WORD, state=tk.DISABLED)
output_text.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Configure resizing
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)

root.mainloop()
