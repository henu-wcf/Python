
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
        if head.x==x2 and head.y==y2:
            flag = True
            return head.s, flag
        for i in range(4):
            tx = head.x + dir[i][0]
            ty = head.y + dir[i][1]
            if tx<0 or tx>=row or ty<0 or ty>=col or isask[tx][ty]==True or loc[tx][ty]=="#":
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