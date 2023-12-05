class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        lengths = [len(x) for x in nums]
        minL = min(lengths)
        index = lengths.index(minL)
        small = nums[index]
        result = []
        i = 0
        while i < len(small):
            n = small[i]
            j = 0
            flag = 0
            while j < len(nums):
                if j == index and j+1 < len(nums):
                    j+=1
                if n not in nums[j]:
                    flag = 1
                    break
                j+=1
            if flag == 0:
                result.append(n)
            i+=1
        result.sort()
        return result
            
        