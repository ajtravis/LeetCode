class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        used = set()
        i = 0;
        result = []
        length = len(nums)
        while i < length:
            if nums[i] in used:
                i+= 1     
            else:
                used.add(nums[i])
                result.append(nums[i])
                i+=1
        j = 0;
        while j < len(result):
            nums[j] = result[j]
            j+=1
        k = len(result)
        
        return k