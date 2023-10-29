class Solution:
    
#     cv = 0
    
#     def findTheArrayConcVal(self, nums):
#         n = len(nums)
#         if n == 1:
#             Solution.cv += nums[0]
#             result = Solution.cv
#             Solution.cv = 0
#             return result
#         elif n == 2:
#             num1 = str(nums[0])
#             num2 = str(nums[-1])
#             conc = int(num1 + num2)
#             Solution.cv += conc
#             result = Solution.cv
#             Solution.cv = 0
#             return result
#         else:
#             num1 = str(nums[0])
#             num2 = str(nums[-1])
#             conc = int(num1 + num2)
#             Solution.cv += conc
#             new_nums = nums[1:-1]
#             return self.findTheArrayConcVal(new_nums)
    def findTheArrayConcVal(self, nums, cv=0):
        n = len(nums)
        if n == 1:
            cv += nums[0]
            return cv
        elif n == 2:
            num1 = str(nums[0])
            num2 = str(nums[-1])
            conc = int(num1 + num2)
            cv += conc
            return cv
        else:
            num1 = str(nums[0])
            num2 = str(nums[-1])
            conc = int(num1 + num2)
            cv += conc
            new_nums = nums[1:-1]
            return self.findTheArrayConcVal(new_nums, cv)