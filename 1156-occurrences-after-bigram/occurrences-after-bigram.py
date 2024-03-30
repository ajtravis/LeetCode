class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        s=text.split()
        r=[]
        for i in range(len(s)-2):
            if s[i]==first and s[i+1]==second:
                r.append(s[i+2])
        return r
        