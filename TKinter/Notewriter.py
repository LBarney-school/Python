# Behold the imports!
import sys
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def open_file():
    # Open a File, post the file contents to the text field
    filepath = askopenfilename(
        # Expected filetypes
        filetypes=[
            ("Text Files", "*.txt"),
            ("JSON Files", "*.json"),
            ("All Files", "*.*"),
        ]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, "r", encoding="utf-8") as input_file:
        # Error catch in case something weird happens during file load
        try:
            text = input_file.read()
            txt_edit.insert(tk.END, text)
            input_file.close()
            window.title(f"Notewriter - {filepath}")
        except UnicodeDecodeError:
            print("UnicodeDecodeError")
            pass


def save_file():
    # Save Current File As New File
    filepath = asksaveasfilename(
        # Expected filetypes
        defaultextension=".txt",
        filetypes=[
            ("Text Files", "*.txt"),
            ("JSON Files", "*.json"),
            ("All Files", "*.*"),
        ],
    )
    if not filepath:
        return
    with open(filepath, "w", encoding="utf-8") as output_file:
        # Save file data to selected file
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
        output_file.close()
    window.title(f"Notewriter - {filepath}")


def endProg():
    # Close window and properly end program
    window.destroy()
    sys.exit(0)


# Open Window
window = tk.Tk()
window.title("Notewriter")

# Configure basic window parameters
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

# Set up window frame and buttons
txt_edit = tk.Text(window)
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(frm_buttons, text="Open", command=open_file)
btn_save = tk.Button(frm_buttons, text="Save As...", command=save_file)
btn_close = tk.Button(frm_buttons, text="Close", command=endProg)

# Set up button padding
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_close.grid(row=2, column=0, sticky="ew", padx=5)

frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

# Run window
window.mainloop()
