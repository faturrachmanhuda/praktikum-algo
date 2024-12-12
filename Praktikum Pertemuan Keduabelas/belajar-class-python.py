class Mahasiswa:
  def __init__(self, nama, nim, jurusan):
    self.nama = nama
    self.nim = nim
    self.jurusan = jurusan
  
  def displayData(self):
    print(f"Nama: {self.nama}, NIM: {self.nim}, Jurusan: {self.jurusan}")

nama = input("Nama Mahasiswa: ")
nim = input("NIM Mahasiswa: ")
jurusan = input("Jurusan Mahasiswa: ")

mahasiswa1 = Mahasiswa(nama, nim, jurusan)
mahasiswa1s.displayData()
