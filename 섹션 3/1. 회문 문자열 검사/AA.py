import sys

#sys.stdin = open("in1.txt","r")

n = int(input().strip())
for i in range(n):
    s = input().strip()
    result = "YES"
    for x in range(len(s)):
        y = -1-x
        if x > len(s)/2:
            break
        
        if s[x].upper() != s[y].upper():
            result = "NO"
            break
        
    print(f"#{i+1} {result}")
