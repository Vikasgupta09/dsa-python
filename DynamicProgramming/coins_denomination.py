# count sum using coin denominations

comb = dict()
def sum_all (arr):
    print(arr)
    sum = 0
    for num in arr:
        sum += num
    return sum

def count_sum_rec(coins, sum, index):
    # base case
    if index == len(coins):
        return 0
    if sum == 0:
        return 1

    count = count_sum_rec(coins, sum, index+1)
    if coins[index] <= sum:
        count += count_sum_rec(coins, sum-coins[index], index)

    return count

print(count_sum_rec([1,2,3],4,0))

dp = dict()
def count_sum_dp(coins, sum):
    for i in range(len(coins)+1):
        dp[(0,i)] = 1
    for i in range(1,sum+1):
        dp[(i,0)] = 0

    for i in range(1,sum+1):
        for j in range(1,len(coins)+1):
            dp[(i, j)] = dp[(i, j-1)]
            if coins[j-1] <= i:
                dp[(i, j)] += dp[(i-coins[j-1], j)]

    return dp[(i, j)]

print(count_sum_dp([1,2,3],4))