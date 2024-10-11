import calendar

nama_bulan = [
    "januari", "februari", "maret", "april", "mei", "juni",
    "juli", "agustus", "september", "oktober", "november", "desember"
]

bulan = input("Bulan apa / keberapa? ").replace(" ", "")
tahun = input("Tahunnya? ").replace(" ", "")

while True:
  if bulan.isdigit():
    if int(bulan) <= 0 or int(bulan) > 12:
      print("Bulan hanya dari 1 hingga 12.")
      break
    elif 1 <= int(bulan) <= 12:
      hari = calendar.monthrange(int(tahun), int(bulan))[1]
      print(f"Bulan {bulan} tahun {tahun} memiliki {hari} hari.")
      break

  else:
    if bulan.lower() not in nama_bulan:
      print("Bulan tidak valid.")
      break
    else:
      bulan = nama_bulan.index(bulan.lower()) + 1
      hari = calendar.monthrange(int(tahun), int(bulan))[1]
      print(f"Bulan {bulan} tahun {tahun} memiliki {hari} hari.")
      break