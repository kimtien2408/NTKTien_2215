from SinhVien import SinhVien
class QuanLySinhVien:
    listSinhVien =[]
    def generateID(self):
        MaxID = 1
        if(self.SoLuongSinhVien()> 0):
            MaxID = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if (MaxID < sv._id):
                    MaxID = sv._id
            MaxID = MaxID +1
        return MaxID
    
    def SoLuongSinhVien(self):
        return self.listSinhVien.__len__()
    
    def NhapSinhVien(self):
        SVID = self.generateID()
        name = input("Nhập tên sinh viên: ")
        sex = input("Nhập giới tính sinh viên: ")
        major = input("Nhập chuyên ngành của sinh viên: ")
        DiemTB = float(input("Nhập điểm trung bình của sinh viên: "))
        sv = SinhVien(SVID, name, sex, major, DiemTB )
        self.XepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)
        
    def UpdateSinhVien(self,ID):
        sv:SinhVien = self.findByID(ID)
        if(sv != None):
            name = input("Nhập tên sinh viên: ") 
            sex = input("Nhập giới tính sinh viên: ")
            major = int(input("Nhập chuyên ngành của sinh viên: "))
            DiemTB = float(input("Nhập điểm trung bình của sinh viên: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._DiemTB = DiemTB
            self.XepLoaiHocLuc(sv)
        else:
            print("Sinh viên có ID = {} không tồn tại.".format(ID))
            
    def SortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse= False)
        
    def SortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name, reverse= False)
        
    def SortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._DiemTB, reverse= False)
        
    def findByID(self,ID):
        searchResult = None
        if(self.SoLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (sv._id == ID):
                    searchResult = sv
        return searchResult
    
    def findByName(self, keyword):
        listSV = []
        if(self.SoLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if(keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV
    
    def deleteByID(self, ID):
        isDeleted = False
        sv = self.findByID(ID)
        if(sv != None):
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted
    
    def XepLoaiHocLuc (self, sv:SinhVien):
        if (sv._DiemTB >= 8):
            sv._HocLuc ="Giỏi"
        elif (sv._DiemTB >=6.5):
            sv._HocLuc = "Khá"
        elif (sv._DiemTB >=5):
            sv._HocLuc = "Trung Bình"
        else:
            sv._HocLuc = "Yếu"
            
    def ShowSinhVien(self,listSV):
        print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} "
              .format ("ID","Name", "Sex", "Major", "DiemTB", "HocLuc"))
        if(listSV.__len__() > 0):
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} "
                    .format(sv._id, sv._name, sv._sex, sv._major, sv._DiemTB, sv._HocLuc))
        print("\n")   
        
    def getListSinhVien(self):
        return self.listSinhVien
        