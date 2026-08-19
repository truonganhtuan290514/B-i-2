ten = input("Nhap ten hoc sinh: ")
toan = float(input("Nhap diem Toan: "))
van = float(input("Nhap diem Van: "))

diem_tb = (toan + van) / 2

print("Ten hoc sinh:", ten)
print("Diem trung binh:", diem_tb)

anh = float(input("Nhap diem Anh: "))

diem_tb = (toan + van + anh) / 3

print("Diem trung binh 3 mon:", diem_tb)

if diem_tb >= 8:
    xep_loai = "Gioi"
elif diem_tb >= 6.5:
    xep_loai = "Kha"
elif diem_tb >= 5:
    xep_loai = "Trung binh"
else:
    xep_loai = "Yeu"

print("Xep loai:", xep_loai)