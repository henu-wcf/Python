# 中序遍历二叉树
# 算法：递归遍历 houXu(root, kv)

# 注意 左根右：左右是指左子树和右子树，
# 对左子树再进行左根右直至结束，然后输出根， 然后对右子树进行左右根直至结束
# 递归容易迷，可以进行断点调试
def main():
    result = []
    kv = {}
    line = input().split(" ")
    for li in line:
        newline = li.split("(")
        key = newline[1][0:3]
        value = newline[0]
        kv[key] = value

    print(kv)
    root = "0,0"
    houXu(root, kv)
def houXu(root, kv):

    if root in kv:
        #左
        lchild = kv[root]+",1" #前一个根节点的左子节点
        houXu(lchild, kv)
        #根
        print(kv[root])
        #右
        rchild = kv[root]+',2'#前一个根节点的右子节点
        houXu(rchild, kv)

    else :
        return     #返回到上一层调用处

main()