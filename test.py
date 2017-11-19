import sys

def elim_left(nums):
    def elim_right(nums):
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return nums[0]
        elif len(nums) == 3:
            return nums[1]
        else:
            return elim_left(list(map(lambda x: nums[x], filter(lambda x: (len(nums) - x - 1) % 2 != 0, list(range(0, len(nums))) ))))

    if len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return nums[1]
    elif len(nums) == 3:
        return nums[1]
    else:
        return elim_right([nums[2 * x + 1] for x in range(0, len(nums) // 2)])


for x in range(1, int(sys.argv[1])):
    print(x, elim_left(list(map(lambda x: x + 1, list(range(0, x))))))
