import sqlite3

# 连接到 SQLite 数据库
# 如果数据库不存在，将会在指定路径创建一个数据库文件
conn = sqlite3.connect('project_management.db')

# 创建一个 cursor 对象，用于执行 SQL 语句
cursor = conn.cursor()

# 创建 projects 表的 SQL 语句
create_table_sql = '''
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT NOT NULL,
    contact_name TEXT NOT NULL,
    contact_phone TEXT NOT NULL,
    project_name TEXT NOT NULL,
    project_location TEXT NOT NULL
);
'''

# 执行 SQL 语句创建表
cursor.execute(create_table_sql)

# 提交事务
conn.commit()

# 关闭 cursor 和连接
cursor.close()
conn.close()

print("项目管理数据库和表已成功创建。")
