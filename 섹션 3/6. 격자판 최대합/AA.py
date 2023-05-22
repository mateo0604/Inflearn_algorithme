import sys

#sys.stdin = open("in1.txt","r")

n = int(input().strip())

grid = list()

max = 0
for _ in range(n):
    grid.append(list(map(int,input().strip().split())))

for i in range(n):
    val_1 = 0
    val_2 = 0

    # 각 행
    val_1 = sum(grid[i])

    # 각 열
    for j in range(n):
        val_2 += grid[j][i]

    if max < val_1:
        max = val_1

    if max < val_2:
        max = val_2

for i in range(n):
    val_3 = 0
    val_4 = 0

    val_3 += grid[i][i]
    val_4 += grid[i][n-1-i]

    if max < val_3:
        max=val_3
    if max < val_4:
        max = val_4
        
print(max)

        
