class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result = []
        def invert(x):
            new_arr = []
            for y in x:
                if y == 0:
                    new_arr.append(1)
                else:
                    new_arr.append(0)
            return new_arr
        for arr in image:
            arr.reverse()
            result.append(invert(arr))
        return result