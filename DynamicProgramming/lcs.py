# Longest common subsequences

# Approach 1: Brute force | recursive
# Time complexity : O(2^n), space complexity = ?
def lcs_recursive(str1, str2, index_of_str1, index_of_str2):
    """
    This function will return the length of longest common subsequence between two string
    :param str1: input string 1
    :param str2: input string 2
    :param index_of_str1:
    :param index_of_str2:
    :return: length of longest common subsequence
    """
    # base_condition
    if index_of_str1 == 0 or index_of_str2 == 0:
        return 0

    # divide into subproblem
    if str1[index_of_str1-1] == str2[index_of_str2-1]:
        return 1 + lcs_recursive(str1,str2, index_of_str1-1, index_of_str2-1)
    # case when str don't match
    return max (lcs_recursive(str1, str2, index_of_str1-1,index_of_str2), lcs_recursive(str1, str2, index_of_str1, index_of_str2-1))

# Approach 2: DP | memoization
# time complexity = O(mn)
lcs_memo = dict()
def lcs_dp(str1, str2, index_of_str1, index_of_str2):
    """
    This function will return the length of longest common subsequence between two string
    using DP memoization to optimize the recursive approach
    :param str1: input string 1
    :param str2: input string 2
    :param index_of_str1:
    :param index_of_str2:
    :return: length of longest common subsequence
    """
    # check if we already have the solution to the subproblem
    if (index_of_str1, index_of_str2) in lcs_memo:
        return lcs_memo[(index_of_str1, index_of_str2)]
    # base_condition
    if index_of_str1 == 0 or index_of_str2 == 0:
        return 0

    # divide into subproblem
    if str1[index_of_str1-1] == str2[index_of_str2-1]:
        lcs_memo[(index_of_str1, index_of_str2)] = 1 + lcs_recursive(str1,str2, index_of_str1-1, index_of_str2-1)
        return lcs_memo[(index_of_str1, index_of_str2)]
    # case when given strings don't match
    lcs_memo[(index_of_str1, index_of_str2)] = max (lcs_recursive(str1, str2, index_of_str1-1,index_of_str2), lcs_recursive(str1, str2, index_of_str1, index_of_str2-1))
    return lcs_memo[(index_of_str1, index_of_str2)]

# Approach 2: DP | tabulation
# time complexity = O(mn)
def lcs_dp_tab(str1, str2):
    # create map with 0 values as our prerequisite
    memo = dict()
    for i in range(len(str1)+1):
        memo[(i, 0)] = 0
    for i in range(len(str2)+1):
        memo[(0, i)] = 0

    for i in range(1,len(str1)+1):
        for j in range(1,len(str2)+1):
            if str1[i-1] == str2[j-1]:
                memo[(i,j)] = 1 + memo[(i-1,j-1)]
            else:
                memo[(i, j)] = max(memo[(i-1,j)],memo[(i,j-1)])
    return memo[(i,j)]

# test cases
string1 = "AGGTAB"
string2 = "GXTXAYB"
print(lcs_dp(string1, string2, len(string1), len(string2)))
print(lcs_dp_tab(string1, string2))