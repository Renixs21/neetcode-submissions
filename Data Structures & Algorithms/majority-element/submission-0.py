class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        fun = {}

        for num in nums:
            if num in fun:
                fun[num] += 1
            else:
                fun[num] = 1

        return max(fun, key=fun.get)