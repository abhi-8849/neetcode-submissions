class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        parent = list(range(n))

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
                return False

        return True