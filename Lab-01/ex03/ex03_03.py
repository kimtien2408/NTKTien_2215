def TaoTupleTuList(lst):
    return tuple[lst]
inputlist = input("Nhập danh sách các số, cách nhau bằng dấu phẩy:")
numbers = list(map(int,inputlist.split(',')))
MyTuple = TaoTupleTuList(numbers)
print("List: ",numbers)
print("Tuple lấy từ List: ", MyTuple)
