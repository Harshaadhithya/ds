def diagonalSum(mat):
    """Method - 1""" #Refer the docs for explanation

    # sum = 0
    # n = len(mat)
    # for row_ind in range(len(mat)):
    #     for col_ind in range(len(mat[row_ind])):
    #         print(row_ind,col_ind)
    #         if row_ind == col_ind or row_ind + col_ind == n - 1:
    #             print("yes",mat[row_ind][col_ind])
    #             sum += mat[row_ind][col_ind]


    """Method - 2 """
    sum=0
    n=len(mat)

    for ind in range(n):
        sum+=mat[ind][ind]
        sum+=mat[ind][(n-1)-ind]

    if n % 2 == 1:
        sum -= mat[int(n / 2)][int(n / 2)]
        """this is because, in above loop ,
         in each row we are trying to get both diagonal elements of that row.
         but if n=3, if current ind =1, then (n-1)-ind = (3-1)-1 = 1. 
         so when we add mat[ind][ind] and mat[ind][n-1-ind] both respresents the same element,
          but we should conider only one. so to avoid this condition in odd 'n' matrix we are doing this"""

    return sum

"""Note: in method 1 we are not subtracting if n id odd, because there we are iterating
 each element one after one using two loops. one for row and other for col.
 and inside the loop we have used if condition. if row == col or (row+col==n-1).
 in this case for n=3, row_ind=1,col_ind=1. even though this satisfies both the condition
  it just adds that value only once to the sum, because we are checking both the conditions
   in the same if block using OR operator.
    so if either of the condition is staisfied then it adds it to the sum. 
    so no duplicate addition is taken place here"""

print(diagonalSum([[1,2,3],[4,5,6],[7,8,9]]))
