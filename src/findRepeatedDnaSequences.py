"""
所有的DNA都是由一系列缩写为`A`, `C`, `G`, `T`的核苷酸组成， 例如：
`ACGAATTCCG`。在研究DNA时，识别DNA中重复的序列有时候会对研究很有帮助。

编写一个函数， 找出所有的目标子串，目标子串长度为`L`， 且在DNA字符串`s` 中出现次数超过一次

**test case**
>>> s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
>>> findRepeatedDnaSequence(sequence=s, length=10)
['AAAAACCCCC', 'CCCCCAAAAA']

>>> s = 'AAAAAAAAAAAAA'
>>> findRepeatedDnaSequence(sequence=s, length=10)
['AAAAAAAAAA']

# Solution
***
## Approach 1
简单固定长度滑动窗口， 长度为L, 左边逐个迭代。
并且用两个set(), 一个用于存储已经见过的字符串，一个用于输出

"""


def findRepeatedDnaSequence(sequence, length):
    n = len(sequence)
    seen = set()
    output = set()

    # iterate over all sequences of length
    for start in range(n - length + 1):
        tmp = sequence[start:start + length]
        if tmp in seen:
            output.add(tmp[:])
        seen.add(tmp)

    return list(output)


if __name__ == '__main__':
    s1 = 'AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'
    s2 = 'AAAAAAAAAAAAA'
    print(f"For input DNA string: {s1}"
          f"\n The Repeated subSequence is: {findRepeatedDnaSequence(sequence=s1, length=10)}")
    print(f"For input DNA string: {s2}"
          f"\n The Repeated subSequence is: {findRepeatedDnaSequence(sequence=s2, length=10)}")
