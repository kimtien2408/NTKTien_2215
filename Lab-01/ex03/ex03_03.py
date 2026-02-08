def TaoTupleTuLisst(lst):
    return tuple[::-1]
inputlist = input("Nhập danh sách các số, cách nhau bằng dấu phẩy:")
numbers = list(map(int,inputlist.split(',')))
MyTuple = TaoTupleTuLisst(numbers)
print("List: ",numbers)
print("Tuple từ List: ", MyTuple)
