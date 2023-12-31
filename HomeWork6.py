def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 10, 40]
    x = 40
    result = binary_search(arr, x)

    if result != -1:
        print("Индекс искомого числа: ", str(result))
    else:
        print("Число не найдено в массиве")