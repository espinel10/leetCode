##https://leetcode.com/problems/binary-search/submissions/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a=0
        b=len(nums)
        if len(nums)==1:
            if nums[0]==target:
                return 0
            else:
                return -1
        ant=0
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
        return resp
