


res = []
asteroids = [-10,-2,-9,15]
for a in asteroids:
    while res and a * res[-1] < 0:
        if abs(a) > abs(res[-1]):
            res.pop()
            continue
        elif abs(a) == abs(res[-1]):
            res.pop()
        break
    else:
        res.append(a)

print(res)