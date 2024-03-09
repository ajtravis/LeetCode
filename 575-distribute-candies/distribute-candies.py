class Solution:
    def distributeCandies(self,theList):
        n = len(theList)
        setList =set(theList)
        sl = len(setList)
        eatLimit = int(n/2)
        if eatLimit>sl:
            return sl
        return eatLimit