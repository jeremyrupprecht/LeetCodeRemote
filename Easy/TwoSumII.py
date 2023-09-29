# Two Sum II
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/?source=submission-ac

def twoSumTwo(numbers, target):
    p1 = 0
    p2 = len(numbers) - 1
    while p1 != p2:
        sum = numbers[p1] + numbers[p2]
        if sum == target:
            return [(p1 + 1), (p2 + 1)]
        elif sum > target:
            p2 -= 1
        else:
            p1 += 1
    return []

if __name__ == "__main__":
    numbers = [-1,0]
    target = -1
    result = twoSumTwo(numbers, target)
    print(result)


