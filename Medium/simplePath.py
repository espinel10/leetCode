class Solution:
    def simplifyPath(self, path: str) -> str:
        pass
        path=path.split("/")
        while path.count('')>0:
            path.remove('')
        pilar=[]
        for arch in path:
            if arch=='..':
                if len(pilar)>0:
                    pilar.pop()
            else:
                if arch=='.':
                    continue
                else:
                    pilar.append(arch)
        return "/"+"/".join(pilar)
