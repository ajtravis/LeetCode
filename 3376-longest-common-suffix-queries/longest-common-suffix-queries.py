class TrieNode:
    def __init__(self):
        self.children = {}
        self.ans = [5001,500001]

class Trie:
    def __init__(self):
        self.dict1 = TrieNode()

    def insert(self,word,idx):
        dict2 = self.dict1
        dict2.ans = min(dict2.ans,[len(word),idx])

        for i in word[::-1]:
            if i not in dict2.children:
                dict2.children[i] = TrieNode()
            dict2 = dict2.children[i]
            dict2.ans = min(dict2.ans,[len(word),idx])

    def find(self,word):
        dict2 = self.dict1 

        for i in word:
            if i not in dict2.children:
                break 
            dict2 = dict2.children[i]

        return dict2.ans[1]

class Solution:
    def stringIndices(self, wordsContainer, wordsQuery):
        trie = Trie()

        for i,j in enumerate(wordsContainer):
            trie.insert(j,i)

        return [trie.find(w[::-1]) for w in wordsQuery]