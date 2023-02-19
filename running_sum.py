nums = [1,2,3,4,5]
result = []

for j in range(len(nums)):
    s = 0
    for i in range(j + 1):
        s += nums[i]

    result.append(s)

print(result)