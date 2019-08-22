def Selectsort(nums):
    for i in range(len(nums)):
        min = nums[i]
        for j in range(i + 1, len(nums)):
            if nums[j] < min:
                nums[j], min = min, nums[j]
        nums[i] = min
    return nums
nums = [5,4,3,2,1]
print(Selectsort(nums))