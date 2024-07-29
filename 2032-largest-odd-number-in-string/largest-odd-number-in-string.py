class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        x = list(num)
        l = len(x)
        i = len(x)-1
        z = -1
        print(i)
        while i >= 0:
            print()
            if int(x[i]) % 2 != 0:
                z = i+1
                break
            i -= 1
        if z == -1:
           
            return ""
        elif z == 0:
           
            return str(x[0])
        else:
           
            return str("".join(x[:z]))


            
