def interval_scheduling(intervals):
    intervals.sort(key=lambda x: x[1])  # Ordena por término (crescente)
    selected = []
    last_end = -float('inf')
    for start, end in intervals:
        if start >= last_end:
            selected.append((start, end))
            last_end = end
    return selected