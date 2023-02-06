class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        words = sorted(words, key = len)
      
        hash_ind = {}
        for i, val in enumerate(words):
            hash_ind[val] = i
        ans = [1] * len(words)
        for i in range(len(words)-1, -1, -1):
            word = words[i]
            for j in range(len(word)):
                new = word[:j] + word[j+1:]             
                if new in hash_ind:
                    ans[hash_ind[new]] = max( ans[hash_ind[new]], 1 + ans[hash_ind[word]])
  
        return max(ans)
