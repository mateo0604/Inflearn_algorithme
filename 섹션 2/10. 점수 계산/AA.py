import sys

#sys.stdin = open("in2.txt","r")
n = int(input().strip())
scores = list(map(int,input().strip().split()))
results = 0
plus = 0

for s in scores:
    if s:
        plus+=1
        results+=plus
    else:
        plus =0
print(results)
