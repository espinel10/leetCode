class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        look=defaultdict(list)
        output=0
        for i,c in enumerate(s):
            look[c].append(i)
        def bs(lst,i):
            l,r=0,len(lst)
            while l<r:
                mid = (l+r)//2
                if i< lst[mid]:
                    r=mid
                else:
                    l=mid+1
            return l
        for w in words:
            prev=-1
            found = True
            for c in w:
                tmp=bs(look[c],prev)
                if tmp == len(look[c]):
                    found=False
                    break
                else:
                    prev = look[c][tmp]
            if found:
                output+=1
        return output
