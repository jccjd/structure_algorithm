# def merge_sort(list):
#     """归并排序"""
#     if len(list) <= 1:
#         return list
#     mid = len(list) // 2
#     left_list = merge_sort(list[:mid])
#     right_list = merge_sort(list[mid:])
#
#     leftpoint = 0
#     rightpoint = 0
#
#     result = []
#
#     while leftpoint < len(left_list) and rightpoint < len(right_list):
#         if left_list[leftpoint] < right_list[rightpoint]:
#             result.append(left_list[leftpoint])
#             leftpoint += 1
#         else:
#             result.append(right_list[rightpoint])
#             rightpoint += 1
#     result += left_list[leftpoint:]
#     result += right_list[rightpoint:]
#
#     return result
def merge(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    left = merge(list[:mid])
    right = merge(list[mid:])

    leftponit = 0
    rightponit = 0
    result = []

    while leftponit < len(left) and rightponit < len(right):
        if left[leftponit] < right[rightponit]:
            result.append(left[leftponit])
            leftponit += 1
        else:
            result.append(right[rightponit])
            rightponit += 1

    result += left[leftponit:]
    result += right[rightponit:]

    return result
numbers = [5, 4, 3, 2, 1]
print(merge(numbers))
