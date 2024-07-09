class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        i = 0
        l = len(code)
        index = list(range(l))
         
        def helper(x, k = k):
            y = k
            match k:
                case k if k == 0:
                    return 0
                case k if k > 0:
                    total = 0
                    while y > 0:
                        x += 1
                        if x >= l:
                            x = 0
                        total += code[x]
                        y -= 1
                    return total
                case k if k < 0:
                    print(x)
                    total = 0
                    while y < 0:
                        x -= 1
                        print(y)
                        if x < 0:
                            x = l-1
                        total += code[x]
                        y += 1
                    return total
        
                    
        result = [helper(z) for z in index]
        return result
