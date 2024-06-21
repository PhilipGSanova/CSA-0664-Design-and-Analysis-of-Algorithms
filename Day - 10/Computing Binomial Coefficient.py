def coef(n,k):
    C=[[0 for _ in range(k+1)]for _ in range(n+1)]

    for i in range(n+1):
        for j in range(min(i,k)+1):
            if i == j or j == 0:
                C[i][j]=1
            else:
                C[i][j]=C[i-1][j-1]+C[i-1][j]
    
    return C[n][k]

print(coef(4,2))