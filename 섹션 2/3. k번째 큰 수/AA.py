def test(k,num_list):

    res = set()
    num_list.sort(reverse=True)
    for x in range(len(num_list)):
        for y in range(x+1,len(num_list)):
            for z in range(y+1,len(num_list)):
                res.add(num_list[x]+num_list[y]+num_list[z])
    res = sorted(list(res),reverse=True)

    return res[k-1]



    # max_1 = num_list.pop()
    # max_2 = num_list.pop()
    # while k > len(num_list):
    #     max_1,max_2 = max_2,num_list.pop()
    #     k -= len(num_list)
    # print(max_1)
    # print(max_2)
    # print(num_list)
    # return max_1 + max_2 + num_list[k-1]

if __name__ == '__main__':
    n,k = map(int,input().split())
    num_list = list(map(int,input().split()))
    print(test(k,num_list))