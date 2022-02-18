class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        def search_ud(u,d):
            while u<=d:
                pivot=(u+d)//2
                if matrix[pivot][0] <= target <= matrix[pivot][-1]:
                    return pivot
                else:
                    if target < matrix[pivot][-1]:
                        d=pivot-1
                    else:
                        u=pivot+1
            return -1
        
        def search_lr(l,r,k):
            while l<=r:
                pivot=(l+r)//2
                if matrix[k][pivot]==target:
                    return True
                else:
                    if target < matrix[k][pivot]:
                        r=pivot-1
                    else:
                        l=pivot+1
            return False
        
        K=search_ud(0,len(matrix))
        
        return search_lr(0,len(matrix[0]),K)
        
