import math

## INPUT
bil1 = input("Masukkan bilangan pertama: ")
bil2 = input("Masukkan bilangan kedua: ")

## PROSES
bil1 = int(bil1)
bil2 = int(bil2)
tg1 = bil1 + bil2
tg2 = bil1 - bil2
tg3 = bil1 * bil2
tg4 = bil1 % bil2
tg5 = bil1 / bil2
tg6 = math.log10(bil1)
tg7 = bil1 ** bil2

## OUTPUT
print("Pertambahan:",tg1)
print("Pengurangan / Selisih:",tg2)
print("Perkalian:",tg3)
print("Hasil bagi:",tg4)
print("Pembagian:",tg5)
print("Log basis 10:",tg6)
print("Pangkat 2:",tg7)