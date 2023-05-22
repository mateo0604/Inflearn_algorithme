import sys

#sys.stdin = open("in1.txt","r")

cnt_a = int(input().strip())
list_a = list(map(int,input().strip().split()))

cnt_b = int(input().strip())
list_b = list(map(int,input().strip().split()))

list_a.extend(list_b)    
list_a.sort()
for i in list_a:
    print(i,end=' ')
