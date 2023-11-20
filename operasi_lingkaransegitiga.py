from modul_lingkaran import lingkaran
from modul_segitiga import segitiga


# Masukkan perintah pemilihan
print("Pilih bangun ruang yang akan dihitung? ")
print("1. Lingkaran")
print("2. Segitiga")
print("-------------------------------------")

# Proses pemiliihan dan penginputan
pilih = input("Pilih (1/2) : ")
if pilih == "1":
    jari_jari = int(input("Masukkan nilai jari - jari : "))
    hasil = lingkaran(jari_jari)
    
elif pilih == "2":
    alas = int(input("Masukkan nilai alas : "))
    tinggi = int(input("Masukkan nilai tinggi : "))
    luas = segitiga(alas, tinggi)