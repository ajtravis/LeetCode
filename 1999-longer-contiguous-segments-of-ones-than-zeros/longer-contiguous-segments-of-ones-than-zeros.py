class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        def longest_streak(x):
            max_streak = 0
            current_streak = 0

            for bit in s:
                if bit == x:
                    current_streak += 1
                    max_streak = max(max_streak, current_streak)
                else:
                    current_streak = 0

            return max_streak
        zero = longest_streak('0')
        one = longest_streak('1')
        
        if one > zero:
            return True
        else:
            return False