class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.__nama = nama
        self.__nim = nim
        self.__jurusan = jurusan

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama):
        if nama:
            self.__nama = nama
        else:
            print("Nama tidak boleh kosong!")

    def get_nim(self):
        return self.__nim

    def set_nim(self, nim):
        if len(nim) == 10 and nim.isdigit():
            self.__nim = nim
        else:
            print("NIM harus berupa 10 digit angka!")

    def get_jurusan(self):
        return self.__jurusan

    def set_jurusan(self, jurusan):
        if jurusan:
            self.__jurusan = jurusan
        else:
            print("Jurusan tidak boleh kosong!")

    def display_data(self):
        print(f"Nama: {self.__nama}, NIM: {self.__nim}, Jurusan: {self.__jurusan}")

nama = input("Nama Mahasiswa: ")
nim = input("NIM Mahasiswa: ")
jurusan = input("Jurusan Mahasiswa: ")

mahasiswa = Mahasiswa(nama, nim, jurusan)

while True:
    print("\n--- Pilihan ---")
    print("1. Tampilkan Data Mahasiswa")
    print("2. Ubah Nama")
    print("3. Ubah NIM")
    print("4. Ubah Jurusan")
    print("5. Keluar")

    pilihan = input("Pilih opsi (1-5): ")

    if pilihan == "1":
        mahasiswa.display_data()
    elif pilihan == "2":
        nama_baru = input("Masukkan nama baru: ")
        mahasiswa.set_nama(nama_baru)
    elif pilihan == "3":
        nim_baru = input("Masukkan NIM baru: ")
        mahasiswa.set_nim(nim_baru)
    elif pilihan == "4":
        jurusan_baru = input("Masukkan jurusan baru: ")
        mahasiswa.set_jurusan(jurusan_baru)
    elif pilihan == "5":
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")
