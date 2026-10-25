#bai1
import random
name=input("Nhập tên của bạn:")
age=int(input("Nhập tuổi của bạn: "))
high=float(input("Nhập chiều cao của bạn: "))
co_di_hoc_hay_khong=input("Bạn có đi học hay không (Y/N): ")=="Y"
print(type(name))
print(type(age))
print(type(high))
print(type(co_di_hoc_hay_khong))
#Trong các tên sau, tên nào hợp lệ và tên nào sai? Giải thích lý do, rồi sửa lại các tên sai cho đúng quy tắc Python:
# 2diem, ho_ten, tong tien, class, diemTB, so-luong
#bai2
#2diem sai vì bắt đầu bằng số, sửa thành diem2
#ho_ten đúng vì bắt đầu bằng chữ cái và có dấu gạch dưới
#tong tien sai vì không có dấu gạch dưới,sửa thành tong_tien
#class sai vì class là từ khóa của Python,sửa thành lop_hoc
#diemTB đúng vì bắt đầu bằng chữ cái và chỉ chứa chữ cái
#so-luong sai vì dấu gạch ngang - không được dùng trong tên biến,sửa thành: so_luong
#bai3
a=17
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
n = float(input("Nhap mot so: "))
if n % 2 == 0:
    print("So chan")
else:
    print("So le")
#bai4
print("a", "b", "c", sep="-")
print("Xin chào!", end="")
print("Tạm biệt!")
print("2025", "10", "25", sep="/")
#bai5
a = input("Nhập họ tên của bạn: ")
b = int(input("Nhập tuổi của bạn: "))
print(f"Xin chào {a}! Sang năm bạn {b} tuổi")
#phần mở rộng
dai = float(input("Nhập chiều dài: "))
rong = float(input("Nhập chiều rộng: "))
chu_vi = (dai + rong) * 2
dien_tich = dai * rong
print("Chu vi là:", chu_vi)
print("Diện tích là:", dien_tich)
#bai6
chuoi = "Python"
print(chuoi[0], chuoi[-1])
print(chuoi[:3])
print(chuoi[::-1])
print(chuoi, chuoi, chuoi, sep="-")
#bai7
toan = float(input("Nhập điểm Toán: "))
van = float(input("Nhập điểm Văn: "))
print("Cả hai môn đều >= 5:", toan>= 5 and van >=5)
print("Có ít nhất một môn >= 8:", toan>= 8 or van>= 8)
print("Có bị điểm liệt:", toan<3 or van<3)
print("Học sinh giỏi:", (toan+van) / 2>= 8 and not (toan <6 or van<6))
#bai8
hoten = input("Nhập họ tên: ").strip()
print(hoten.upper())
print(hoten.lower())
print(len(hoten))
print(f'Họ tên "{hoten.upper()}" có {len(hoten)} ký tự')
#bai9
#lower chuyển chữ hoa thành thường
#strip là cắt bớt khoàng trắng dư thừa
noname = input("Nhập họ tên đầy đủ: ").strip()
cac_tu = noname.split()
ho = cac_tu[0]
ten = cac_tu[-1]
tendangnhap =ho[:3].lower() + ten[::-1].lower() + str(random.randint(10, 99))
print(f"Tên đăng nhập của bạn là: {tendangnhap}")
#bai10
chu_thuong = "abcdefghijklmnopqrstuvwxyz"
chu_hoa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chu_so = "0123456789"
ky_tu_dac_biet = "!@#$%&*"
tat_ca = chu_thuong + chu_hoa + chu_so + ky_tu_dac_biet
mK = int(input("Nhập độ dài mật khẩu: "))

if mK < 8:
    print("Lỗi: Mật khẩu phải có ít nhất 8 ký tự!")
else:
    matkhau = [
        random.choice(chu_thuong),
        random.choice(chu_hoa),
        random.choice(chu_so),
        random.choice(ky_tu_dac_biet)
    ]
    for i in range(mK - 4):
        matkhau.append(random.choice(tat_ca))
    random.shuffle(matkhau)
    matkhau = "".join(matkhau)
    print(f"Mật khẩu của bạn ({mK} ký tự): {matkhau}")