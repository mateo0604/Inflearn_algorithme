import sys

#sys.stdin = open("in1.txt","r")
result = list()

for i in range(1,21):
    result.append(str(i))
    
for i in range(10):
    ai,bi = map(int,input().strip().split())
    temp = result[ai-1:bi]
    result[ai-1:bi] = temp[::-1]
print(' '.join(result))
    
    
