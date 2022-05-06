from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l=[]
        digit = int(''.join([str(elem) for elem in digits])) +1
        [l.append(i) for i in str(digit)]
        return l



a=Solution()
print(a.plusOne([9]))