def DAC_Max(a, index, l):
    if index >= l - 2:
        if a[index] > a[index + 1]:
            return a[index]
        else:
            return a[index + 1]

    max_val = DAC_Max(a, index + 1, l)

    if a[index] > max_val:
        return a[index]
    else:
        return max_val

def DAC_Min(a, index, l):
    if index >= l - 2:
        if a[index] < a[index + 1]:
            return a[index]
        else:
            return a[index + 1]

    min_val = DAC_Min(a, index + 1, l)

    if a[index] < min_val:
        return a[index]
    else:
        return min_val

def main():
    arr = []
    n = None
    while True:
        try:
            n = int(input("Enter the number of elements in the array: "))
            break
        except ValueError:
            print("Invalid input! Please enter an integer.")

    print("Enter the elements of the array:")
    for i in range(n):
        while True:
            try:
                num = int(input())
                arr.append(num)
                break
            except ValueError:
                print("Invalid input! Please enter an integer.")
        
    print("Maximum Order Received:", DAC_Max(arr, 0, len(arr)))
    print("Minimum Orders Received:", DAC_Min(arr, 0, len(arr)))

if __name__ == "__main__":
    main()
