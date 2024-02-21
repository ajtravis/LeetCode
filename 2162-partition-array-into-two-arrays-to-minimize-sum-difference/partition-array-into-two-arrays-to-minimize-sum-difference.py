class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 2
        total = sum(nums)
        goal = total // 2

        def dfs(nums):
            ans = {(0, 0)}
            
            for num in nums:
                ans |= {(num + j[0], j[1] + 1) for j in ans}
            
            arr = []

            for i in range(n-1):
                arr.append([])

            length = 0
            
            for val, idx in ans:
                if idx != 0 and idx != n:
                    arr[idx-1].append(val)
                    
            return arr
            
        arr1 = dfs(nums[:n])
        arr2 = [sorted(arr) for arr in dfs(nums[n:])]

        halfSum = sum(nums[:n])

        min_diff = abs((total - halfSum) - halfSum)

        for i in range(len(arr1)):
            for j in range(len(arr1[i])):
                target = goal - arr1[i][j]
                
                idx = bisect.bisect_left(arr2[n-i-2], target)
                
                minDiff = math.inf
                value = math.inf
                
                if idx<len(arr2[n-i-2])and abs(target - arr2[n-i-2][idx]) < minDiff:
                        minDiff = abs(target - arr2[n-i-2][idx])
                        value = arr2[n-i-2][idx]
                if idx>0 and abs(target - arr2[n-i-2][idx-1]) < minDiff:
                        minDiff = abs(target - arr2[n-i-2][idx-1])
                        value = arr2[n-i-2][idx-1]
                
                halfSum = arr1[i][j] + value
                min_diff = min(min_diff, abs((total - halfSum) - halfSum))
                
        return min_diff