with open('input/input-1.txt') as f:
    nums = list(map(int, f.read().splitlines()))

d = {}
# part 1: O(n)
for num in nums:
    if num in d:
        print("part 1:", num * d[num],
                    ";", num, d[num])
    d[2020 - num] = num

# part 2: O(n^2)
for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if (nums[i] + nums[j]) in d:
            print("part 2:", nums[i] * nums[j] * d[nums[i] + nums[j]]
                      , ";", nums[i], nums[j], d[nums[i] + nums[j]])
            break
    else:
        continue
    break
