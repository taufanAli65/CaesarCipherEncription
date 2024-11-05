import caesarCipher as c

if __name__ == "__main__":
    print("""[1] Encryption
[2] Decryption""")
    ask_user = int(input("Pilih [1]/[2] : "))
    key = str(input("Key : "))
    sentence = str(input("Sentence : "))
    
    if ask_user == 1 :
        print(f"Hasil encrypt : {c.encrypt(key, sentence)}")
    elif ask_user == 2 : 
        print(f"Hasil decrypt : {c.decrypt(key, sentence)}")
    else :
        print("Key yang anda inputkan tidak valid")