# with memo - n, n
# without memo 2^n, n
store = {}
def fabo(n):
    if n <= 1:
        store[n] = n
        return n
    if n in store:
        return store[n]
    res = fabo(n-1)+fabo(n-2)
    store[n] = res
    return res
fabo(500)

for x, y in sorted(store.items()):
    print(x, y)


# n, 1
n = 100
a = -1
b = 1
for i in range(n):
    c = a+b
    print(c)
    a = b
    b = c
