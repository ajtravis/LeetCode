class Solution:
    def maxPower(self, s: str) -> int:
        if not s:
            return 0
        
        max_power = 1
        current_char = s[0]
        current_power = 1

        for char in s[1:]:
            if char == current_char:
                current_power += 1
                max_power = max(max_power, current_power)
            else:
                current_char = char
                current_power = 1

        return max_power

