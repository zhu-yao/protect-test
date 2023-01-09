from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int],target:int) -> List[int]:
        # 哈希集合，记录每个字符是否出现过
        occ = dict()
        for i,value in enumerate(nums):
            if target - value in occ:
                return [occ[target - value],i]
            else:
                occ[value] = i
        return []

if __name__ == '__main__':
    a = Solution().twoSum([1,2,3,4,5],6)
    print(a)






