class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        l=0
        j=0
        salida=0
        last=-1
        
        for i,n in enumerate(nums):
            if n < left:
                if j>0:
                    salida+=j+l
                    salida-=i-last -1
                l+=1
            elif left <= n <= right:
                salida+=j+l+1
                j+=1
                last=i
            else:
                l=0
                j=0
        return salida
                    
