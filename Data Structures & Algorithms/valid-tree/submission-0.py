from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        graph = [[] for _ in range(n)]

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        q = deque([0])
        seen = {0}

        while q:
            node = q.popleft()

            for nei in graph[node]:
                if nei not in seen:
                    q.append(nei)
                    seen.add(nei)

        
        return len(seen) == n