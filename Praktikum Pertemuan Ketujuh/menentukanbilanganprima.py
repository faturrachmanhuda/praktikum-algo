def is_prima(n):
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

def is_non_prima(n):
  return not is_prima(n)

bilangan = int(input("Input bilangan: "))

if is_prima(bilangan):
  print(bilangan, "adalah bilangan prima")
elif is_non_prima(bilangan):
  print(bilangan, "adalah bilangan non-prima")