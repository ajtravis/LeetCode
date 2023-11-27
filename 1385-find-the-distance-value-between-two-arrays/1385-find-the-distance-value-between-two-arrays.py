class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        i = 0
        while i < len(arr1):
            j = 0
            while j < len(arr2):
                dif = abs(arr1[i] - arr2[j])
                if j == (len(arr2) - 1) and dif > d:
                    count += 1
                if dif <= d:
                    break
                j += 1
            i += 1
        return count  
                        
            # vals = []
            # for j in arr2:
            #     dif = abs(i - j)
            #     vals.append(dif)
            # distances.append(vals)
#         x = 0
#         while x < len(distances):
            
#         return count