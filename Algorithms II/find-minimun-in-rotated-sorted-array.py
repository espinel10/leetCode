class Solution:
    def findMin(self, nums: List[int]) -> int:
    
        def find_k(l,r):
            if nums[l] < nums[r] or l==r:
                return 0
            while l<=r:
                pivot = (l+r)//2
                if nums[pivot] > nums[pivot+1]:
                    return pivot+1
                else:
                    if nums[pivot] < nums[l]:
                        r= pivot -1
                    else:
                        l= pivot +1
                              
        return nums[find_k(0,len(nums)-1)]
        
