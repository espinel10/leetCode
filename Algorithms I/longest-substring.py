##https://leetcode.com/problems/longest-substring-without-repeating-characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        max_sum=1
        s+=s[-1]
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                value=len(set(s[i:j]))
                if value!=len(s[i:j]):
                    break
                value=len(set(s[i:j]))
                max_sum=max(max_sum,value)
        return max_sum
