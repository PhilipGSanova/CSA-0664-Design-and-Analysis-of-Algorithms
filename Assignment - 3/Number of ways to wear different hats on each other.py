from functools import lru_cache

class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(hats)
        hat_to_people = [[] for _ in range(41)]
        for i, h in enumerate(hats):
            for j in h:
                hat_to_people[j].append(i)
        
        @lru_cache(None)
        def dp(i, mask):
            if i == 41:
                return int(mask == (1 << n) - 1)
            res = dp(i + 1, mask)
            for p in hat_to_people[i]:
                if mask & (1 << p) == 0:
                    res += dp(i + 1, mask | (1 << p))
            return res % MOD
        
        return dp(1, 0)
