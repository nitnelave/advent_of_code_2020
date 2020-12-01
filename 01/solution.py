#! /usr/bin/env python3

numbers = sorted(map(int, open('input')))

def find_two_nums(nums, total):
    i = 0
    j = -1
    while nums[i] + nums[j] != total:
        if nums[i] + nums[j] > total:
            j -= 1
        else:
            i += 1
        if i - j > len(nums) + 2:
            return None

    return nums[i] * nums[j]


def find_three_nums():
    for i in range(len(numbers)):
        prod = find_two_nums(numbers[:i]+numbers[i+1:], 2020 - numbers[i])
        if prod is not None:
            return prod * numbers[i]
    return None

print(find_two_nums(numbers, 2020))

print(find_three_nums())
