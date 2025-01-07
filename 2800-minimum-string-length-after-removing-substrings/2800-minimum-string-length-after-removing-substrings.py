class Solution:
    def minLength(self, s: str) -> int:
        i = 0
        while i < len(s)-1:
            cur = s[i]
            nxt = s[i+1]
            if cur == "A" and nxt == "B" or cur == "C" and nxt == "D":
                if i == 0:
                    s = s[2:]
                    print(s)
                else:
                    
                    s = s[0:i] + s[i+2:]
                    print(s)
                i = 0
            else:
                i+=1
        return len(s)