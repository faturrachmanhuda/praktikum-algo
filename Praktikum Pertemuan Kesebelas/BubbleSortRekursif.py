import random

def bubble_sort_recursive(arr, n=None):
    if n is None:
        n = len(arr)
    
    if n == 1:
        return

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    bubble_sort_recursive(arr, n - 1)

number_list = random.sample(range(1, 11), 10)
print(f"List sebelum disort:\n{number_list}")

bubble_sort_recursive(number_list)
print(f"List setelah disort:\n{number_list}")
