class Solution:
     def minMaxGame(self, nums: List[int]) -> int:
        while len(nums)>1:
            nn=[]
            for i in range(len(nums)//2):
                if i%2==0:
                    nn.append(min(nums[2*i],nums[2*i+1]))
                else:
                    nn.append(max(nums[2*i],nums[2*i+1]))
            nums=nn
        return nums[0]