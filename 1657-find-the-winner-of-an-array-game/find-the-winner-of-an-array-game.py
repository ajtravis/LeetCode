class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        i = 0
        high = max(arr)
        while i < k:
            if k > len(arr):
                return high
            if arr[0] > arr[1]:
                low = arr.pop(1)
                arr.append(low)
                i += 1
            else:
                low = arr.pop(0)
                arr.append(low)
                i = 1
        return arr[0]