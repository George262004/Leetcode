class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        def reverse(l,r):
            while l < r:
                nums[l],nums[r] = nums[r],nums[l]
                l += 1
                r -= 1

        reverse(0,len( nums) - 1)
        reverse(0,k - 1)
        reverse(k,len( nums ) - 1)
