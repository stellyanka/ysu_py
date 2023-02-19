nums1 = [1,2,3,4,3]
nums2 = [5,6,2,3,3]

print(list(set(nums1) & set(nums2)))


result = []
for n in nums1:
    if n in nums2 and not n in result:
        result.append(n)
        
print(result)