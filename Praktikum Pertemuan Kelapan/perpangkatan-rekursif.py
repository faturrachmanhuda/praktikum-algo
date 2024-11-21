def perpangkatan(angka, power, temp=1, total=1):
  if temp > power:
    return total
  else:
    total *= angka
    return perpangkatan(angka, power, temp + 1, total)

angka = int(input("Angka Basic: "))
power = int(input("Angka Pangkat: "))
hasil = perpangkatan(angka, power)
print(f"{angka} pangkat {power} adalah {hasil}")
