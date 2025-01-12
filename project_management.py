import tkinter as tk
import sqlite3
from tkinter import messagebox


class ProjectManagementWindow:
    def __init__(self, master):
        self.master = master
        self.window = tk.Toplevel(master)
        self.window.title("项目管理")
        self.window.geometry("800x600")

        # 连接到项目数据库（如果不存在则创建）
        self.conn = sqlite3.connect('projects.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                company_name TEXT,
                contact_name TEXT,
                contact_phone TEXT,
                project_name TEXT,
                project_location TEXT
            )
        ''')

        # 项目管理模块标题
        self.title_label = tk.Label(self.window, text="项目管理模块", font=("Arial", 16))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # 操作按钮
        self.new_project_button = tk.Button(self.window, text="新建项目", command=self.new_project_prompt)
        self.new_project_button.grid(row=1, column=0, padx=10, pady=10, sticky=tk.N + tk.S)

        self.delete_project_button = tk.Button(self.window, text="删除项目", command=self.delete_project)
        self.delete_project_button.grid(row=2, column=0, padx=10, pady=10, sticky=tk.N + tk.S)

        self.open_project_button = tk.Button(self.window, text="打开项目", command=self.open_project)
        self.open_project_button.grid(row=3, column=0, padx=10, pady=10, sticky=tk.N + tk.S)

        self.copy_project_button = tk.Button(self.window, text="复制项目", command=self.copy_project)
        self.copy_project_button.grid(row=4, column=0, padx=10, pady=10, sticky=tk.N + tk.S)

        self.view_projects_button = tk.Button(self.window, text="查看项目", command=self.view_projects)
        self.view_projects_button.grid(row=5, column=0, padx=10, pady=10, sticky=tk.N + tk.S)

        # 项目列表框
        self.project_listbox = tk.Listbox(self.window)
        self.project_listbox.grid(row=1, column=1, rowspan=5, padx=10, pady=10, sticky=tk.N + tk.S + tk.E + tk.W)
        self.scrollbar = tk.Scrollbar(self.window, orient=tk.VERTICAL, command=self.project_listbox.yview)
        self.scrollbar.grid(row=1, column=2, rowspan=5, padx=0, pady=10, sticky=tk.N + tk.S)
        self.project_listbox.config(yscrollcommand=self.scrollbar.set)
        self.update_project_listbox()

    def new_project_prompt(self):
        new_project_window = tk.Toplevel(self.window)
        new_project_window.title("新建项目")

        # 项目信息输入框
        company_name_label = tk.Label(new_project_window, text="甲方公司名称：")
        company_name_label.pack()
        company_name_entry = tk.Entry(new_project_window)
        company_name_entry.pack()

        contact_name_label = tk.Label(new_project_window, text="甲方联系人：")
        contact_name_label.pack()
        contact_name_entry = tk.Entry(new_project_window)
        contact_name_entry.pack()

        contact_phone_label = tk.Label(new_project_window, text="甲方联系人电话：")
        contact_phone_label.pack()
        contact_phone_entry = tk.Entry(new_project_window)
        contact_phone_entry.pack()

        project_name_label = tk.Label(new_project_window, text="项目名称：")
        project_name_label.pack()
        project_name_entry = tk.Entry(new_project_window)
        project_name_entry.pack()

        project_location_label = tk.Label(new_project_window, text="项目地点：")
        project_location_label.pack()
        project_location_entry = tk.Entry(new_project_window)
        project_location_entry.pack()

        save_button = tk.Button(new_project_window, text="保存项目", command=lambda: self.new_project(
            company_name_entry.get(),
            contact_name_entry.get(),
            contact_phone_entry.get(),
            project_name_entry.get(),
            project_location_entry.get()
        ))
        save_button.pack()

    def new_project(self, company_name, contact_name, contact_phone, project_name, project_location):
        if all([company_name, project_name, project_location]):
            self.cursor.execute('''
                INSERT INTO projects (company_name, contact_name, contact_phone, project_name, project_location)
                VALUES (?,?,?,?,?)
            ''', (company_name, contact_name, contact_phone, project_name, project_location))
            self.conn.commit()
            tk.messagebox.showinfo("操作成功", f"项目 {project_name} 已创建")
        else:
            tk.messagebox.showerror("错误", "项目名称和项目地点不能为空。")

    def delete_project(self):
        selected_index = self.project_listbox.curselection()
        if selected_index:
            selected_project_name = self.project_listbox.get(selected_index)
            self.cursor.execute('DELETE FROM projects WHERE project_name =?', (selected_project_name,))
            self.conn.commit()
            tk.messagebox.showinfo("操作成功", f"项目 {selected_project_name} 已删除")
            self.update_project_listbox()
        else:
            tk.messagebox.showerror("错误", "请选择要删除的项目。")

    def open_project(self):
        selected_index = self.project_listbox.curselection()
        if selected_index:
            selected_project_name = self.project_listbox.get(selected_index)
            self.cursor.execute('SELECT * FROM projects WHERE project_name =?', (selected_project_name,))
            project = self.cursor.fetchone()
            if project:
                self.open_project_edit_window(project)
            else:
                tk.messagebox.showerror("错误", f"未找到项目 {selected_project_name}")
        else:
            tk.messagebox.showerror("错误", "请选择要打开的项目。")

    def open_project_edit_window(self, project):
        edit_window = tk.Toplevel(self.window)
        edit_window.title(f"编辑项目 - {project[4]}")

        self.id = project[0]
        self.company_name_var = tk.StringVar(value=project[1])
        self.contact_name_var = tk.StringVar(value=project[2])
        self.contact_phone_var = tk.StringVar(value=project[3])
        self.project_name_var = tk.StringVar(value=project[4])
        self.project_location_var = tk.StringVar(value=project[5])

        company_name_label = tk.Label(edit_window, text="甲方公司名称：")
        company_name_label.pack()
        company_name_entry = tk.Entry(edit_window, textvariable=self.company_name_var)
        company_name_entry.pack()

        contact_name_label = tk.Label(edit_window, text="甲方联系人：")
        contact_name_label.pack()
        contact_name_entry = tk.Entry(edit_window, textvariable=self.contact_name_var)
        contact_name_entry.pack()

        contact_phone_label = tk.Label(edit_window, text="甲方联系人电话：")
        contact_phone_label.pack()
        contact_phone_entry = tk.Entry(edit_window, textvariable=self.contact_phone_var)
        contact_phone_entry.pack()

        project_name_label = tk.Label(edit_window, text="项目名称：")
        project_name_label.pack()
        project_name_entry = tk.Entry(edit_window, textvariable=self.project_name_var)
        project_name_entry.pack()

        project_location_label = tk.Label(edit_window, text="项目地点：")
        project_location_label.pack()
        project_location_entry = tk.Entry(edit_window, textvariable=self.project_location_var)
        project_location_entry.pack()

        save_button = tk.Button(edit_window, text="保存修改", command=self.save_project_changes)
        save_button.pack()

    def save_project_changes(self):
        company_name = self.company_name_var.get()
        contact_name = self.contact_name_var.get()
        contact_phone = self.contact_phone_var.get()
        project_name = self.project_name_var.get()
        project_location = self.project_location_var.get()

        if all([company_name, project_name, project_location]):
            self.cursor.execute('''
                UPDATE projects
                SET company_name =?, contact_name =?, contact_phone =?, project_name =?, project_location =?
                WHERE id =?
            ''', (company_name, contact_name, contact_phone, project_name, project_location, self.id))
            self.conn.commit()
            tk.messagebox.showinfo("操作成功", f"项目 {project_name} 已保存")
        else:
            tk.messagebox.showerror("错误", "项目名称和项目地点不能为空。")

    def copy_project(self):
        selected_index = self.project_listbox.curselection()
        if selected_index:
            selected_project_name = self.project_listbox.get(selected_index)
            self.cursor.execute('SELECT * FROM projects WHERE project_name =?', (selected_project_name,))
            project = self.cursor.fetchone()
            if project:
                new_project_name = selected_project_name + "_copy"
                self.cursor.execute('''
                    INSERT INTO projects (company_name, contact_name, contact_phone, project_name, project_location)
                    VALUES (?,?,?,?,?)
                ''', (project[1], project[2], project[3], new_project_name, project[5]))
                self.conn.commit()
                tk.messagebox.showinfo("操作成功", f"项目 {selected_project_name} 已复制为 {new_project_name}")
            else:
                tk.messagebox.showerror("错误", f"未找到项目 {selected_project_name}")
        else:
            tk.messagebox.showerror("错误", "请选择要复制的项目。")

    def get_project_name(self):
        project_name_window = tk.Toplevel(self.window)
        project_name_window.title("输入项目名称")

        project_name_label = tk.Label(project_name_window, text="请输入项目名称：")
        project_name_label.pack()
        project_name_entry = tk.Entry(project_name_window)
        project_name_entry.pack()

        ok_button = tk.Button(project_name_window, text="确定", command=lambda: project_name_window.destroy())
        ok_button.pack()

        project_name_window.wait_window()
        return project_name_entry.get()

    def view_projects(self):
        self.cursor.execute('SELECT * FROM projects')
        projects = self.cursor.fetchall()
        if projects:
            project_info = ""
            for project in projects:
                project_info += (
                    f"ID: {project[0]}\n"
                    f"甲方公司名称: {project[1]}\n"
                    f"甲方联系人: {project[2]}\n"
                    f"甲方联系人电话: {project[3]}\n"
                    f"项目名称: {project[4]}\n"
                    f"项目地点: {project[5]}\n\n"
                )
            tk.messagebox.showinfo("项目列表", project_info)
        else:
            tk.messagebox.showinfo("提示", "没有项目记录。")

    def update_project_listbox(self):
        self.cursor.execute('SELECT project_name FROM projects')
        projects = self.cursor.fetchall()
        self.project_listbox.delete(0, tk.END)
        for project in projects:
            self.project_listbox.insert(tk.END, project[0])


if __name__ == "__main__":
    root = tk.Tk()
    app = ProjectManagementWindow(root)
    root.mainloop()