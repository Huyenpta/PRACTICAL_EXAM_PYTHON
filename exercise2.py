import pandas as pd

data = {
    'id': ['SP01', 'SP02', 'SP03', 'SP04', 'SP05'],
    'name': ['Bàn phím cơ', 'Chuột không dây', 'Màn hình 24inch', 'Tai nghe Bluetooth', 'Cáp HDMI'],
    'price': [120, 45, 2000, 300, 150], 
    'quantity': [50, 120, 30, 80, 200]
}

df = pd.DataFrame(data)

df.to_csv('products.csv', index=False)
print("Đã lưu dữ liệu thành công ra file: 'products.csv'\n")

df_read = pd.read_csv('products.csv')

print("\n--- Tất cả sản phẩm ---")
print(df_read)

print("\n--- Sản phẩm có giá > 100 ---")
print(df_read[df_read['price'] > 100])

total_inventory_value = (df_read['price'] * df_read['quantity']).sum()
print(f"\nTổng giá trị hàng tồn kho: {total_inventory_value}")

df_read['total'] = df_read['price'] * df_read['quantity']
print("\n--- DataFrame sau khi thêm cột 'total' ---")
print(df_read)