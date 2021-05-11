class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pass
        seen , n = set() ,len(s)
        right , res = -1 ,0
        for left in range(n):
            while right +1<n and s[right+1] not in seen:
                right+=1
                seen.add(s[right])
            res = max(res,right - left + 1)
            if right == n-1:
                break
            seen.discard(s[left])
        return res
        
