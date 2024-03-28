def minimize_moves(arr):
    swaps_count = 0
    arr_len = len(arr)
    for i in range(arr_len - 1):
        min_index = i
        for j in range(i + 1, arr_len):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            print("Swap", min_index, "th book with", i, "th book")
            swaps_count += 1
            arr[min_index], arr[i] = arr[i], arr[min_index]
    return swaps_count

if __name__ == "__main__":
    total_books = int(input("Enter the total number of books: "))
    print("Enter the publication years of the books separated with spaces:")
    publication_years = list(map(int, input().split()))
    
    print("----OUTPUT----")
    total_swaps = minimize_moves(publication_years)
    print("Total number of swaps needed:", total_swaps)
    
    print("Sorted order of books by publication year:")
    for year in publication_years:
        print(year, end=" ")
    print()
