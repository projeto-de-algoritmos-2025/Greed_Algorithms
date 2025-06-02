class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        total = sum(stones)
        half = total // 2
        dp = [0] * (half + 1)

        for stone in stones:
            for j in range(half, stone - 1, -1):
                dp[j] = max(dp[j], dp[j - stone] + stone)
        
        return total - 2 * dp[half]
