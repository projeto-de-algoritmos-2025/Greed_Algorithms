def minimal_lateness(tasks):
    tasks.sort(key=lambda x: x[1])  # Ordena por deadline (crescente)
    current_time = 0
    max_lateness = 0
    for t, d in tasks:
        current_time += t
        lateness = max(0, current_time - d)
        if lateness > max_lateness:
            max_lateness = lateness
    return max_lateness