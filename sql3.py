import sqlite3

def create_and_initialize_permissions_database(db_path='permissions.db'):
    """
    创建权限数据库并初始化permissions表及默认权限。
    
    :param db_path: 数据库文件路径，默认为'permissions.db'
    """
    # 连接到SQLite数据库（如果数据库不存在，则会自动创建）
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 创建permissions表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS permissions (
            user_id INTEGER PRIMARY KEY,  -- 用户ID
            permission_level INTEGER NOT NULL  -- 权限级别
        )
    ''')

    # 初始化默认权限 - 假设我们有一些预定义的用户ID和他们的初始权限级别
    default_permissions = [
        (1, 3),  # 管理员用户，拥有最高权限
        (2, 2),  # 普通用户，可以使用所有功能但不能进行高级操作
        (3, 1)   # 受限用户，只能访问基本功能且不能使用某些功能
    ]

    # 插入或更新默认权限
    for user_id, permission_level in default_permissions:
        cursor.execute('''
            INSERT OR REPLACE INTO permissions (user_id, permission_level)
            VALUES (?, ?)
        ''', (user_id, permission_level))

    # 提交更改并关闭连接
    conn.commit()
    conn.close()

    print("权限数据库已成功创建或已存在，并初始化了默认权限。")

# 调用函数以创建数据库并初始化权限
create_and_initialize_permissions_database()