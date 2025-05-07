class Solution:
    

    def findTheDifference(self, s: str, t: str) -> str:
        def count_elements(lst):
            count_dict = {}
            for item in lst:
                if item in count_dict:
                    count_dict[item] += 1
                else:
                    count_dict[item] = 1
            return count_dict
        
        def find_difference(a, b):
            all_keys = set(a.keys()).union(b.keys())
            for key in all_keys:
                if a.get(key) != b.get(key):
                    return key
            return None

        ds = count_elements(list(s))
        dt = count_elements(list(t))
        return find_difference(ds, dt)