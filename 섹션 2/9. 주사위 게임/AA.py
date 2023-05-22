import sys,os

def test(s):
    set_s = set(s)
    amount = 0
    if len(set_s) < 2 :
        amount = 10000 + (set_s.pop()*1000)
    elif len(set_s) < 3:
        max_num = 0
        for i in s:
            if max_num < s.count(i):
                max_num = i
        amount = 1000 + (max_num*100)
    else:
        amount = max(set_s)*100
    return amount

#sys.stdin = open("in1.txt","r")
n = int(input().strip())
results = list()
for i in range(n):
    s = list(map(int,input().strip().split()))
    results.append(test(s))

print(max(results))


        
    
