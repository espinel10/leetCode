class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(defaultdict)
        
        
        def dfs(curr_node , target_node , acum_product,visited):
            visited.add(curr_node)
            ret=-1.0
            neighbors=graph[curr_node]
            if target_node in neighbors:
                ret=acum_product * neighbors[target_node]
            else:
                for neighbor , value in neighbors.items():
                    if neighbor in visited:
                        continue
                    ret = dfs(neighbor,target_node,acum_product * value ,visited)
                    if ret !=-1.0:
                        break
            return ret
        
        for (dividend,divisor) , value in zip(equations,values):
            graph[dividend][divisor]=value
            graph[divisor][dividend]=1 / value
            
        results=[]
        
        
        for dividend , divisor in queries:
            ret=-1.0
            if dividend not in graph or divisor not in graph:
                ret=-1.0
            elif dividend==divisor:
                ret=1.0
            else:
                visited=set()
                ret = dfs(dividend,divisor,1,visited)
            results.append(ret)
    
        
        return results
