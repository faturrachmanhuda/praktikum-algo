import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def bubble_sort2(arr):
    n = len(arr)
    if arr(0) > arr(1):
        arr(0), arr(1)

def indexNumber(numberList):
  for index, element in enumerate(number_list):
    if element == number_to_find:
        return index
        break

number_list = random.sample(range(1, 11), 10)
print(f"\nList saat ini:\n{number_list}")

number_to_find = int(input("\nInput angka yang ingin dicari: "))

bubble_sort(number_list)
print(f"\nList setelah di sort, dari terkecil hingga terbesar menggunakan bubble sort:\n{number_list}")

indexNumbers = indexNumber(number_list)
print(f"\nAngka {number_to_find} berada di index {indexNumbers}")

