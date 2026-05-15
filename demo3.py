import pandas as pd

df = pd.read_csv("students.csv")
# df: DataFrame (giong 1 table trong SQL)

print(df["name"][0])
#sua diem thi cho ai duoi 25 tuoi
df.loc[df["age"]<25,"mark"] = df["mark"]+1
new_df = pd.DataFrame([
    {"name":"Quoc","age":23,"mark":8},
    {"name":"Dat","age":28,"mark":7},
    {"name":"Kiet","age":20,"mark":6},
])
df = pd.concat([df,new_df],ignore_index=True)

#luu lai vao file
df.to_csv("students.csv", index=False)

print(df)

#Xây dựng file dữ liệu sản phẩm
#ID name, price, description image, catagory, qty
#tìm những sản phẩm qty=0
#những sản phẩn price > 100000
#ghi file mới sau khi lọc dữ liệu

df = pd.read_csv("products.csv")

print(df["ID_name"][0])

new_df = pd.DataFrame([
    {"ID_name":"SP01","price":1000000,"description_image":"image01.jpg","catagory":"Phone","qty":2},
    {"ID_name":"SP01","price":1000000,"description_image":"image01.jpg","catagory":"Phone","qty":2},
    {"ID_name":"SP01","price":1000000,"description_image":"image01.jpg","catagory":"Phone","qty":2},
])
print(df)

resulf = df[(df["qty"] ==0)]
print(resulf)
resulf1= df[(df["price"]>100000)]
print(resulf1)

resulf1.to_csv("products.csv", index=False)
