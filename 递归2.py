#递归 求二叉树的高度
#
def inputTree():
    kv = {}       #用kv存储二叉树 形式：kv[根节点]=(左子节点， 右子节点)
    kv["A"] = ("B", "C")
    kv["B"] = ("D", "F")
    kv["C"] = ("G", "I")
    kv["D"] = ("", "")
    kv["E"] = ("", "")
    kv["F"] = ("E", "")
    kv["G"] = ("", "H")
    kv["H"] = ("", "")
    kv["I"] = ("", "")
    return kv

def getHight(kv, root):
    if root=="":
        return 0
    return max(getHight(kv, kv[root][0])+1, getHight(kv, kv[root][1])+1)    #核心：假设根节点有左右两个子树，那么树高为：
                                                                            #max(左子树的树高+1， 右子树的树高+1)，以此递归
def main():
    root = "A"
    kv = inputTree()
    h = getHight(kv, root)
    print(h)
main()