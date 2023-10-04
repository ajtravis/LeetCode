class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        for i in range(len(encoded)):
            ele = arr[-1] ^ encoded[i]
            arr.append(ele)
        return arr