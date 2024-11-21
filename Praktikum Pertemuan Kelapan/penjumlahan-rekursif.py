def penjumlahan(jumlah, temp=1, total=0):
  if temp > jumlah:
    return total
  else:

    angka = int(input(f"Masukkan angka ke-{temp}: "))

    return penjumlahan(jumlah, temp + 1, total + angka)

jumlahAngka = int(input("Masukkan jumlah angka: "))
hasil = penjumlahan(jumlahAngka)
print("Hasil dari pertambahan angka tersebut adalah:",hasil)