class Solution(object):
    def findMinHeightTrees(self, n, edges):
        if n <= 1:
            return [0]

        dict1, dict2 = defaultdict(int), defaultdict(list)

        for i,j in edges:
            dict1[i] += 1
            dict1[j] += 1
            dict2[i].append(j)
            dict2[j].append(i)

        stack = [i for i in range(n) if dict1[i] == 1]

        while stack:
            temp, ans = [], stack

            for leaves in stack:
                for neighbor in dict2[leaves]:
                    dict1[neighbor] -= 1

                    if dict1[neighbor] == 1:
                        temp.append(neighbor)

            stack = temp

        return ans
