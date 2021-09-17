# https://leetcode.com/problems/rotate-array/

def reverse_inplace(nums, lo, hi):
    while lo < hi:
        nums[lo], nums[hi] = nums[hi], nums[lo]
        lo += 1
        hi -= 1


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        reverse_inplace(nums, 0, len(nums) - 1)
        reverse_inplace(nums, 0, k - 1)
        reverse_inplace(nums, k, len(nums) - 1)
