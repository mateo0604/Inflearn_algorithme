def test(s,e,k,num_list):
    num_list = sorted(num_list[s-1:e])
    return num_list[k-1]

if __name__ == "__main__":
    case_cnt = int(input())
    results = list()
    for i in range(case_cnt):
        n,s,e,k = map(int,input().split())
        num_list = list(map(int,input().split()))
        results.append(test(s,e,k,num_list))
    for idx,r in enumerate(results):
        print(f"#{idx+1} {r}")