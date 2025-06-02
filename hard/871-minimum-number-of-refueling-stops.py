import heapq

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        heap = []  # max-heap (valores negativos)
        res = 0
        i = 0
        fuel = startFuel

        while fuel < target:
            # Adiciona todos os postos ao alcance
            while i < len(stations) and stations[i][0] <= fuel:
                heapq.heappush(heap, -stations[i][1])  # max-heap
                i += 1

            # Se não tem mais postos para abastecer, falha
            if not heap:
                return -1

            # Abastece no maior posto disponível
            fuel += -heapq.heappop(heap)
            res += 1

        return res
