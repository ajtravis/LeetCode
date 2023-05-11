class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        def helper(char, i):
            i += 1
            y = ''
            chars = char.split()
            vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
            first = chars[0][0]
            if first in vowels:
                chars.append('ma') 
                a = 'a' * i
                chars.append(a)
                return y.join(chars)
            else:   
                end = [x for x in chars[0][1:]]
                end.append(first)
                end.append('ma')
                a = 'a' * i
                end.append(a)
                return y.join(end)
                
        result = []
        s = sentence.split(" ")
        for i, c in enumerate(s):
            r = helper(c, i)
            result.append(r)
        z = " "
        return z.join(result)