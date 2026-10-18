import random
#1
print("Chào mừng bạn đến với chương trình này ")
Do_dai_mat_Khau=int(input("Nhập độ dài mật khẩu: "))
Co_muon_bao_gom_chu_hoa=input("Có muốn bao gồm chữ hoa (Y/N) ")
Co_muon_bao_gom_chu_thuong=input("Có muốn bao gồm chữ số (Y/N) ")
Co_muon_ki_tu_dac_biet=input("Có muốn bao gồm ký tự đặc biệt (Y/N) ")
password=""
if Co_muon_bao_gom_chu_hoa.upper()=="Y":
    password+=random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
if Co_muon_bao_gom_chu_thuong.upper()=="Y":
    password+=random.choice("abcdefghijklmnopqrstuvwxyz")
if Co_muon_ki_tu_dac_biet.upper()=="Y":
    password+=random.choice("!@#$%^&*")
    while len(password)<Do_dai_mat_Khau:
        if Co_muon_bao_gom_chu_hoa.upper()=="Y":
            password+=random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        if Co_muon_bao_gom_chu_thuong.upper()=="Y":
            password+=random.choice("abcdefghijklmnopqrstuvwxyz")
        if Co_muon_ki_tu_dac_biet.upper()=="Y":
            password+=random.choice("!@#$%^&*")
password_list=list(password)
random.shuffle(password_list)
print(f"Mật khẩu được tạo là: {''.join(password_list)}")
#2
print("="*40)
print("     TRÌNH TẠO MẬT KHẨU NGẪU NHIÊN ")
print("="*40)
MK=int(input("Nhập độ dài mật khẩu: "))
Co_Chu_hoa_ko=input("Có muốn bao gồm chữ hoa (Y/N) ")
Co_Chu_so_ko=input("Có muốn bao gồm chữ số (Y/N) ")
Co_ky_tu_dac_biet_ko=input("Có muốn bao gồm ký tự đặc biệt (Y/N) ")
mk_moi=""
if Co_Chu_hoa_ko.upper()=="Y":
    mk_moi+=random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
if Co_Chu_so_ko.upper()=="Y":
    mk_moi+=random.choice("abcdefghijklmnopqrstuvwxyz")
if Co_ky_tu_dac_biet_ko.upper()=="Y":
    mk_moi+=random.choice("!@#$%^&*")
    while len(mk_moi)<MK:
        if Co_Chu_hoa_ko.upper()=="Y":
            mk_moi+=random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        if Co_Chu_so_ko.upper()=="Y":
            mk_moi+=random.choice("abcdefghijklmnopqrstuvwxyz")
        if Co_ky_tu_dac_biet_ko.upper()=="Y":
            mk_moi+=random.choice("!@#$%^&*")
mk_moi_list=list(mk_moi)
random.shuffle(mk_moi_list)
print(f"Mật khẩu được tạo là: {''.join(mk_moi_list)}")
#3
chu_thuong = "abcdefghijklmnopqrstuvwxyz"
chu_hoa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chu_so = "0123456789"
dac_biet = "!@#$%^&*()_+"
kho = chu_thuong
if input("Có muốn bao gồm chữ hoa (Y/N): ").lower() == "y":
    kho += chu_hoa
if input("Có muốn bao gồm chữ số (Y/N): ").lower() == "y":
    kho += chu_so
if input("Có muốn bao gồm ký tự đặc biệt (Y/N): ").lower() == "y":
    kho += dac_biet
N = int(input("Nhập độ dài mật khẩu: "))
MKM = ""
for i in range(N):
    MKM += random.choice(kho)
print("Mật khẩu ngẫu nhiên là:", MKM)
#return la tra lai