### https://leetcode.com/problems/first-bad-version
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=1
        b=n
        if n==1:
            return 1
        ant=0
        resp=-1
        while True:
            mid=a+((b-a)//2)
            #print(mid)
            if mid==ant:
                break
            ant=mid
            if isBadVersion(mid) == False:
                a=mid
            else:
                resp=mid
                b=mid
        
        if resp==-1:
            return n
        return resp
