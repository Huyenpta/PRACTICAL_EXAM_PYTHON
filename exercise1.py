n = int(input("Nhập số lượng sinh viên: "))
students = []

for i in range(n):
    print(f"\nNhập thông tin sinh viên thứ {i+1}:")
    student_id = input("Mã sinh viên: ")
    full_name = input("Họ và tên: ")
    python_score = float(input("Điểm môn Python: "))
    
    student = {
        "id": student_id,
        "name": full_name,
        "score": python_score
    }
    students.append(student)

print("\n--- KẾT QUẢ ---")

print("Danh sách tất cả sinh viên:")
for s in students:
    print(f"Mã sinh viên: {s['id']}, Họ và tên: {s['name']}, Điểm Python: {s['score']}")

if students:
    max_student = max(students, key=lambda x: x['score'])
    print(f"Sinh viên có điểm cao nhất: {max_student['name']} ({max_student['score']})")

    avg_score = sum(s['score'] for s in students) / n
    print(f"Điểm trung bình: {avg_score:.2f}")

    passed_students = [s['name'] for s in students if s['score'] >= 5]
    print("Danh sách sinh viên thi đỗ (score >= 5):", passed_students)