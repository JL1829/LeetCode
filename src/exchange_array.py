nums = [1, 2, 3, 4]


def exchange(array):
    even = [i for i in array if i % 2 == 0]
    odd = [i for i in array if i % 2 != 0]
    return odd + even


print(f"Original Array: {nums},\n Now swapping")
print(f"After swapping: {exchange(nums)}")


# two pointer solution
# Time: O(N), Space: O(1)
def twoPointerExchange(array):
    # two pointer
    i = 0
    j = len(array) - 1

    while i < j:
        # even number
        while i < j and array[i] & 1 == 1:
            i += 1
        # odd number
        while i < j and array[j] & 1 == 0:
            j -= 1
        # swap
        array[i], array[j] = array[j], array[i]

    return array


nums = [1, 2, 3, 4]
print(f"Another Solution: {twoPointerExchange(nums)}")
