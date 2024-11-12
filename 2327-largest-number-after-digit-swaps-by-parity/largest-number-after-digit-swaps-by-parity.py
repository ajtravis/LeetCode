class Solution:
    def largestInteger(self, num: int) -> int:
        digits = []
        while num:
            digits.append(num % 10)
            num //= 10
        for i in range(len(digits) - 1, 0, -1):
            flag_odd_1 = digits[i] & 1
            for j in range(i - 1, -1, -1):
                if digits[i] < digits[j]:
                    flag_odd_2 = digits[j] & 1
                    if flag_odd_1 == flag_odd_2:
                        digits[i], digits[j] = digits[j], digits[i]
        num = 0
        for i in range(len(digits) - 1, -1, -1):
            num = num * 10 + digits[i]
        return num