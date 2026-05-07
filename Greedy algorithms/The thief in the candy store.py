def main():
    import sys

    data = sys.stdin.read().strip().split()
    if not data:
        return

    n, W = int(data[0]), int(data[1])
    cakes = []
    idx = 2
    for _ in range(n):
        p = int(data[idx])
        s = int(data[idx + 1])
        idx += 2
        cakes.append((p, s))

    # Сортируем по убыванию цены за единицу объёма
    cakes.sort(key=lambda x: x[0] / x[1], reverse=True)

    total_value = 0.0
    remaining_capacity = W

    for price, volume in cakes:
        if remaining_capacity >= volume:
            total_value += price
            remaining_capacity -= volume
        else:
            total_value += price * (remaining_capacity / volume)
            break

    print(f"{total_value:.2f}")


if __name__ == "__main__":
    main()