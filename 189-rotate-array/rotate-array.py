class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
            k = k % len(nums)
            l = len(nums) - k
            n1 = nums[l:]
            n2 = nums[:l]
            nums[:] = n1 + n2
            return nums
        