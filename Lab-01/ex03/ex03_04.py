def TruCapPhanTu(Tuple_Data):
    firstElement = Tuple_Data[0]
    lastElement  = Tuple_Data[-1]
    return firstElement,lastElement
input_Tuple = eval(input("Nhập Tuple, ví dụ (1,2,3):"))
first, last = TruCapPhanTu(input_Tuple)
print("Phần tử đầu tiên:", first)
print("Phần tử cuối cùng:",last)