import tkinter as tk
from tkinter import filedialog
import requests
import os

def install_file():
    folder = filedialog.askdirectory()
    if not folder:
        result_label.config(text="Установка отменена.")
        return

    try:
        url = "http://127.0.0.1:5000/download"
        response = requests.get(url)
        response.raise_for_status()

        file_path = os.path.join(folder, "my.txt")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(response.text)

        result_label.config(text=f"Файл установлен в:\n{file_path}")
    except Exception as e:
        result_label.config(text=f"Ошибка: {str(e)}")

root = tk.Tk()
root.title("install")
root.geometry("400x150")

label = tk.Label(root, text="Выберите папку для установки файла:")
label.pack(pady=10)

btn = tk.Button(root, text="Установить файл", command=install_file)
btn.pack()

result_label = tk.Label(root, text="", wraplength=380, fg="green")
result_label.pack(pady=10)

root.mainloop()
