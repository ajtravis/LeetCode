class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 2 == 1:
            return 1 + self.numberOfSteps(num-1)
        else:
            return 1 + self.numberOfSteps(num/2)
        # steps = 0
        # while num > 0:
        #     if num % 2 == 0:
        #         num = num/2
        #     else:
        #         num -= 1
        #     steps+= 1
        # return steps