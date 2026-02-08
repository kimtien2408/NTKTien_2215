def DemSoLanXuatHien(lst):
    countDict = {}
    for item in lst:
        if item in countDict:
            countDict[item]+=1
        else:
            countDict[item]=1
    return countDict
inputString = input("Nhập Danh sách các từ, cách nhau bằng dấu cách:")
wordList = inputString.split()
SoLanXuatHien = DemSoLanXuatHien(wordList)
print("Số lần xuất hiện của các phần tử:", SoLanXuatHien)