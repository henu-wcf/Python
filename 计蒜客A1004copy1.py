# 前序遍历二叉树
# 算法：递归遍历 qianXu(root, kv)

# 注意 根左右：左右是指左子树和右子树，
# 对左子树再进行根左右直至结束，然后对右子树进行根左右直至结束
def main():
    result = []
    kv = {}
    line = input().split(" ")
    for li in line:
        newline = li.split("(")
        key = newline[1][0:3]
        value = newline[0]
        kv[key] = value

    root = "0,0"
    qianXu(root, kv)
    print(kv)
def qianXu(root, kv):
    if root in kv:
        print(kv[root])
        lchild = kv[root]+",1"    #前一个根节点的左子节点
        qianXu(lchild, kv)
        rchild = kv[root]+',2'    #前一个根节点的右子节点
        qianXu(rchild, kv)
    else :
        return     #返回到上一层调用处

main()