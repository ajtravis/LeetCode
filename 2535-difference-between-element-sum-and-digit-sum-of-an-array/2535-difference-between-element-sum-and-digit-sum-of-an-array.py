class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        ele_sum = 0
        digit_sum = 0
        for i in nums:
            ele_sum += i
            s = str(i)
            for d in s:
                digit_sum += int(d)
        return abs(ele_sum - digit_sum)