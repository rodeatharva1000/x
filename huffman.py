import heapq

class Node:
    def __init__(self, c, f):
        self.c = c
        self.f = f
        self.l = None
        self.r = None

    def __lt__(self, o):
        return self.f < o.f
    
l = [('a', 5), ('b', 3), ('c', 7), ('d', 11), ('e', 2)]
h = []
for c, f in l:
    heapq.heappush(h, Node(c, f))

while len(h) > 1:
    t1 = heapq.heappop(h)
    t2 = heapq.heappop(h)
    n = Node(None, t1.f+t2.f)
    n.l, n.r = t1, t2
    heapq.heappush(h, n)

head = h[0]
t = {}

def trav(n, p=""):
    if n is None:
        return
    if n.c is not None:
        t[n.c] = p
        return
    trav(n.l, p+"0")
    trav(n.r, p+"1")

trav(head)
for a, b in t.items():
    print(a, b)

