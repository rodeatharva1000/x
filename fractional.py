w = [40, 30, 90]
v = [7, 20, 10]
c = 140

x = [val/wei for val, wei in zip(v, w)]
n = sorted([(val, wei, fra) for val, wei, fra in zip(v, w, x)], key=lambda x:x[2], reverse=True)

ans = 0
for val, wei, fra in n:
    if c >= wei:
        c -= wei
        ans += val
    else:
        ans += val * (c/wei)
        break

print(ans)
