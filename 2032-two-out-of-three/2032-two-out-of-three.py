class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        matches = []
        n = [nums1, nums2, nums3]
        def getL(x):
            return len(x)
        n.sort(key=getL)
        n1, n2 = set(n[0]), set(n[1])
        n3, n4 = n[1]+n[2], n[0]+n[2]
        for x in n1:
            if x in n3:
                matches.append(x)
        for x in n2:
            if x in n4:
                if x not in matches:
                    matches.append(x)
        return matches