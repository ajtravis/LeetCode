class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        lst = list(s)
    
        # Initialize the start and end indices for the string reversal
        start = 0
        end = len(lst) - 1

        while start < end:
            # If the start index does not point to an English letter, move it forward
            if not lst[start].isalpha():
                start += 1
            # If the end index does not point to an English letter, move it backward
            elif not lst[end].isalpha():
                end -= 1
            # If both the start and end indices point to English letters, swap them
            else:
                lst[start], lst[end] = lst[end], lst[start]
                start += 1
                end -= 1

        # Join the list of characters into a string and return it
        return ''.join(lst)