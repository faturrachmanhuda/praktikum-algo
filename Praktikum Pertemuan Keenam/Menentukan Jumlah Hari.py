import calendar
import datetime

def jumlahHari(bulan, tahun):
  tanggal = datetime.date(tahun, bulan, 1)
  jumlahHari = calendar.monthrange(tanggal.year, tanggal.month)[1]
  return jumlahHari

def kabisat(tahun):
  if tahun % 4 == 0:
    if tahun % 100 == 0:
      if tahun % 400 == 0:
        return True
      else:
        return False
    else:
      return True

while True:
  bulan = int(input("Masukkan bulan: (1-12) "))
  if bulan < 1 or bulan > 12:
    print("Bulan tidak valid")
  else:
    break

tahun = int(input("Masukkan tahun: "))


if kabisat(tahun):
  print(f"Jumlah hari dalam bulan {bulan} tahun {tahun} adalah {jumlahHari(bulan, tahun)}")
  print(f"Tahun {tahun} adalah tahun kabisat")
else:
  print(f"Jumlah hari dalam bulan {bulan} tahun {tahun} adalah {jumlahHari(bulan, tahun)}")
  print(f"Tahun {tahun} bukan tahun kabisat")