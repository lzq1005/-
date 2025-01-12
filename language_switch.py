import tkinter as tk
import json
from tkinter import messagebox

def update_widget_text(widget, language_data):
    if hasattr(widget, 'config') and 'text' in widget.config():
        widget_text = widget.cget('text')
        widget.config(text=language_data.get(widget_text, widget_text))
    for child in widget.winfo_children():
        update_widget_text(child, language_data)
        


class LanguageSwitchWindow:
    def __init__(self, master):
        self.master = master
        self.window = tk.Toplevel(master)
        self.window.title("语言切换")
        self.window.geometry("800x600")

        self.language_frame = tk.Frame(self.window)
        self.language_frame.pack()
        tk.Label(self.language_frame, text="选择语言：").pack(side=tk.LEFT)
        self.language_var = tk.StringVar()
        tk.Radiobutton(self.language_frame, text="中文", variable=self.language_var, value="zh-CN").pack(side=tk.LEFT)
        tk.Radiobutton(self.language_frame, text="英文", variable=self.language_var, value="en-US").pack(side=tk.LEFT)

        self.switch_button = tk.Button(self.window, text="切换", command=self.switch_language)
        self.switch_button.pack()

    def switch_language(self):
        selected_language = self.language_var.get()
        try:
            with open(f'{selected_language}.json', 'r', encoding='utf-8') as file:
                language_data = json.load(file)
            update_widget_text(self.master, language_data)
            messagebox.showinfo("提示", language_data.get("语言已成功切换为", "Language has been switched successfully."))
        except FileNotFoundError:
            messagebox.showerror("错误", f"语言文件 {selected_language}.json 未找到。")
