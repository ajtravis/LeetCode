class Solution(object):
    def digitSum(self, s, k):
        while len(s)>k:
            s1=""
            for i in range(0,len(s),k):
                s1+=str(sum([int(j) for j in s[i:i+k]]))
            s=s1
        return s