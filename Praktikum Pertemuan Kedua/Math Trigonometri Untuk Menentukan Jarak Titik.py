import math

lat1 = float(input("Masukkan latitude titik pertama: "))
lon1 = float(input("Masukkan longitude titik pertama: "))
lat2 = float(input("Masukkan latitude titik kedua: "))
lon2 = float(input("Masukkan longitude titik kedua: "))

lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
delta_lat = lat2 - lat1
delta_lon = lon2 - lon1
a = math.sin(delta_lat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(delta_lon / 2)**2
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
R = 6371.0
distance = R * c

# Output jarak
print(f"Jarak antara kedua titik adalah {distance:.2f} km")