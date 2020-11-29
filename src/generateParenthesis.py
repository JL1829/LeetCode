"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

**test case**

>>> n = 3
>>> generateParenthesis(number=n)
['((()))', '(()())', '(())()', '()(())', '()()()']

"""


def generateParenthesis(number):
    result = []

    def dfs(left, right, path):
        if left > number or right > number:
            return
        if left == right == number:
            result.append(path)
        if left < right:
            return
        dfs(left + 1, right, path + '(')
        dfs(left, right + 1, path + ')')
    dfs(0, 0, '')
    return result


if __name__ == '__main__':
    n = 3
    print(generateParenthesis(number=n))
