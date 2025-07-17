class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        from collections import Counter
        c=Counter(nums)
        for item in c.keys():
            if c[item] > len(nums)//2:
                return item
