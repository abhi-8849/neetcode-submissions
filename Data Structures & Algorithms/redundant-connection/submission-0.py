class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) 
        parent = list(range(n+1))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]

            return x

        def union(u,v):
            ru, rv = find(u), find(v)

            if ru == rv:
                return False

            parent[ru] = rv
            return True

        for u,v in edges:
            if not union(u,v):
                return [u,v]