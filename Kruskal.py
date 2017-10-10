def init(namefile):
    f = open(namefile)
    numbers = map(lambda x: int(x),f.readline().split(" "))
    if len(numbers) == 2:
        sodinh = numbers[0]
        socanh = numbers[1]
        lit = []*socanh
        for i in range(socanh):
            numbers = map(lambda x: int(x),f.readline().split(" "))
            lit.append(numbers)
    return sodinh, lit
def find(father,u):
    while father[u]!=u:
        u = father[u]
    return u
def kruskal(n,dsCanh):
    lit = []
    father = [i for i in range(n)]
    dsCanh.sort(key= lambda ver: ver[2])
    i = 0
    while len(lit)<n and i<len(dsCanh):
        u = find(father,dsCanh[i][0]-1)
        v = find(father,dsCanh[i][1]-1)
        if u > v:
            father[u] = father[v]
            lit.append(dsCanh[i])
        elif u < v:
            father[v] = father[u]
            lit.append(dsCanh[i])
        i+=1
    return lit
n, dsCanh = init("c:\\Users\PHAM_DUNG\\myproject\\algorithm\\algorithm_pttkgt\\danhsachcanh.txt")
print kruskal(n, dsCanh)
