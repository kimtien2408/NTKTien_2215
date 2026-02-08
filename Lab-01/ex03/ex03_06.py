def XoaPhanTu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False
MyDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}    
keyToDelete = 'b'
result = XoaPhanTu(MyDict, keyToDelete)
if result:
    print("Phần tử đã được xóa từ Dictionary:", MyDict)
else:
    print("Không tìm thấy phần tử cần xóa trong Dictionary!!")
