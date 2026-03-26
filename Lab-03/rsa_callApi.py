import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from Ui.rsa import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Mapping buttons theo đúng Object Name trong hình ảnh
        self.ui.btnKey.clicked.connect(self.call_api_gen_keys)   # Nút "Generate Keys"
        self.ui.btnEncrypt.clicked.connect(self.call_api_encrypt) # Nút "Encrypt"
        self.ui.btnDecrypt.clicked.connect(self.call_api_decrypt) # Nút "Decrypt"
        self.ui.btnSign.clicked.connect(self.call_api_sign)       # Nút "Sign"
        self.ui.btnVeri.clicked.connect(self.call_api_verify)     # Nút "Verify" (btnVeri)

    def call_api_gen_keys(self):
        url = "http://127.0.0.1:5020/api/rsa/generate_keys"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                QMessageBox.information(self, "Thông báo", data.get("message", "Đã tạo key!"))
            else:
                print(f"Error: Status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Connection Error: {e}")

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5020/api/rsa/encrypt"
        # PlainText -> txtplain
        payload = {
            "message": self.ui.txtplain.toPlainText(),
            "key_type": "public"
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                # CipherText -> txtCipher
                self.ui.txtCipher.setPlainText(data["encrypted_message"])
                QMessageBox.information(self, "Thông báo", "Mã hóa thành công!")
        except Exception as e:
            print(f"Error: {e}")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5020/api/rsa/decrypt"
        # Lấy từ txtCipher trả về txtplain
        payload = {
            "ciphertext": self.ui.txtCipher.toPlainText(),
            "key_type": "private"
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txtplain.setPlainText(data["decrypted_message"])
                QMessageBox.information(self, "Thông báo", "Giải mã thành công!")
        except Exception as e:
            print(f"Error: {e}")

    def call_api_sign(self):
        url = "http://127.0.0.1:5020/api/rsa/sign"
        # Information -> txtInfor
        payload = {"message": self.ui.txtInfor.toPlainText()}
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                # Signature -> txtSign
                self.ui.txtSign.setPlainText(data["signature"])
                QMessageBox.information(self, "Thông báo", "Ký số thành công!")
        except Exception as e:
            print(f"Error: {e}")

    def call_api_verify(self):
        url = "http://127.0.0.1:5020/api/rsa/verify"
        payload = {
            "message": self.ui.txtInfor.toPlainText(),
            "signature": self.ui.txtSign.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                result = "Xác thực THÀNH CÔNG" if data.get("is_verified") else "Xác thực THẤT BẠI"
                QMessageBox.information(self, "Kết quả xác thực", result)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())