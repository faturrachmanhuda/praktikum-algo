nama = input("Masukkan Nama-mu: ")
umur = input("Masukkan Umur-mu: ")
alamat = input("Masukkan Alamat-mu: ")
email = input("Masukkan Email-mu: ")
dosen_wali = input("Masukkan Dosen Wali-mu: ")

with open("Biodata.txt", "w") as f:
  f.write(f"Nama: {nama}\n")
  f.write(f"Umur: {umur}\n")
  f.write(f"Alamat: {alamat}\n")
  f.write(f"Email: {email}\n")
  f.write(f"Dosen Wali: {dosen_wali}\n")
  f.close()
  
print()
file = open("Biodata.txt", "r")
text = file.read()
print(text)
file.close()

print("Selesai!")