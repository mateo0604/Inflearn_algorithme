import sys

# sys.stdin = open("in1.txt","r")

n = int(input().strip())

grid = list(list(map(int,input().strip().split())) for _ in range(n))


cnt = 0
for i in range(n):
    for j in range(n):
        val = grid[i][j]
        up = 0 if i-1 < 0 else grid[i-1][j]
        down = 0 if i+1 >= n else grid[i+1][j]
        left= 0 if j-1 < 0 else grid[i][j-1]
        right = 0 if j+1>=n else grid[i][j+1]

        if val > up and val > down and val > left and val > right:
            cnt += 1

print(cnt)
