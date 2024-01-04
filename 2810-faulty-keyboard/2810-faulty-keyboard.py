class Solution:
    def finalString(self, s: str) -> str:
        result = []
        def add_char(c):
            if c != 'i':
                result.append(c) 
            else:
                if len(result) > 0:
                    result.reverse()
            return
        chars = list(s)
        for c in chars:
            add_char(c)
        joined = ('').join(result)
        
        return joined