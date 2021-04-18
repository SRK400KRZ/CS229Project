def greedy_assignment(M):
    chosableCol = [i for i in range(len(M[0]))]
    ans = []
    for r in range(len(M)):
        minimum = M[r][0]
        minRen = 0
        for c in chosableCol:
            if minimum > M[r][c]:
                minimum = M[r][c]
                minRen = c
        chosableCol.remove(minRen)
        ans.append(minimum)
    return ans

# greedy_assignment(M)
# parameter: M is a list of lists of positive integers representing an n x n matrix
# return:    a list K = [k_0, k_1, k_2, ... ] of length n indicating the elements chosen from M.
#            k_0 is in row 0, k_1 is in row 1, etc, and all the k_i are in different columns of M.
# NOTE:      It's greedy! Let k_0 be the minimum of row 0. For i > 0, k_i is the minimum
#            element in row i that does not violate the constraint, "all selected elements
#            are in different columns."



M = [[9, 2, 7, 8],[6, 4, 3, 7],
[5, 8, 1, 8],[7, 6, 9, 4]]
for i in range(len(M)):
    for j in range(len(M)):
        print(M[i][j], end=" ")
    print()
print("Solution:", greedy_assignment(M))
