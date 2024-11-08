bilangan = int(input("Input bilangan: "))

if bilangan % 10 == 1 and bilangan != 11:
  suffix = "st"
elif bilangan % 10 == 2 and bilangan != 12:
  suffix = "nd"
elif bilangan % 10 == 3 and bilangan != 13:
  suffix = "rd"
else:
  suffix = "th"

print(f"{bilangan}{suffix}")