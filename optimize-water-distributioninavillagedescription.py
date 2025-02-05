class Solution:
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        for i in range(len(wells)):
            pipes.append([0,i+1,wells[i]])
        pipes.sort(key = lambda x: x[2])
        self.parent = [i for i in range(n+1)]
        cost = 0
        print(self.parent)
        print(pipes)

        for house in pipes:
            x = house[0]
            y = house[1]
            px = self.find(x)
            py = self.find(y)
            if px != py:
                self.parent[py] = px
                cost += house[2]
        print(self.parent)
        return cost

        
        