import DFS

def duyet(mang_vertex,matran):
    cur_time = 1
    not_end=True
    group = 1
    # buoc 1
    while not_end:
        not_end=False
        for i in range(len(mang_vertex)):
            if mang_vertex[i].start_time == 0:
                not_end = True
                mang_vertex[i].group = group
                cur_time = DFS.Dfs(mang_vertex,matran,i,cur_time)
                cur_time += 1
                group += 1
                break
def Kosaraju(mang_vertex,matran):
    duyet(mang_vertex,matran)
    print "Sau buoc 1:"
    for i in range(len(mang_vertex)):
        print "dinh %d: %d %d %d" %(i+1,mang_vertex[i].start_time,mang_vertex[i].end_time,mang_vertex[i].group)
    #buoc 2  
    DFS.reverse_matrix(matran)
    #buoc 3
    mang_vertex.sort(key= lambda ver: ver.end_time,reverse=True) # sap xep theo thu tu giam dan end_time
    for i in range(len(mang_vertex)):
        mang_vertex[i].reset()
    duyet(mang_vertex,matran)
    mang_vertex.sort(key=lambda ver: ver.index)
    print "Sau buoc 3:"
    for i in range(len(mang_vertex)):
        print "dinh %d: %d %d %d" %(i+1,mang_vertex[i].start_time,mang_vertex[i].end_time,mang_vertex[i].group)

matran = DFS.init('c:\\Users\PHAM_DUNG\\myproject\\algorithm\\algorithm_pttkgt\\input_kosaraju.txt')
mang_vertex = [DFS.Vertex(index=i) for i in range(matran.height)]
Kosaraju(mang_vertex,matran)