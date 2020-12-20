nums = [18,11,9,0,5,1]

def last_index(ls, elem):
    return len(ls) - 2 - ls[:-1][::-1].index(elem)

for i in range(len(nums), 2020):
    last_num = nums[-1]
    if last_num not in nums[:-1]:
        nums.append(0)
        continue
    last_idx = last_index(nums, last_num)
    nums.append(i - 1 - last_idx)

print(nums[-1])

