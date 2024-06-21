def dice_sum_ways(faces, dice, target):
    dp = [[0] * (target + 1) for _ in range(dice + 1)]
    dp[0][0] = 1

    for d in range(1, dice + 1):
        for t in range(1, target + 1):
            for face in range(1, faces + 1):
                if face <= t:
                    dp[d][t] += dp[d - 1][t - face]

    return dp[dice][target]

faces = 6
dice = 3
target = 8
print(dice_sum_ways(faces, dice, target))