a,b,c = map(int, input("Nilai A, B, dan C: ").split())

D = b**2 - 4*a*c

print(f"Determinannya: {D}")

if D > 0:
  x1 = (-b + D**(1/2)) / (2*a)
  x2 = (-b - D**(1/2)) / (2*a)
  print(f"Rumus ABC ada plus minusnya, berikut plusminusnya:\nPlus = {x1}\nMinus = {x2}")
elif D == 0:
  x = -b / (2*a)
  print(f"Termasuk dalam akar kembar dengan value = {x}")
else:
  real_part = -b / (2*a)
  imaginary_part = (-D)**0.5 / (2*a)
  print(f"Termasuk dalam akar kompleks dengan value: X1 = {real_part} + {imaginary_part}i dan X2 = {real_part} - {imaginary_part}i")