satuan = input("Satuan meter / inch: ").strip()
panjang = float(input("Panjang: "))
lebar = float(input("Lebar: "))

if satuan.lower() == "meter":
    luas = panjang * lebar
    print(f"Luas ruangannya adalah: {luas} m²")
elif satuan.lower() == "inch":
    panjang2 = panjang * 0.0254
    lebar2 = lebar * 0.0254
    luas = panjang2 * lebar2
    print(f"Luas ruangannya adalah: {luas} m²")
else:
    print("Satuan yang anda masukkan tidak terdefinisi!")