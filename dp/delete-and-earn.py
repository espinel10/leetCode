class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        for num in nums:
            points[num]+=num
        elements = sorted(points.keys())
        two_back=0
        one_back=points[elements[0]]
        
        for i in range(1 , len(elements)):
            curr = elements[i]
            if curr == elements[i-1]+1:
                two_back , one_back =one_back , max(one_back , two_back + points[curr])
            else:
                two_back , one_back = one_back, one_back + points[curr]
                
        return one_back
        
                    
