class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_k(l,r):
            if nums[l] < nums[r]:
                return 0
            while l<=r:
                pivot = (l + r) // 2
                if nums[pivot] > nums[pivot + 1]:
                    return pivot +1
                else:
                    if nums[pivot] < nums[l]:
                        r = pivot - 1
                    else:
                        l = pivot + 1
        def search(l,r):
            while l<=r:
                pivot = (l+r)//2
                if nums[pivot] == target:
                    return pivot
                else:
                    if target < nums[pivot]:
                        r=pivot-1
                    else:
                        l=pivot+1
            return -1
        n=len(nums)
        if n==1:
            return 0 if nums[0] == target else -1
        k=find_k(0,n-1)
        if nums[k]==target:
            return k
        if k==0:
            return search(0,n-1)
        if target < nums[0]:
            return search(k,n-1)
    
        return search(0,k)
