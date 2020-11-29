nums = [3, 2, 4]


def twoSum(array, target):
    array.sort()
    low, high = 0, len(array) - 1

    while low < high:
        res = array[low] + array[high]
        if res < target:
            low += 1
        elif res > target:
            high -= 1
        elif res == target:
            return [low, high]


print(twoSum(nums, 9))


def two_sum_duplicate(array, target):
    array.sort()
    result = []
    left, right = 0, len(array) - 1
    while left < right:
        total = array[left] + array[right]
        if total < target:
            left += 1
        elif total > target:
            right -= 1
        else:
            result.append([array[left], array[right]])
            left += 1
            right -= 1

    return result


nums2 = [1, 3, 1, 2, 2, 3]
print(f"With incoming array: {nums2}, and target: 4")
print(f"Return tuple(duplicate) is: {two_sum_duplicate(array=nums2, target=4)}")


def two_sum_non_duplicate(array, target):
    # time complexity: O(N log N)
    array.sort()
    lo, hi = 0, len(array) - 1
    result = []
    while lo < hi:
        total = array[lo] + array[hi]
        left, right = array[lo], array[hi]
        if total < target:
            while lo < hi and array[lo] == left:
                lo += 1
        elif total > target:
            while lo < hi and array[hi] == right:
                hi -= 1
        else:
            result.append([left, right])
            while lo < hi and array[lo] == left:
                lo += 1
            while lo < hi and array[hi] == right:
                hi -= 1

    return result


print(f"Return Tuple without duplicate: {two_sum_non_duplicate(array=nums2, target=4)}")


def two_sum_modify(array, start, target):
    # time complexity: O(N log N)
    array.sort()
    lo = start
    hi = len(array) - 1
    result = []
    while lo < hi:
        total = array[lo] + array[hi]
        left, right = array[lo], array[hi]
        if total < target:
            while lo < hi and array[lo] == left:
                lo += 1
        elif total > target:
            while lo < hi and array[hi] == right:
                hi -= 1
        else:
            result.append([left, right])
            while lo < hi and array[lo] == left:
                lo += 1
            while lo < hi and array[hi] == right:
                hi -= 1

    return result


def three_sum(array, target):
    array.sort()
    n = len(array)
    result = []
    for i in range(n):
        tuples = two_sum_modify(array, i + 1, target - array[i])
        for item in tuples:
            item.append(array[i])
            result.append(item)

        while i < n - 1 and array[i] == array[i + 1]:
            i += 1

    return result


nums4 = [-1, 0, 1, 2, -1, 4]

print(f"\n 3 Sums with nums: {nums4}, and target: 0: \n {three_sum(array=nums4, target=0)}")
