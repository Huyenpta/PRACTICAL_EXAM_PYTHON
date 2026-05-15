import random

import pandas as pd
from sqlalchemy import create_engine,text

db = "mysql+pymysql://root:@localhost:3306/t2507e"
engine = create_engine(db)

query = "SELECT * FROM students"
df = pd.read_sql(query,engine)

print(df)

df.to_csv("students.csv",index=False)

df2 = pd.read_csv("schools.csv")
df2.to_sql(
    name="schools",
    con= engine,
    if_exists="replace", #append
    index=False
)

insert_sql = text("INSERT INTO students(name,dob,mark,group_id) values('Tien Anh','2010-09-19',8,1)")
#conn = engine.connect()
with engine.connect() as conn:
    conn.execute(insert_sql)
    conn.commit()


# DB có bảng users(id,name,email,salary)
# yêu cầu:
# 1. Tao 1 file users.csv có 20 người theo thông tin trên
# 2. Nạp dữ liệu vào db- table: users
# 3. THêm 1 column: net_salary
# 4. Tính dữ liệu vào net_salary (giar sử net = salary-10%)
# 5. Xuất dữ liệu mới ra csv

data = []
for i in range(1, 21):
    data.append({
        "id": i,
        "name": f"User {i}",
        "email": f"user{i}@gmail.com",
        "salary": random.randint(5000, 20000)
    })

df = pd.DataFrame(data)
df.to_csv("users.csv", index=False)


df.to_sql("users", con=engine, if_exists="replace", index=False)


with engine.connect() as conn:
    conn.execute(text("ALTER TABLE users ADD COLUMN net_salary FLOAT"))
    conn.commit()


with engine.connect() as conn:
    conn.execute(text("UPDATE users SET net_salary = salary * 0.9"))
    conn.commit()


df_new = pd.read_sql("SELECT * FROM users", engine)
df_new.to_csv("users_updated.csv", index=False)
