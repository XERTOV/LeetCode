class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new_nums = {}
        for i, item in enumerate (nums):
            new_nums[item] = i
            list(new_nums.keys())
        nums[:] = new_nums
        return len(nums)
        