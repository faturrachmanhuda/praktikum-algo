nilai = 0
counter = 0

while True:
  inputGrade = input("Grade: ").upper()

  if inputGrade == "A":
    counter += 1
    nilai += 4.0
    continue
  elif inputGrade == "A-":
    counter += 1
    nilai += 3.75
    continue
  elif inputGrade == "B+":
    counter += 1
    nilai += 3.50
    continue
  elif inputGrade == "B":
    counter += 1
    nilai += 3.00
    continue
  elif inputGrade == "B-":
    counter += 1
    nilai += 2.75
    continue
  elif inputGrade == "C+":
    counter += 1
    nilai += 2.50
    continue
  elif inputGrade == "C":
    counter += 1
    nilai += 2.00
    continue
  elif inputGrade == "C-":
    counter += 1
    nilai += 1.75
    continue
  elif inputGrade == "D":
    counter += 1
    nilai += 1.50
    continue
  elif inputGrade == "E":
    counter += 1
    nilai += 1.25
    continue
  else:
    if counter > 0:
            nilai = nilai / float(counter)
        
    if 3.75 <= nilai <= 4.0:
            grade = "A"
    elif 3.5 <= nilai < 3.75:
            grade = "A-"
    elif 3.0 <= nilai < 3.5:
            grade = "B+"
    elif 2.75 <= nilai < 3.0:
            grade = "B"
    elif 2.5 <= nilai < 2.75:
            grade = "B-"
    elif 2.0 <= nilai < 2.5:
            grade = "C+"
    elif 1.75 <= nilai < 2.0:
            grade = "C"
    elif 1.5 <= nilai < 1.75:
            grade = "C-"
    elif 1.25 <= nilai < 1.5:
            grade = "D"
    else:
            grade = "E"
        
    print(f"Rata-rata nilai: {nilai:.2f}, Grade: {grade}")
    break