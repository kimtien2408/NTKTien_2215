import socket
import threading
from tkinter import *
from tkinter import scrolledtext
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad, unpad

class ChatClient:
    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        
        self.client_key = RSA.generate(2048)
        self.server_public_key = RSA.import_key(self.socket.recv(2048))
        self.socket.send(self.client_key.publickey().export_key(format='PEM'))
        
        encrypted_aes_key = self.socket.recv(2048)
        cipher_rsa = PKCS1_OAEP.new(self.client_key)
        self.aes_key = cipher_rsa.decrypt(encrypted_aes_key)

        # --- Giao diện Tkinter ---
        self.root = Tk()
        self.root.title("AES-RSA Secure Chat")
        
        self.chat_area = scrolledtext.ScrolledText(self.root, state='disabled', width=50, height=20)
        self.chat_area.pack(padx=10, pady=10)
        
        self.msg_entry = Entry(self.root, width=40)
        self.msg_entry.pack(side=LEFT, padx=10, pady=10)
        self.msg_entry.bind("<Return>", lambda event: self.send_message())
        
        self.send_btn = Button(self.root, text="Gửi", command=self.send_message)
        self.send_btn.pack(side=RIGHT, padx=10)

        # Luồng nhận tin
        threading.Thread(target=self.receive_messages, daemon=True).start()
        self.root.mainloop()

    def encrypt_message(self, message):
        cipher = AES.new(self.aes_key, AES.MODE_CBC)
        ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
        return cipher.iv + ciphertext

    def decrypt_message(self, encrypted_message):
        iv = encrypted_message[:AES.block_size]
        ciphertext = encrypted_message[AES.block_size:]
        cipher = AES.new(self.aes_key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(ciphertext), AES.block_size).decode()

    def send_message(self):
        msg = self.msg_entry.get()
        if msg:
            self.display_message(f"Bạn: {msg}")
            encrypted = self.encrypt_message(msg)
            self.socket.send(encrypted)
            self.msg_entry.delete(0, END)
            if msg == "exit":
                self.root.quit()

    def receive_messages(self):
        while True:
            try:
                data = self.socket.recv(1024)
                if data:
                    decrypted = self.decrypt_message(data)
                    self.display_message(f"Đối phương: {decrypted}")
            except:
                break

    def display_message(self, msg):
        self.chat_area.config(state='normal')
        self.chat_area.insert(END, msg + "\n")
        self.chat_area.config(state='disabled')
        self.chat_area.yview(END)

if __name__ == "__main__":
    ChatClient('localhost', 12345)