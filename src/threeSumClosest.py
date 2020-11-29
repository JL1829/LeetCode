"""
给定一个包括n各整数的数组`nums`和一个目标值`target`
找出`nums`中的三个整数，使得它们的和与`target`最接近，返回这三个整数的和
假定每组输入只存在唯一答案。

>>> nums = [-1, 2, 1, -4]
>>> target = 1
>>> threeSumClosest(array=nums, tg=target)
2

因为与`target`最接近的和是2：
sum([-1, 2, 1]) == 2

>>> nums = [-1, 2, 1, -4]
>>> target = 0
>>> threeSumClosest(array=nums, tg=target)
-1

解题思路：
类似于threeSum， 只是这里加多了一个abs(current_sum - target) < abs(result - target)
的过程

遍历首元素，第二元素和最后元素双指针对撞（对撞指针）
"""

numbers = [-1, 2, 1, -4]


def threeSumClosest(array, tg):
    if not array or len(array) < 3:
        return []

    array.sort()

    result = float('inf')
    for i in range(len(array)):
        if i > 0 and array[i] == array[i - 1]:
            continue

        left = i + 1
        right = len(array) - 1
        while left < right:
            current_sum = array[i] + array[left] + array[right]
            if current_sum == tg:
                return tg
            if abs(current_sum - tg) < abs(result - tg):
                result = current_sum
            if current_sum < tg:
                left += 1
            else:
                right -= 1

    return result


print(f"With input array: {numbers}, and target: 1"
      f"\n the answer is: {threeSumClosest(array=numbers, tg=1)}")

print(f"With input array: {numbers}, and target: 0"
      f"\n the answer is: {threeSumClosest(array=numbers, tg=0)}")
