import sys

#sys.stdin = open("in1.txt","r")

n = int(input().strip())

grid = list(list(map(int,input().strip().split())) for _ in range(n))

m = int(input().strip())

order = list(list(map(int,input().strip().split())) for _ in range(m))


# 회전 수행

for o in order:
    # 행
    row = o[0]-1
    # 방향
    dit = o[1]
    # 회전 수
    rotate = o[2] % n

    # 오른쪽이면
    if dit :
        grid[row] = grid[row][-rotate:] + grid[row][:-rotate]
    # 왼쪽이
    else:
        grid[row] = grid[row][rotate:] + grid[row][:rotate]

# 모래시계 구하기
start = 0
end = n
result = 0
for i in range(n):
    result += sum(grid[i][start:end])
    if i < n//2:
        start += 1
        end -= 1
    else:
        start -= 1
        end +=1
print(result)
        
