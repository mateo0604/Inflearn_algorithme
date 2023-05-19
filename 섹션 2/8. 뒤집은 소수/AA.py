def isPrime(x):
    return int(x[::-1])

def reverse(x):
    if x < 2 : return False
    
    for i in range(2,x):
        if x % i ==0:
            return False
    return True
if __name__ == "__main__":
    cnt = int(input().strip())
    numbers = input().strip().split()
    numbers = list(map(isPrime,numbers))
    numbers = [str(n) for n in numbers if reverse(n)]
    print(" ".join(numbers))