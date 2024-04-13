class Solution(object):
    def isArmstrong(self, n):
        """
        :type n: int
        :rtype: bool
        """
        k=[]
        for i in str(n):
            j=int(i)**len(str(n))
            k.append(j)
        if sum(k)==int(n):
            return True
        else:
            return False
        