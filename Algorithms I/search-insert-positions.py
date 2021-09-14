#####https://leetcode.com/problems/search-insert-position
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        a=0
        b=len(nums)-1
        if len(nums)==1:
            if nums[0]==target:
                return 0      
        mid=0
        ant=-99
        resp=-1
        while a!=b:
            mid=a+((b-a)//2)            
            if mid==ant:
                break
            ant=mid
            if target > nums[mid]:
                a=mid
            elif target < nums[mid]:
                b=mid
            else:
                resp=mid
                break
                
        if resp==-1:
            if nums[a] > target:
                resp=max(0,mid-1)
            else:
                resp=b
                if nums[-1] < target:
                    resp+=1
        return resp
