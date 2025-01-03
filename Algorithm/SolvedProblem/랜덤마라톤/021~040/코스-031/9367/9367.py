import math

NOT_USING = -1
INCONSISTENT = -1

def solve():
    n, m = map(int, input().split())
    car_info = {}
    for _ in range(n):
        car_name, p, q, k = input().split()
        car_info[car_name] = {"p": int(p), "q": int(q), "k": int(k)}

    rentals = []
    names = set()
    for _ in range(m):
        t, name, event, detail = input().split()
        rentals.append((int(t), name, event, detail))
        names.add(name)

    rentals.sort(key=lambda x: x[0])
    rental_info = {}
    price_info = {name: 0 for name in names}

    for t, name, event, detail in rentals:
        if price_info[name] == INCONSISTENT:
            continue

        if event == "p":
            car_name = detail
            if name in rental_info and rental_info[name]["t"] != NOT_USING:
                price_info[name] = INCONSISTENT
                continue
            if car_name not in car_info:
                price_info[name] = INCONSISTENT
                continue

            rental_info[name] = {"t": t, "car_name": car_name}
            price_info[name] += car_info[car_name]["q"]

        elif event == "r":
            distance = int(detail)
            if name not in rental_info or rental_info[name]["t"] == NOT_USING:
                price_info[name] = INCONSISTENT
                continue

            car_name = rental_info[name]["car_name"]
            rental_info[name]["t"] = NOT_USING
            price_info[name] += car_info[car_name]["k"] * distance

        elif event == "a":
            damage_rate = float(detail)
            if name not in rental_info or rental_info[name]["t"] == NOT_USING:
                price_info[name] = INCONSISTENT
                continue

            car_name = rental_info[name]["car_name"]
            damage_cost = math.ceil(car_info[car_name]["p"] * damage_rate / 100)
            price_info[name] += damage_cost

    sorted_names = sorted(names)

    for name in sorted_names:
        if rental_info.get(name, {"t": NOT_USING})["t"] != NOT_USING or price_info[name] == INCONSISTENT:
            print(f"{name} INCONSISTENT")
        else:
            print(f"{name} {price_info[name]}")

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()