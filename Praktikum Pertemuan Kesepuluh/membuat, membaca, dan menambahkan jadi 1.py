def create_file(filename):
    with open(filename, 'w') as file:
        print(f"File '{filename}' telah dibuat.")
        
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print(f"Isi dari file '{filename}':")
            print(file.read())
    except FileNotFoundError:
        print(f"File '{filename}' tidak ditemukan.")

def append_to_file(filename, text):
    with open(filename, 'a') as file:
        file.write(text + '\n')
        print(f"Text telah ditambahkan ke dalam file '{filename}'.")

def show_menu():
    print("\nMenu:")
    print("1. Buat file baru")
    print("2. Baca file")
    print("3. Tambahkan text ke dalam file")
    print("4. Keluar (close)")

# Program utama
def main():
    while True:
        show_menu()
        pilihan = input("Pilih menu (1/2/3/4): ")

        if pilihan == '1':
            filename = input("Masukkan nama file: ")
            create_file(filename)

        elif pilihan == '2':
            filename = input("Masukkan nama file untuk dibaca: ")
            read_file(filename)

        elif pilihan == '3':
            filename = input("Masukkan nama file untuk ditambahkan text: ")
            text = input("Masukkan text yang ingin ditambahkan: ")
            append_to_file(filename, text)

        elif pilihan == '4':
            print("Terima kasih telah menggunakan program.")

        else:
            print("Pilihan tidak valid, coba lagi.")

# Menjalankan program
if __name__ == "__main__":
    main()
