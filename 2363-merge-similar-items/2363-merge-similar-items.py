class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        pairs = {}
        result = []
        for i in items1:
            pairs[i[0]] = i[1]
        for i in items2:
            if i[0] in pairs:
                pairs[i[0]] += i[1]
            else:
                pairs[i[0]] = i[1]
        sorted_pairs = dict(sorted(pairs.items()))
        for x,y in sorted_pairs.items():
            result.append([x, y])
        return result
