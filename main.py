ten = input("Nhap ten hoc sinh: ")
toan = float(input("Nhap diem Toan: "))
van = float(input("Nhap diem Van: "))
anh = float(input("Nhap diem Anh: "))

diem_tb = (toan + van + anh) / 3

if diem_tb >= 8:
    xep_loai = "Gioi"
elif diem_tb >= 6.5:
    xep_loai = "Kha"
elif diem_tb >= 5:
    xep_loai = "Trung binh"
else:
    xep_loai = "Yeu"

print("Hoc sinh:", ten)
print("Diem Toan:", toan)
print("Diem Van:", van)
print("Diem Anh:", anh)
print("Diem trung binh:", round(diem_tb, 2))
print("Xep loai:", xep_loai)