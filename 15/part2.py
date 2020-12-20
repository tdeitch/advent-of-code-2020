nums = [18,11,9,0,5,1]

lasts = dict()
for i, n in enumerate(nums[:-1]):
    lasts[n] = i

last_num = nums[-1]
for i in range(len(nums), 30000000):
    if last_num not in lasts:
        lasts[last_num] = i - 1
        last_num = 0
        continue
    last_idx = lasts[last_num]
    lasts[last_num] = i - 1
    last_num = i - 1 - last_idx

print(last_num)

