//Code

def plusMinus(arr):
    n = len(arr)
    p = ne = z= 0
    for i in arr:
        if i > 0:
            p += 1
        elif i < 0:
            ne+= 1
        else:
            z += 1
    po = p / n
    no = ne / n
    zo = z / n

    print(f"{po:.6f}")
    print(f"{no:.6f}")
    print(f"{zo:.6f}")

arr = [-4, 3, -9, 0, 4, 1]
plusMinus(arr)
