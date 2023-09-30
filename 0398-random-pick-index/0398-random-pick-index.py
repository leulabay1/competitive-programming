class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.hash_map = defaultdict(list)
        for r in range(len(self.nums)):
            self.hash_map[self.nums[r]].append(r)

    def pick(self, target: int) -> int:
        for val in self.hash_map:
            if val==target:
                k = random.choice(self.hash_map.get(val))
                return k

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)