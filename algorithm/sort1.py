def bubble(nums):
    for i in range(len(nums)):
        for j in range(len(nums) -1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums

def Insertsort(nums):
    for i in range(len(nums)):
        for j in range(i - 1, -1, -1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
nums = [4, 3, 2, 1]

def Selectsort(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums

def merg_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = merg_sort(nums[:mid])
    right = merg_sort(nums[mid:])

    left_point = 0
    right_point = 0
    result = []

    while len(left) > left_point and len(right) > right_point:
        if left[left_point] < right[right_point]:
            result.append(left[left_point])
            left_point += 1
        else:
            result.append(right[right_point])
            right_point += 1

    result += left[left_point:]
    result += right[right_point:]
    return result


nums = [1, 4, 3, 2]
# print(bubble(nums))
# print(Insertsort(nums))
# print(Selectsort(nums))
print(merg_sort(nums))
