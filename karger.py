class Vertex:
    def __init__(self):
        self.adges = []
        
class Edge:
    def __init__(self):
        
class SuperVerTex:
    def __init__(self):
        self.vertexs  = []
        self.adges = []

def init(namefile):
    f = open(namefile)
    numbers = map(lambda x: int(x),f.read().split(" "))
    if len(numbers) == 2:
        n = numbers[0]
        m = numbers[1]
    vertexs = [[] for i in range(n)]
    for i in range(m):
        numbers = map(lambda x: int(x),f.read().split(" "))
        vertexs[numbers[0]].append(numbers[1])
    