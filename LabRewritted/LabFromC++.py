import random

def fill_arr(arr, rows, cols):
    random.seed()
    for i in range(rows):
        for j in range(cols):
            arr[i][j] = random.randint(0, 9)


def print_arr(arr, rows, cols):
    for i in range(rows):
        for j in range(cols):
            print(arr[i][j], end=" ")
        print()


def seek_min_elem(arr, rows, cols):
    min_val = float('inf')
    min_i = 0

    for i in range(rows):
        for j in range(cols):
            if arr[i][j] < min_val:
                min_val = arr[i][j]
                min_i = i

    print("\nMIN:", min_val)
    print("MIN_i:", min_i, "\n")

    rows, cols, new_arr = cut_arr(arr, rows, cols, min_i)
    return rows,cols, new_arr


def cut_arr(arr, rows, cols, min_i):
    new_arr = [x for x in arr if x != arr[min_i]]
    rows -= 1
    return rows, cols, new_arr


if __name__ == "__main__":
    rows = int(input("Rows: "))
    cols = int(input("Cols: "))

    arr = [[0 for j in range(cols)] for i in range(rows)]

    fill_arr(arr, rows, cols)
    print_arr(arr, rows, cols)
    rows, cols, arr = seek_min_elem(arr, rows, cols)
    print_arr(arr, rows, cols)
