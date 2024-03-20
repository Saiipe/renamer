import tkinter as tk
from tkinter import filedialog

pdf_paths = filedialog.askopenfilenames()
root = tk.Tk()
root.withdraw()
root.destroy()