panjang1, panjang2, panjang3 = map(float,input("Input panjang: ").split())

if panjang1 + panjang2 > panjang3 and panjang1 + panjang3 > panjang2 and panjang2 + panjang3 > panjang1:
  
  if panjang1 == panjang2 == panjang3:
    print("Segitiga Sama Sisi")
    # 3 3 3
  elif panjang1 == panjang2 or panjang1 == panjang3 or panjang2 == panjang3:
    print("Segitiga Sama Kaki")
    # 5 5 3
  else:
   print("Segitiga Sembarang")
    # 4 5 6
else:
  print("Bukan bagian dari segitiga.\nSyarat Membangun Segitiga:\n1. Panjang1 + Panjang2 harus lebih besar dari Panjang3\n2. Panjang1 + Panjang3 harus lebih besar dari Panjang2\n3. Panjang2 + Panjang3 harus lebih besar dari Panjang1")