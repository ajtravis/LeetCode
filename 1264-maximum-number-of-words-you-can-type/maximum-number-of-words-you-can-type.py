class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        
        text = text.split(" ")
        words = len(text)
        letters = list(brokenLetters)
        print(letters)
        for w in text:
            for c in letters:
                if c in w:
                    words -= 1
                    break
        return words