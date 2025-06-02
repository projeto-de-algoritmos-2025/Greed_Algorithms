import heapq
def interval_partitioning(intervals):
    intervals.sort(key=lambda x: x[0])  # Ordena por início (crescente)
    resources = []  # Heap para fins de intervalos
    for start, end in intervals:
        if resources and resources[0] <= start:
            heapq.heappop(resources)  # Reutiliza recurso
        heapq.heappush(resources, end)
    return len(resources)