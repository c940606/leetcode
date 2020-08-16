class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        import functools

        @functools.lru_cache(None)
        def dfs(left, right):
            if right < left:
                return 0
            return max(
                nums[left] + min(dfs(left + 2, right), dfs(left + 1, right - 1)),
                nums[right] + min(dfs(left, right - 2), dfs(left + 1, right - 1))
            )

        return (cur := dfs(0, len(nums) - 1)) >= sum(nums) - cur
