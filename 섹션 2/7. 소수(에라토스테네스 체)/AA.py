def test(n):
    num_list = [i for i in range(2,n+1)]


    for num in num_list:
        if not num:
            continue
        for i in range(2,(n//num)+1):
            num_list[(num*i)-2] = 0
    num_list = [i for i in num_list if i]
    print(len(num_list))
if __name__=="__main__":
    n = int(input().strip())
    test(n)