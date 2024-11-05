def encrypt(key, sentence):
    # Alphabet untuk enkripsi
    letters = 'abcdefghijklmnopqrstuvwxyz'
    
    # Menemukan posisi huruf key dalam alphabet
    pos = letters.find(key.lower())  # Cari posisi huruf key
    if pos == -1:
        print("Key tidak valid. Harus huruf dalam alphabet.")
        return ""
    
    encryptedSentence = ""
    
    # Iterasi untuk setiap huruf dalam kalimat yang akan dienkripsi
    for char in sentence:
        if char.isalpha():  # Cek apakah karakter adalah huruf
            # Menghitung posisi huruf terenkripsi
            new_pos = (letters.find(char.lower()) + pos) % len(letters)
            
            # Menambahkan huruf terenkripsi ke hasil enkripsi
            if char.isupper():
                encryptedSentence += letters[new_pos].upper()
            else:
                encryptedSentence += letters[new_pos]
        else:
            encryptedSentence += char  # Kalau bukan huruf, tambahkan langsung (misal spasi)
    return encryptedSentence

def decrypt(key, encrypted_sentence):
    # Alphabet untuk enkripsi
    letters = 'abcdefghijklmnopqrstuvwxyz'
    
    # Menemukan posisi huruf key dalam alphabet
    pos = letters.find(key.lower())  # Cari posisi huruf key
    if pos == -1:
        print("Key tidak valid. Harus huruf dalam alphabet.")
        return ""
    
    decrypted_sentence = ""
    
    # Iterasi untuk setiap huruf dalam kalimat yang akan didekripsi
    for char in encrypted_sentence:
        if char.isalpha():  # Cek apakah karakter adalah huruf
            # Menghitung posisi huruf yang terdekripsi (mengurangi posisi)
            new_pos = (letters.find(char.lower()) - pos) % len(letters)
            
            # Menambahkan huruf terdekripsi ke hasil dekripsi
            if char.isupper():
                decrypted_sentence += letters[new_pos].upper()
            else:
                decrypted_sentence += letters[new_pos]
        else:
            decrypted_sentence += char  # Kalau bukan huruf, tambahkan langsung (misal spasi)

    return decrypted_sentence