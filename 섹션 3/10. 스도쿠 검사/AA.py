import sys

#sys.stdin = open("in1.txt","r")

grid = list(list(map(int,input().strip().split())) for _ in range(9))


t = {1,2,3,4,5,6,7,8,9}

result = True


def test(grid):
    #행 / 열끼리 비교
    for i in range(9):
        ch1 = [0]*9
        ch2 = [0]*9
        
        for j in range(
            9):      
            ch1[grid[i][j]-1]=1
            ch2[grid[j][i]-1]=1
            
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False

    ch3 = {0:[0]*9,1:[0]*9,2:[0]*9}
    for i in range(9):
        if i!=0 and i%3 ==0:
            for val in ch3.values():
                if sum(val) != 9 :
                    return False
            ch3 = {0:[0]*9,1:[0]*9,2:[0]*9}
        for j in range(9):
            ch3[j//3][grid[i][j]-1]=1
    return True

if test(grid):
    print('YES')
else:
    print('NO')

        
