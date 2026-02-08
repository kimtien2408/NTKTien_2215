def DaoNguocList(lst):
    return lst[::-1]
input_List = input("Nhập danh sách các số , cách nhau bằng dấu phẩy: ")
numbers= list(map(int,input_List.split(',')))
ListDaoNguoc =DaoNguocList(numbers)
print("List sau khi đảo ngược:",ListDaoNguoc)