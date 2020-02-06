#表达式树（即：叶子节点为实数，其余节点为运算符）的遍历输出

def inputTree():
    kv = {}       #用kv存储二叉树 形式：kv[(根节点, 该节点第几次出现)]=((左子节点,该节点第几次出现),（右子节点,该节点第几次出现))
    kv[("-", 1)] = (("+", 1), ("/", 1))
    kv[("+", 1)] = (("4", 1), ("*", 1))
    kv[("/", 1)] = (("12", 1), ("3", 1))
    kv[("4", 1)] = ("", "")            #(子节点为空时不用记录第几次)
    kv[("*", 1)] = (("1", 1), ("-", 2))
    kv[("1", 1)] = ("", "")
    kv[("-", 2)] = (("5", 1), ("2", 1))
    kv[("12", 1)] = ("", "")
    kv[("3", 1)] = ("", "")
    kv[("5", 1)] = ("", "")
    kv[("2", 1)] = ("", "")
    return kv

def qianxu(kv, root):           #前序表达式
    if root=="":
        return
    print(root[0]+" ", end="")
    qianxu(kv, kv[root][0])
    qianxu(kv, kv[root][1])

def zhongxu(kv, root):          #中序表达式
    if root=="":
        return

    if (kv[root][0]=="" and kv[root][1]=="" and len(root[0]))==1 \
            or root==("-", 1) or root[0]=="*" or root[0]=="/":          #表达式形式上去掉多余的括号
        zhongxu(kv, kv[root][0])
        print(root[0], end="")
        zhongxu(kv, kv[root][1])
    else:
        print("(", end="")
        zhongxu(kv, kv[root][0])
        print(root[0], end="")
        zhongxu(kv, kv[root][1])
        print(")", end="")

def houxu(kv ,root):          #后序表达式
    if root=="":
        return
    if len(root[0])!=1:
        print("(", end="")
        houxu(kv, kv[root][0])
        houxu(kv, kv[root][1])
        print(root[0], end="")
        print(") ", end="")
    else:
        houxu(kv, kv[root][0])
        houxu(kv, kv[root][1])
        print(root[0] + " ", end="")

def main():
    kv = inputTree()
    root = ("-", 1)
    qianxu(kv, root)
    print()
    zhongxu(kv, root)
    print()
    houxu(kv, root)

main()