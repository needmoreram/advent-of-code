with open('input/input-1.txt') as f:
    nums = f.read().rstrip('\n')

def foo(nums, delta):
    ans = 0
    for i, c in enumerate(nums):
        n = int((i + delta) % len(nums))
        if c == nums[n]:
            ans += int(c)
    return ans

print("part 1:", foo(nums, 1))
print("part 2:", foo(nums, len(nums)/2))
