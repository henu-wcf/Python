#解决从某一点到其余各点的最短距离：dijkstra算法
#题目来源：  计蒜客   T1213  拯救行动
import heapq
import math


# 此处tmp的作用是：因为heapq优先队列库 heapq.heappush(pqueue, (head.s + 1, tmp, node))
# 如果第二个参数传入的是一个元组，则系统在将该元组入列时，会按照元组里的元素 顺序 进行比较，
# 然而如果head.s+1的结果相同，且此时没有tmp
# 系统则会将node进行比较。但是node是类的对象，对象之间无法比较
#（注意：其实当head.s+1相等时，就是做dijkstra算法时遇到 到两个点距离相等时，此时确定哪个都行（离散数学）；
# 所以tmp只是起到让系统能够确定一个即可；可见计算机不及人的智力）
tmp = 0
pqueue = []                     #dijkstr算法的核心：优先队列（Python中直接有可以用的优先队列，import heapq）
isask = [[False for i in range(200)] for i in range(200)]
dir = [[0,1], [0,-1], [1,0], [-1,0]]
class Node:
    def __init__(self, x, y, s, parent):
        self.x = x
        self.y = y
        self.s = s
        self.parent = parent
def bfs(loc, row, col, x1, y1, x2, y2, distance):
    global pqueue, isask, dir, tmp
    flag = False
    node = Node(x1, y1, 0, None)
    tmp = tmp+1
    heapq.heappush(pqueue, (0, tmp, node))

    while(pqueue):
        head = heapq.heappop(pqueue)[2]   #将队列中第一个元组（因为优先队列，它的head.s也最小）中的第三个元素（对象）取出
        isask[head.x][head.y] = True
        if head.x==x2 and head.y==y2:
            flag = True
            return head.s, flag
        for i in range(4):
            tx = head.x + dir[i][0]
            ty = head.y + dir[i][1]
            if tx<0 or tx>=row or ty<0 or ty>=col or isask[tx][ty]==True or loc[tx][ty]=="#":
                continue
            else:
                if loc[tx][ty]=="@":
                    if head.s + 1 < distance[tx][ty]:
                        node = Node(tx, ty, head.s+1, head)
                        tmp = tmp+1
                        heapq.heappush(pqueue, (head.s + 1, tmp, node))
                        distance[tx][ty] = head.s + 1
                if loc[tx][ty]=="x":
                    if head.s + 2 < distance[tx][ty]:
                        node = Node(tx, ty, head.s+2, head)
                        tmp = tmp +1
                        heapq.heappush(pqueue, (head.s + 2, tmp, node))
                        distance[tx][ty] = head.s + 2
                if loc[tx][ty]=="a":
                    if head.s + 1 < distance[tx][ty]:
                        node = Node(tx, ty, head.s+1, head)
                        tmp = tmp+1
                        heapq.heappush(pqueue, (head.s + 1, tmp, node))
                        distance[tx][ty] = head.s + 1


    return 0, flag

def main():
    line = input().split(" ")
    row = eval(line[0])
    col = eval(line[1])
    loc = [[0 for k in range(200)] for k in range(200)]
    distance = [[0 for k in range(200)] for k in range(200)]        #dijkstra的初始状态 开始点到其余各点的距离
    for i in range(row):
        line = input()
        for j in range(col):
            loc[i][j] = line[j]
            distance[i][j] = math.inf                           #将起始点到其余各点的距离初始化为正无穷
            if line[j]=="r":
                x1, y1 = i, j
                distance[i][j] = 0                             #将起始点到自身的距离初始化为0
            if line[j]=="a":
                x2, y2 = i, j
    step, flag = bfs(loc, row, col, x1, y1, x2, y2, distance)
    if flag:
        print(step)
    else:
        print("Impossible")
main()