import tkinter as tk
from tkinter import messagebox
import sqlite3


class PermissionManagementWindow:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        self.window = tk.Toplevel(master)
        self.window.title("权限管理")
        self.window.geometry("800x600")

        # 连接到权限数据库（如果不存在则创建）
        self.conn = sqlite3.connect('permissions.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS permissions (
                user_id INTEGER PRIMARY KEY,
                permission_level INTEGER NOT NULL
            )
        ''')

        # 假设用户ID为1的用户是我们要管理的用户
        self.user_id = 1

        # 标题
        self.title_label = tk.Label(self.window, text="权限管理", font=("Arial", 20))
        self.title_label.grid(row=0, column=0, columnspan=3, pady=20)

        # 版本选择
        self.version_frame = tk.Frame(self.window)
        self.version_frame.grid(row=1, column=0, columnspan=3)
        tk.Label(self.version_frame, text="选择权限版本：").pack(side=tk.LEFT)
        self.version_var = tk.IntVar()
        self.version1_check = tk.Checkbutton(self.version_frame, text="版本1", variable=self.version_var, onvalue=1, offvalue=0)
        self.version1_check.pack(side=tk.LEFT)
        self.version2_check = tk.Checkbutton(self.version_frame, text="版本2", variable=self.version_var, onvalue=2, offvalue=0)
        self.version2_check.pack(side=tk.LEFT)
        self.version3_check = tk.Checkbutton(self.version_frame, text="版本3", variable=self.version_var, onvalue=3, offvalue=0)
        self.version3_check.pack(side=tk.LEFT)

        # 权限提示
        self.permission_prompt = tk.Label(self.window, text="您当前的权限为：未知")
        self.permission_prompt.grid(row=2, column=0, columnspan=3, pady=20)

        # 确定按钮
        self.confirm_button = tk.Button(self.window, text="确定", command=self.set_permission, bg="lightblue")
        self.confirm_button.grid(row=3, column=1, pady=20)

        # 加载现有权限
        self.load_permissions()

    def set_permission(self):
        permission_level = self.version_var.get()

        # 更新数据库中的权限信息
        self.cursor.execute('''
            INSERT OR REPLACE INTO permissions (user_id, permission_level) VALUES (?,?)
        ''', (self.user_id, permission_level))
        self.conn.commit()

        # 应用新的权限设置并更新权限提示
        self.app.apply_permission_settings(permission_level)
        self.update_permission_prompt(permission_level)

        messagebox.showinfo("切换成功", f"权限已切换为版本{permission_level}")

    def load_permissions(self):
        self.cursor.execute('SELECT permission_level FROM permissions WHERE user_id=?', (self.user_id,))
        row = self.cursor.fetchone()
        if row:
            self.version_var.set(row[0])
            self.app.apply_permission_settings(row[0])
            self.update_permission_prompt(row[0])
        else:
            self.version_var.set(1)
            self.app.apply_permission_settings(1)
            self.update_permission_prompt(1)

    def update_permission_prompt(self, permission_level):
        if permission_level == 1:
            self.permission_prompt.config(text="您当前的权限为：版本1，可使用的功能：权限管理、语言")
        elif permission_level == 2:
            self.permission_prompt.config(text="您当前的权限为：版本2，可使用的功能：权限管理、语言、项目")
        elif permission_level == 3:
            self.permission_prompt.config(text="您当前的权限为：版本3，可使用的功能：权限管理、语言、项目、系统计算与风机选型")