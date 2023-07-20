lst = list(map(int, input().split()))
def count_Sort(lst):
    ans = []
    res=[0 for i in  range(10)]
    n=len(lst)
    for i in range(n):
        res[lst[i]] += 1
    for i in range(len(res)):
         while res[i]>0:
             ans.append(i)
             res[i]-=1
    return ans
print(count_Sort([1, 3, 1]))
print(count_Sort(lst))
