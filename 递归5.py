#求二叉树中指定节点所在层数       #法一法二 参考：https://blog.csdn.net/olizxq/article/details/84338296

#方法二：利用递归 getNodeLayer(kv, root, node, layer)  增加了 layer：层数参数
def inputTree():
    kv = {}
    kv["1"] = ("2", "3")
    kv["2"] = ("4", "5")
    kv["5"] = ("7", "")
    kv["7"] = ("", "8")
    kv["3"] = ("", "6")
    kv["4"] = ("", "")
    kv["8"] = ("", "")
    kv["6"] = ("", "")
    return kv

def getNodeLayer(kv, root, node, layer):
    if root=="":
        return
    else:
        if root==node:
            print(layer)
        getNodeLayer(kv, kv[root][0], node, layer+1)
        getNodeLayer(kv, kv[root][1], node, layer+1)
                                                      #不必恢复  layer, 各函数调用层独立使用
    return

def main():
    kv = inputTree()
    root = "1"
    node = "7"
    layer = 1
    getNodeLayer(kv, root, node, layer)    #找节点"7"所在层数

main()