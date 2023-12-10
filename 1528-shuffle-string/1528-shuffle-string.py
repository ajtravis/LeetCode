class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # Create a list to store characters in the shuffled order
        shuffled = [''] * len(s)

        # Iterate through the string and assign characters to their corresponding positions
        for i, char in enumerate(s):
            shuffled[indices[i]] = char

        # Join the list of characters to form the shuffled string
        result = ''.join(shuffled)
        return result