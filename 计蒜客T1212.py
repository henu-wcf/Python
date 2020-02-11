#bfs 问题
#算法的核心：
# 1.队列queue的先进先出，各个点都是只进队列一次，出一次；对图遍历完整的一次结束条件是队列为空
# 2.根据题意进行提前结束
# 3.需要定义一个标记数组isask，来标记已经访问过的点
# 4.dir数组为方向数组，用于对从队列头取出的点遍历它的“上下左右”四个方向

#题目来源：计蒜客  T1212  仙岛求药
queue = []
isask = [[False for i in range(20)] for i in range(20)]
dir = [[0,1], [0,-1], [-1,0], [1,0]]
class Node:
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s
def bfs(loc, row, col, x1, y1, x2, y2):
    global queue, isask, dir
    flag = False
    node = Node(x1, y1, 0)
    queue.append(node)
    isask[x1][y1] = True
    while(queue):
        head = queue[0]
        del(queue[0])
        if head.x==x2 and head.y==y2:             #根据题意提前结束
            flag = True
            return head.s, flag
        for i in range(4):                        #遍历队列头 点 的上下左右
            tx = head.x + dir[i][0]
            ty = head.y + dir[i][1]
            if tx<0 or tx>=row or ty<0 or ty>=col or isask[tx][ty]==True or loc[tx][ty]=="#":       #判断是否越界，是否碰到不可以访问的点
                continue
            else:
                node = Node(tx, ty, head.s+1)
                queue.append(node)
                isask[tx][ty] = True
    return 0, flag

def main():
    line = input().split(" ")
    row = eval(line[0])
    col = eval(line[1])
    loc = [[0 for k in range(col)] for k in range(row)]
    for i in range(row):
        line = input()
        for j in range(col):
            loc[i][j] = line[j]
            if line[j]=="@":
                x1, y1 = i, j
            if line[j]=="*":
                x2, y2 = i, j
    step, flag = bfs(loc, row, col, x1, y1, x2, y2)
    if flag:
        print(step)
    else:
        print("-1")

main()
