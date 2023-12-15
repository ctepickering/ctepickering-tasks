def binarySearch(array, x, first, last):

    if last >= first:

        mid = first + (last - first)//2

        # If found at mid, then return it
        if array[mid] == x:
            return mid

        # Search the left half
        elif array[mid] > x:
            return binarySearch(array, x, first, mid-1)

        # Search the right half
        else:
            return binarySearch(array, x, mid + 1, last)

    else:
        return -1


array = [3, 4, 5, 6, 7, 8, 9]
x = 4

result = binarySearch(array, x, 0, len(array)-1)

if result != -1:
    print("item is present at  " + str(result))
else:
    print("Not found")