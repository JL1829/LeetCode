"""
给你n个非负整数`a1, a2, a3.....`
每个数代表坐标中的一个点(i, a_i)。在坐标内画n条垂直于x轴的直线
找出最大面积（容纳最多水）的组合。

输入：[1,8,6,2,5,4,8,3,7]
输出：49
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为49。

![pic](https://aliyun-lc-upload.oss-cn-hangzhou.aliyuncs.com/aliyun-lc-upload/uploads/2018/07/25/question_11.jpg)

"""

points = [1, 8, 6, 2, 5, 4, 8, 3, 7]


def max_area(height):
    low, high = 0, len(height) - 1
    answer = 0
    while low < high:
        area = min(height[low], height[high]) * (high - low)
        answer = max(answer, area)

        if height[low] < height[high]:
            low += 1
        else:
            high -= 1

    return answer


print(f"With input height points: {points}"
      f"\n The maximum area: {max_area(height=points)}")


# official answer
def maxArea(height):
    n = len(height)
    low = 0
    high = n - 1

    maxarea = (high - low) * min(height[low], height[high])

    while low < high:
        if height[low] < height[high]:
            low += 1
        else:
            high -= 1
        maxarea = max(maxarea, (high - low) * min(height[low], height[high]))

    return maxarea
