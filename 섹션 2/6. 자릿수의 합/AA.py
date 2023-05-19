def digit_sum(x):
    max_num = 0
    result = None
    for num in x:
        tot = 0
        for n in num:
            tot+=int(n)
        if max_num<tot:
            max_num = tot
            result = num
    print(result)
    

if __name__ == "__main__":
    cnt = int(input().strip())
    numbers = input().strip().split()
    digit_sum(numbers)