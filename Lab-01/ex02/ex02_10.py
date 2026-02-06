def DaoNguocChuoi(chuoi):
    return chuoi[::-1]
input_string = input("Mời nhập chuỗi cần đảo ngược: ")
print("Chuỗi đảo ngược là:",DaoNguocChuoi(input_string))