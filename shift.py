nums = [1,2,4,7,8]
k = 3

l = len(nums)

for _ in range(k % l):
    last = nums[-1]
    for i in range(l - 1, -1, -1):
        nums[i] = nums[i-1]

    nums[0] = last

print(nums)

