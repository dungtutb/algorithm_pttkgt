
class Vertex:
    
    def __init__(self,index=0,start_time=0,end_time=0,status=0,group=0):
        self.start_time = start_time
        self.end_time = end_time
        self.status = status
        self.index = index
        self.group = group
    def reset(self):
        self.start_time = 0
        self.end_time = 0
        self.status = 0
        self.group = 0
        
class MatranKe:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.Arr = [[0]*width]*height

def init(namefile):
    f = open(namefile)
    line = f.readline().split(" ")
    numbers = map(lambda x: int(x),line)
    if len(numbers) == 1:
        arr = MatranKe(numbers[0],numbers[0])        
        for i in range(arr.height):
            line = f.readline().split(" ")
            numbers = map(lambda x: int(x),line)   
            arr.Arr[i] = numbers
        f.close()
        return arr
    else:
        f.close()
        return MatranKe(0,0)
    
def Dfs(mang_vertex,matran,index,cur_time):
    mang_vertex[index].start_time = cur_time
    cur_time += 1
    mang_vertex[index].status = 1
    for i in range(len(mang_vertex)):
        if mang_vertex[i].status == 0 and matran.Arr[mang_vertex[index].index][mang_vertex[i].index]>0:
            mang_vertex[i].group = mang_vertex[index].group
            cur_time = Dfs(mang_vertex,matran,i,cur_time)
            cur_time += 1
    mang_vertex[index].status = 2
    mang_vertex[index].end_time = cur_time
    return cur_time  

def reverse_matrix(matran):
    for i in range(matran.height):
        for j in range(i+1,matran.width):
            temp = matran.Arr[i][j]
            matran.Arr[i][j] = matran.Arr[j][i]
            matran.Arr[j][i] = temp

def program():
    
    matran = init('c:\\Users\PHAM_DUNG\\myproject\\algorithm\\algorithm_pttkgt\\input.txt')

    mang_vertex = [Vertex(index=i) for i in range(matran.height)]

    Dfs(mang_vertex,matran,0,1)

    for i in range(len(mang_vertex)):
        print "dinh %d: %d %d" %(i+1,mang_vertex[i].start_time,mang_vertex[i].end_time)