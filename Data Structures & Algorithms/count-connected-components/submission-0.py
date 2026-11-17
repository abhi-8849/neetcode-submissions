from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        seen = set()
        count = 0

        for start in range(n):
            if start in seen:
                continue

            count += 1
            seen.add(start)
            q = deque([start])

            while q:
                node = q.popleft()

                for nei in graph[node]:
                    if nei not in seen:
                        seen.add(nei)
                        q.append(nei)

        return count