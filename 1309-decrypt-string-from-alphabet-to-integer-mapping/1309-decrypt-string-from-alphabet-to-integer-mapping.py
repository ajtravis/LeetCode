class Solution:
    def freqAlphabets(self, s: str) -> str:
        hash_map = {}
        result = ""
        # Characters 'a' to 'i'
        for i in range(1, 10):
            char = chr(i + ord('a') - 1)
            hash_map[str(i)] = char

        # Characters 'j' to 'z'
        for i in range(10, 27):
            char = chr(i + ord('a') - 1)
            hash_map[str(i)] = char
        i = 0
        while i < len(s):
            if i < len(s)-2 and s[i+2] == '#':
                result += hash_map[s[i]+ s[i+1]]
                print(result)
                i+=3
            else:
                result += hash_map[s[i]]
                i+=1
        return result  
        
            