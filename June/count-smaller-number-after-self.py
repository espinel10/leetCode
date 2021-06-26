##Documentation http://www.grantjenks.com/docs/sortedcontainers/sortedlist.html#sortedcontainers.SortedList.bisect_left
##problem https://leetcode.com/problems/count-of-smaller-numbers-after-self/solution/

from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        s= SortedList()
        output=[]
        for n in nums[::-1]:
            ans=SortedList.bisect_left(s,n)
            output.append(ans)
            s.add(n)
        return output[::-1]
