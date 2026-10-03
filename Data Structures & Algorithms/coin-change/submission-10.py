class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(rem):
            if rem in memo:
                return memo[rem]
            if rem == 0:
                return 0
            best = amount + 1
            for c in coins:
                if c <= rem:
                    best = min(best, dp(rem - c) + 1)
            memo[rem] = best
            return best
        res = dp(amount)
        return res if res <= amount else -1
                