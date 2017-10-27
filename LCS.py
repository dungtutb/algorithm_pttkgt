def Max(a,b):
    if a>b: 
        return a
    else:
        return b
def LCS_helper(strX,strY):
    T = [[0 for i in range(len(strY)+1)] for j in range(len(strX)+1)]
    for i in range(1,len(strX)+1):
        for j in range(1,len(strY)+1):
            if strX[i-1] == strY[j-1]:
                T[i][j] = 1 + T[i-1][j-1]
            else:
                T[i][j] = Max(T[i-1][j],T[i][j-1])
    return T
def backtrack(T,strX,strY):
    lcs = ""
    i = len(strX)
    j = len(strY)
    while i>0 and j>0:
        if strX[i-1] == strY[j-1]:
            lcs = lcs + strX[i-1]
            i-=1
            j-=1
        else:
            if T[i-1][j] >= T[i][j-1]:
                i-=1
            else: j-=1
    return lcs
def LCS(strX, strY):
    T = LCS_helper(strX,strY)
    for i in range(len(strX)+1):
        print T[i]
    lcs = backtrack(T,strX,strY)
    print lcs[::-1]
LCS("ACGGA","ACTG")


    

