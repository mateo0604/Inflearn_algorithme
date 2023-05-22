import sys

#sys.stdin = open("in1.txt","r")

n = int(input().strip())

grid = list(list(map(int,input().strip().split())) for _ in range(n))

result = 0
start = end = n//2
for i in range(n):
    result += sum(grid[i][start:end+1])
    
    if i < n // 2 :
        start -= 1
        end += 1
    else:
        start +=1
        end -= 1
    

print(result)
        
