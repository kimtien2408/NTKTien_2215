from flask import Flask, render_template, request, json
from Cipher.Caesar import CaesarCipher
from Cipher.Vigenere import VigenereCipher
from Cipher.Railfence import RailfenceCipher
from Cipher.Playfair import PlayFairCipher
from Cipher.Transposition import TranspositionCipher
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

#CAESAR
#Route Trang 

@app.route("/caesar")
def caesar():
    return render_template("caesar.html")

@app.route("/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    text = request.form['inputPlainText'] 
    key = int(request.form['inputKeyPlain']) 

    caesar = CaesarCipher()
    encrypted_text = caesar.caesar_encrypt(text, key)
    
    return render_template("caesar.html", encrypted_text=encrypted_text)

@app.route("/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    text = request.form['inputCipherText'] 
    key = int(request.form['inputKeyCipher'])

    caesar = CaesarCipher()
    decrypted_text = caesar.caesar_decrypt(text, key)

    return render_template("caesar.html", decrypted_text=decrypted_text)#



#VIGENERE
#Route Trang

@app.route("/vigenere")
def vigenere():
    return render_template("vigenere.html")


@app.route("/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():

    text = request.form['inputPlainText'] 
    key = request.form['inputKeyPlain']

    vigenere = VigenereCipher()
    encrypted_text = vigenere.vigenere_encrypt(text, key)

    return render_template("vigenere.html",encrypted_text=encrypted_text)
    
@app.route("/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():

    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']

    vigenere = VigenereCipher()
    decrypted_text = vigenere.vigenere_decrypt(text, key)

    return render_template("vigenere.html",decrypted_text=decrypted_text)


#RAILFENCE
#Route Trang

@app.route("/railfence")
def railfence():
    return render_template("railfence.html")

@app.route("/railfence/encrypt", methods=["POST"])
def railfence_encrypt():

    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])

    railfence = RailfenceCipher()
    encrypted_text = railfence.rail_fence_encrypt(text, key)

    return render_template("railfence.html", encrypted_text=encrypted_text)


@app.route("/railfence/decrypt", methods=["POST"])
def railfence_decrypt():

    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])

    railfence = RailfenceCipher()
    decrypted_text = railfence.rail_fence_decrypt(text, key)

    return render_template("railfence.html", decrypted_text=decrypted_text)


#PLAYFAIR
#Route Trang

@app.route("/playfair")
def playfair():
    return render_template("playfair.html")


@app.route("/playfair/encrypt", methods=["POST"])
def playfair_encrypt():

    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']

    playfair = PlayFairCipher()

    matrix = playfair.create_playfair_matrix(key)   
    encrypted_text = playfair.playfair_encrypt(text, matrix)

    return render_template("playfair.html", encrypted_text=encrypted_text)

@app.route("/playfair/decrypt", methods=["POST"])
def playfair_decrypt():

    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']

    playfair = PlayFairCipher()

    matrix = playfair.create_playfair_matrix(key) 
    decrypted_text = playfair.playfair_decrypt(text, matrix)

    return render_template("playfair.html", decrypted_text=decrypted_text)



#TRANSPOSITION

@app.route("/transposition")
def transposition():
    return render_template("transposition.html")


@app.route("/transposition/encrypt", methods=["POST"])
def transposition_encrypt():

    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])

    transposition = TranspositionCipher()
    encrypted_text = transposition.transposition_encrypt(text, key)

    return render_template("transposition.html", encrypted_text=encrypted_text)


@app.route("/transposition/decrypt", methods=["POST"])
def transposition_decrypt():

    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])

    transposition = TranspositionCipher()
    decrypted_text = transposition.transposition_decrypt(text, key)

    return render_template("transposition.html", decrypted_text=decrypted_text)

#main Function

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
    