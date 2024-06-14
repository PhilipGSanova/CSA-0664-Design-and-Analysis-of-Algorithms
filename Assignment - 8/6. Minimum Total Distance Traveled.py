def min_total_distance_traveled(robots, factories):
    robots.sort()
    factories.sort()

    r_len = len(robots)
    f_len = len(factories)

    dp = [[float('inf')] * (f_len + 1) for _ in range(r_len + 1)]
    dp[0][0] = 0

    for i in range(r_len + 1):
        dp[i][0] = 0

    for j in range(1, f_len + 1):
        dp[0][j] = 0

    for i in range(1, r_len + 1):
        for j in range(1, f_len + 1):
            dp[i][j] = dp[i][j-1]

            limit_j = factories[j-1][1]
            total_distance = 0

            for t in range(1, min(limit_j, i) + 1):
                total_distance += abs(robots[i-t] - factories[j-1][0])
                dp[i][j] = min(dp[i][j], dp[i-t][j-1] + total_distance)

    return dp[r_len][f_len]

robots = [0, 4, 6]
factories = [[2, 2], [6, 2]]
print(min_total_distance_traveled(robots, factories)) 