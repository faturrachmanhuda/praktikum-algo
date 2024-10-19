totalHarga = 0

while True:
    inputUmur = input("Masukkan umur: ")
    
    if inputUmur.lower() == '':
        break
    
    umur = int(inputUmur)
    
    if umur <= 2:
        hargaTiket = 0
    elif 3 <= umur <= 12:
        hargaTiket = 14
    elif umur >= 65:
        hargaTiket = 18
    else:
        hargaTiket = 23
    
    print(f"Harga tiket untuk umur {umur} tahun adalah ${hargaTiket}")
    totalHarga += hargaTiket

print(f"\nTotal harga tiket: ${totalHarga}")

while True:
    uang = float(input("Masukkan jumlah uang yang dibayarkan: $"))
    
    if uang < totalHarga:
        print("Uang yang dibayarkan kurang, silakan masukkan jumlah yang cukup.")
    else:
        kembalian = uang - totalHarga
        print(f"Terima kasih! Kembalian Anda: ${kembalian:.2f}")
        break
