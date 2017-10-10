class DanhSachKe:
    def __init__(self,sodinh):
        self.CanhKes = [[] for i in range(sodinh)]
    

def init(namefile):
    f = open(namefile)
    line = f.readline().split(" ")
    numbers = map(lambda x: int(x),line)
    if len(numbers) == 2:
        dsKe = DanhSachKe(numbers[0])
        socanh = numbers[1]
        for i in range(socanh):
            numbers = map(lambda x: int(x),f.readline().split(" "))
            dsKe.CanhKes[numbers[0]-1].append([numbers[1],numbers[2]])
            dsKe.CanhKes[numbers[1]-1].append([numbers[0],numbers[2]])
    return dsKe

def prim(dsKe):
    lit = []
    
    
dsKe =  init("c:\\Users\PHAM_DUNG\\myproject\\algorithm\\algorithm_pttkgt\\danhsachcanh.txt")
print dsKe.CanhKes