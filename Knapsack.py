
def Unbounded_Knapsack(items,T):
    K = [0 for i in range(T+1)]
    for x in range(1,T+1):
        mx = 0
        for i in items:
            if(x>=i[0]):
                mx = max(mx,i[1]+K[x-i[0]])
        K[x] = mx
    return K[T]


def Knapsack_0_1(items,T):
    K = [[0 for i in range(len(items)+1)] for j in range(T+1)]
    for j in range(1,len(items)+1):
        for x in range(1,T+1):
            K[x][j] = K[x][j-1]
            if x >= items[j-1][0]:
                K[x][j] = max(K[x][j],K[x-items[j-1][0]][j-1]+items[j-1][1])
    return K[T][len(items)]
def init(namefile):
    f = open(namefile)
    line = f.readline().split(' ')
    numbers = map(lambda x: int(x),line)
    n = numbers[0]
    T = numbers[1]
    items = []
    for i in range(n):
        line = f.readline().split(' ')
        numbers = map(lambda x: int(x),line)
        items.append(numbers)
    for i in range(n):
        print items[i]
    return items,T

items,T = init("c:\\Users\PHAM_DUNG\\myproject\\algorithm\\algorithm_pttkgt\\input_knapsack.txt")
print Unbounded_Knapsack(items,T)
items,T = init("c:\\Users\PHAM_DUNG\\myproject\\algorithm\\algorithm_pttkgt\\input_knapsack1.txt")
print Knapsack_0_1(items,T)