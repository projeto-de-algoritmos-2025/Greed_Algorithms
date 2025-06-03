import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # Passo 1: filtrar cursos impossíveis
        courses = [c for c in courses if c[0] <= c[1]]
        
        # Passo 2: ordenar por prazo final (lastDay)
        courses.sort(key=lambda x: x[1])
        
        heap = []  # Max-heap (armazenamos durações como negativos)
        time = 0   # Tempo acumulado
        
        for dur, end in courses:
            # Caso 1: Curso cabe na agenda atual
            if time + dur <= end:
                time += dur
                heapq.heappush(heap, -dur)  # Armazena -dur para simular max-heap
            
            # Caso 2: Substituir curso mais longo se vantajoso
            elif heap and dur < -heap[0]:
                removed = -heapq.heappop(heap)  # Remove o maior curso atual
                time += dur - removed           # Atualiza o tempo
                heapq.heappush(heap, -dur)       # Adiciona novo curso
                
        return len(heap)