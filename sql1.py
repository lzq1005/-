import sqlite3

# 连接到SQLite数据库
conn = sqlite3.connect('fan_models.db')
# 创建一个游标对象，用于执行SQL语句
cursor = conn.cursor()

# 定义40组风机数据
fan_data = [
('AL 12-750', 10000, 18500, 7.5, 1200),
    ('AL10 - 350B', 9000, 12000, 4.0, 1000),
    ('AL11 - 400C', 10500, 11000, 4.5, 1100),
    ('AL11 - 450D', 9100, 18000, 5.0, 1100),
    ('AL12 - 500E', 8500, 20000, 5.5, 1200),
    ('AL12 - 550F', 87500, 22000, 6.0, 1200),
    ('AL13 - 600G', 14000, 14000, 6.5, 1300),
    ('AL13 - 650H', 15000, 15000, 7.0, 1300),
    ('AL14 - 700I', 16000, 17500, 7.5, 1400),
    ('AL14 - 750J', 7000, 32000, 8.0, 1400),
    ('AL15 - 800K', 8000, 35000, 8.5, 1500),
    ('AL15 - 850L', 9000, 38000, 9.0, 1500),
    ('AL16 - 900M', 9500, 40000, 9.5, 1600),
    ('AL16 - 950N', 21000, 17000, 10.0, 1600),
    ('BL10 - 300O', 7500, 10000, 3.2, 1000),
    ('BL10 - 350P', 8500, 14000, 3.8, 1000),
    ('BL11 - 400Q', 9500, 14400, 4.2, 1100),
    ('BL11 - 450R', 10500, 16500, 4.8, 1100),
    ('BL12 - 500S', 11500, 17900, 5.2, 1200),
    ('BL12 - 550T', 12500, 21000, 5.8, 1200),
    ('BL13 - 600U', 3500, 24000, 6.2, 1300),
    ('BL13 - 650V', 4500, 26000, 6.8, 1300),
    ('BL14 - 700W', 5500, 29000, 7.2, 1400),
    ('BL14 - 750X', 6500, 31000, 7.8, 1400),
    ('BL15 - 800Y', 7500, 34000, 8.2, 1500),
    ('BL15 - 850Z', 8500, 36000, 8.8, 1500),
    ('CL10 - 300AA', 7000, 7200, 3.0, 1000),
    ('CL10 - 350BB', 8000, 10800, 3.6, 1000),
    ('CL11 - 400CC', 9000, 11000, 4.0, 1100),
    ('CL11 - 450DD', 10000, 14000, 4.6, 1100),
    ('CL12 - 500EE', 11000, 17000, 5.0, 1200),
    ('CL12 - 550FF', 12000, 8000, 5.6, 1200),
    ('CL13 - 600GG', 3000, 22000, 6.0, 1300),
    ('CL13 - 650HH', 4000, 24000, 6.6, 1300),
    ('CL14 - 700II', 5000, 27000, 7.0, 1400),
    ('CL14 - 750JJ', 6000, 29000, 7.6, 1400),
    ('DL10 - 300KK', 6500, 4000, 2.8, 1000),
    ('DL10 - 350LL', 7500, 20000, 3.4, 1000),
    ('DL11 - 400MM', 8500, 30000, 3.8, 1100),
    ('DL11 - 450NN', 9500, 50000, 4.4, 1100)
]

# 创建表（如果表不存在）
cursor.execute('''
CREATE TABLE IF NOT EXISTS fan_models (
    model_name TEXT,
    rated_pressure INTEGER,
    rated_flow INTEGER,
    motor_power REAL,
    motor_speed INTEGER
)
''')

# 插入数据的SQL语句
insert_sql = '''
INSERT INTO fan_models (model_name, rated_pressure, rated_flow, motor_power, motor_speed)
VALUES (?,?,?,?,?)
'''

# 使用executemany方法插入多条数据
cursor.executemany(insert_sql, fan_data)

# 提交事务
conn.commit()

# 关闭游标
cursor.close()

# 关闭数据库连接
conn.close()

print("40组风机型号数据已成功插入数据库。")