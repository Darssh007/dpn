def removeElement(nums, val):
    if not nums:
        return 0
    
    k = 0  

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    
    return k
#Case test
nums = [3, 2, 2, 3]
val = 3
expectedNums = [2, 2]

k = removeElement(nums, val)
assert k == len(expectedNums)

nums.sort()
assert nums[:k] == expectedNums

# Print the results
print(f"Modified nums: {nums[:k]}")
print(f"Length of nums not equal to {val}: {k}")
