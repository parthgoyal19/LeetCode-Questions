# Last updated: 14/06/2026, 00:17:53
1class Solution:
2    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
3        ans = []
4
5        for word in words:
6            total = 0
7
8            for ch in word:
9                total += weights[ord(ch) - ord('a')]
10
11            remainder = total % 26
12            ans.append(chr(ord('z') - remainder))
13
14        return "".join(ans)