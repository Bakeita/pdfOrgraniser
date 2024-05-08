import tkinter as tk
from tkinter import filedialog

def open_file_dialog():
    file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        print(f"Selected file: {file_path}")

# Create the main window
root = tk.Tk()
root.geometry("600x400")
root.title("Ouvrir Fichier ")

# Create a button to trigger the file dialog
open_button = tk.Button(root, text="Open File Dialog", command=open_file_dialog)
open_button.pack(pady=20)

# Run the main event loop

root.mainloop()