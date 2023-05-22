import sys

#sys.stdin = open("in1.txt","r")

s = input().strip()

number = 0
divisor = 0

for i in s:
    if i.isdecimal():
        number = number*10 + int(i)
        
print(number)

for i in range(1,number+1):
    if number%i == 0 :
        divisor += 1
print(divisor)
