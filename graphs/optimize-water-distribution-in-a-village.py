class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for index,cost in enumerate(wells):
            graph[0].append((cost , index + 1))
 
        
        for h1,h2,c in pipes:
            graph[h1].append((c , h2))
            graph[h2].append((c , h1))
            
        mst_set=set([0])
        
        heapq.heapify(graph[0])
        edges_heap = graph[0]
        
        tot_cost = 0
        
        while len(mst_set) < n +1:
            cost , next_house = heapq.heappop(edges_heap)
            if next_house not in mst_set:
                mst_set.add(next_house)
                tot_cost+=cost
                for new_cost , neighbor_house in graph[next_house]:
            
                    if neighbor_house not in mst_set:
                        heapq.heappush(edges_heap,(new_cost , neighbor_house))
        
        return tot_cost
