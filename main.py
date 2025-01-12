import tkinter as tk
from permission_management import PermissionManagementWindow
from language_switch import LanguageSwitchWindow
from project_management import ProjectManagementWindow
from system_calculation import SystemCalculationWindow


class TunnelFanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tunnel Fan App")
        self.root.geometry("800x600")
        # 创建主界面按钮
        self.create_main_buttons()

    def create_main_buttons(self):
        # 设置按钮的宽度和高度
        button_width = 20
        button_height = 3

        # 权限管理按钮
        self.permission_button = tk.Button(self.root, text="权限管理\n管理用户权限和角色", command=self.open_permission_management, width=button_width, height=button_height)
        self.permission_button.pack()

        # 中英文切换按钮
        self.language_button = tk.Button(self.root, text="中英文切换\n切换应用程序语言", command=self.open_language_switch, width=button_width, height=button_height)
        self.language_button.pack()

        # 项目管理按钮
        self.project_button = tk.Button(self.root, text="项目管理\n查看和管理项目", command=self.open_project_management, width=button_width, height=button_height)
        self.project_button.pack()

        # 系统计算及风机选型按钮
        self.system_button = tk.Button(self.root, text="系统计算及风机选型\n进行系统计算和风机选型", command=self.open_system_calculation, width=button_width, height=button_height)
        self.system_button.pack()

        # 其他注意事项按钮
        self.other_button = tk.Button(self.root, text="其他注意事项\n注意事项", command=self.show_other_notes, width=button_width, height=button_height)
        self.other_button.pack()

    def open_permission_management(self):
        PermissionManagementWindow(self.root, self)

    def open_language_switch(self):
        LanguageSwitchWindow(self.root)

    def open_project_management(self):
        ProjectManagementWindow(self.root)

    def open_system_calculation(self):
        SystemCalculationWindow(self.root)

    def show_other_notes(self):
        # 此处可添加显示其他注意事项的具体逻辑，例如弹出一个包含注意事项信息的窗口
        pass

    def apply_permission_settings(self, permission_level):
        if permission_level == 1:
            self.permission_button.config(state=tk.NORMAL)
            self.language_button.config(state=tk.NORMAL)
            self.project_button.config(state=tk.DISABLED)
            self.system_button.config(state=tk.DISABLED)
            self.other_button.config(state=tk.DISABLED)
        elif permission_level == 2:
            self.permission_button.config(state=tk.NORMAL)
            self.language_button.config(state=tk.NORMAL)
            self.project_button.config(state=tk.NORMAL)
            self.system_button.config(state=tk.DISABLED)
            self.other_button.config(state=tk.DISABLED)
        elif permission_level == 3:
            self.permission_button.config(state=tk.NORMAL)
            self.language_button.config(state=tk.NORMAL)
            self.project_button.config(state=tk.NORMAL)
            self.system_button.config(state=tk.NORMAL)
            self.other_button.config(state=tk.NORMAL)


if __name__ == "__main__":
    root = tk.Tk()
    app = TunnelFanApp(root)
    root.mainloop()
