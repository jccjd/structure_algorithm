def binary_search(nums, key):
    start = 0
    end = len(nums)
    while start < end:
        mid = (start + end) // 2

        if key > nums[mid]:
            start = mid + 1
        elif key < nums[mid]:
            end = mid - 1
        else:
            return mid


nums = [1, 2, 3, 4, 5]
print(binary_search(nums, 1))
