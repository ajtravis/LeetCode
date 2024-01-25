class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = []
        sep = [list(word) for word in words]
        for char in sep[0]:
            flag = 0
            for x in range(1,len(sep)):
                if char not in sep[x]:
                    flag = 1
                    break
            if flag == 0:
                result.append(char)
                for x in range(1,len(sep)):
                    sep[x].remove(char)
                
        return result