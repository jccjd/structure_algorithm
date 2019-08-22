def quick(list, left, right):
    if left > right:
        return list
    key = list[left]
    start = left
    end = right
    while left < right:
        while left < right and list[right] > key:
            right -= 1
        list[left] = list[right]
        while left < right and list[left] <= key:
            left += 1
        list[right] = list[left]

    list[left] = key
    quick(list, start, left - 1)
    quick(list, left + 1, end)
    return list
# 列表推导式版，更符合分治的思想 而且简洁易懂
# def Quictsort(list):
#     if len(list) <= 1:
#         return list
#
#     mid = len(list) // 2
#     key = list[mid]
#     left = [i for i in list if i < key]
#     middel = [i for i in list if i == key]
#     rigth = [i for i in list if i > key]
#
#     return Quictsort(left) + middel + Quictsort(rigth)
# print(Quictsort([5, 4, 3, 2, 1]))
# list = [2,5,7,6,3,1]
# l = quick(list,0,5)
# print(l)


def Quicksort(nums):
    if len(nums) <= 1:
        return nums

    middle = nums[len(nums) // 2]
    left = [i for i in nums if i < middle]
    cent = [i for i in nums if i == middle]
    right = [i for i in nums if i > middle]

    return Quicksort(left) + cent + Quicksort(right)



nums = [5, 4, 3, 2, 1]
print(Quicksort(nums))