from collections import defaultdict
def test(n:int,m:int):
    tot_dict = defaultdict(int)
    n_list = [i+1 for i in range(n)]
    m_list = [i+1 for i in range(m)]
    results = []
    for i in n_list:
        for j in m_list:
            tot_dict[i+j]+=1
    for key,value in tot_dict.items():
        if value == max(tot_dict.values()):
            results.append(str(key))
    print(' '.join(results))

if __name__ == "__main__":
    n,m = map(int,input().strip().split())
    test(n,m)