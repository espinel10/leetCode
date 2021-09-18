##https://leetcode.com/problems/move-zeroes
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,j=0,1
        if len(nums)==1:
            return 
  
        while j<len(nums):
            #print(nums)
            if nums[i]==0 and nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j+=1
            elif nums[i]==0 and nums[j]==0:
                j+=1
            else:
                i+=1
                j+=1
