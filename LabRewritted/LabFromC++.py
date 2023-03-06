import random

def fill_arr(arr, M, N):
    random.seed()
    for i in range(M):
        for j in range(N):
            arr[i][j] = random.randint(0, 9)


def print_arr(arr, M, N):
    for i in range(M):
        for j in range(N):
            print(arr[i][j], end=" ")
        print()


def seek_min_elem(arr, M, N):
    min_val = float('inf')
    min_i = 0

    for i in range(M):
        for j in range(N):
            if arr[i][j] < min_val:
                min_val = arr[i][j]
                min_i = i

    print("\nMIN:", min_val)
    print("MIN_i:", min_i, "\n")

    M, N, new_arr = cut_arr(arr, M, N, min_i)
    return M, N, new_arr


def cut_arr(arr, M, N, min_i):
    new_arr = []
    for i in range(M):
        if i != min_i:
            new_arr.append(arr[i])
    M -= 1
    return M, N, new_arr


if __name__ == "__main__":
    M = int(input("M: "))
    N = int(input("N: "))

    arr = [[0 for j in range(N)] for i in range(M)]

    fill_arr(arr, M, N)
    print_arr(arr, M, N)
    M, N, arr = seek_min_elem(arr, M, N)
    print_arr(arr, M, N)