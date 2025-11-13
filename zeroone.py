w = [0, 40, 30, 90, 20]
v = [0, 7, 20, 10, 1]
c = 90

n = len(v) - 1

dp = [[0] * (c + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for cap in range(1, c + 1):
        if w[i] <= cap:
            dp[i][cap] = max(
                dp[i-1][cap],                      # not taking item
                v[i] + dp[i-1][cap - w[i]]         # taking item
            )
        else:
            dp[i][cap] = dp[i-1][cap]              # can't take item

print(dp[n][c])
