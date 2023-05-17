from collections import defaultdict
def test(cnt,scores):
    avg = int(round(sum(scores)/cnt,0))
    nums = defaultdict(set)

    for c in scores:
        nums[abs(avg-c)].add(c)

    min_score = sorted(nums[min(nums)])[-1]

    print(f"{avg} {scores.index(min_score)+1}")


if __name__ == "__main__":
    cnt = int(input().strip())
    scores = list(map(int,input().strip().split())) 
    test(cnt,scores)
    # print(test(cnt,scores))    