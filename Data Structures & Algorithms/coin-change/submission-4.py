from functools import cache
import sys
sys.setrecursionlimit(20000)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(total):
            if total == amount:
                return 0
            min_coins = amount + 1
            for c in coins:
                    if c <= (amount - total):
                        min_coins = min(min_coins, dp(total + c) + 1)
            return min_coins
        res = dp(0)
        return res if res <= amount else -1



        