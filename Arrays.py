# Merge Sorted Arrays

def merge(nums1, m, nums2, n):
  index1 = m - 1
  index2 = n - 1
  merged_index = m + n - 1

  while index1 >= 0 and index2 >= 0:
      if nums1[index1] > nums2[index2]:
          nums1[merged_index] = nums1[index1]
          index1 -= 1
      else:
          nums1[merged_index] = nums2[index2]
          index2 -= 1
      merged_index -= 1

  while index2 >= 0:
      nums1[merged_index] = nums2[index2]
      index2 -= 1
      merged_index -= 1

#case1
nums1_1 = [1,2,3,0,0,0]
m_1 = 3
nums2_1 = [2,5,6]
n_1 = 3
merge(nums1_1, m_1, nums2_1, n_1)
print(nums1_1)  
#Case2
nums1_2 = [1]
m_2 = 1
nums2_2 = []
n_2 = 0
merge(nums1_2, m_2, nums2_2, n_2)
print(nums1_2)  
#case3
nums1_3 = [0]
m_3 = 0
nums2_3 = [1]
n_3 = 1
merge(nums1_3, m_3, nums2_3, n_3)
print(nums1_3)  
