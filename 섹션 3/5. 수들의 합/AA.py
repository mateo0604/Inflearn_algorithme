import sys

#sys.stdin = open("in1.txt","r")

n,m = map(int,input().strip().split())
nums = list(map(int,input().strip().split()))
cnt = 0

start=end=val=0


while start < n and end < n:
    
    val += nums[end]
    if val < m :
        end += 1
        continue
    elif val == m :
        cnt +=1

    val=0
    start = end = start+1

print(cnt)
    
        
        
        
