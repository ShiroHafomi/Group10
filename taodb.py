import sqlite3


cursor = conn.cursor()

# Tạo bảng 'users' nếu chưa có
user_table = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        email TEXT NOT NULL
    )
'''

# Thực thi câu lệnh tạo bảng
cursor.execute(user_table)

# Hàm thêm người dùng vào cơ sở dữ liệu
def add_user(username, password, email):
    try:
        # Chuẩn bị câu lệnh SQL để chèn dữ liệu
        user_data = (username, password, email)
        cursor.execute('''
            INSERT INTO users (username, password, email) 
            VALUES (?, ?, ?)
        ''', user_data)

        # Commit các thay đổi và lưu vào cơ sở dữ liệu
        conn.commit()
        print(f"User {username} has been added successfully.")
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()

# Thêm một người dùng mới
add_user('tranvanphuoc', 'phuoc123', 'tranp9436@gmail.com')

# Kiểm tra xem thông tin đã được chèn thành công chưa
cursor.execute('SELECT * FROM users')
users = cursor.fetchall()
print("Users in the database:")
for user in users:
    print(user)

# Đóng kết nối
conn.close()
