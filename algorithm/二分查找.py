def binary_search(list,key):
    start = 0
    end = len(list)
    while start < end:
        mid = (start + end) // 2

        if key > list[mid]:
            start = mid + 1
        elif key < list[mid]:
            end = mid -1
        else:
            return mid

list = [1,2,3,4,5]
print(binary_search(list,1))
