from collections import deque

class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        N = len(graph)
        queue = deque()
        seen = set()
        
        # Inicializa a fila com todos os nós como pontos de partida
        for i in range(N):
            mask = 1 << i
            queue.append((i, mask, 0))  # (nó, nós visitados, passos)
            seen.add((i, mask))
        
        # BFS
        while queue:
            node, mask, dist = queue.popleft()
            if mask == (1 << N) - 1:
                return dist  # todos os nós visitados!
            
            for neighbor in graph[node]:
                next_mask = mask | (1 << neighbor)
                state = (neighbor, next_mask)
                if state not in seen:
                    seen.add(state)
                    queue.append((neighbor, next_mask, dist + 1))
        
        return -1  # nunca deveria chegar aqui
