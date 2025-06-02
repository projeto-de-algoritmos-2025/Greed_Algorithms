def coin_change(N, coins):
    coins.sort(reverse=True)  # Ordena moedas decrescentemente
    count = 0
    for coin in coins:
        while N >= coin:
            N -= coin
            count += 1
    return count if N == 0 else -1  # -1 se impossível