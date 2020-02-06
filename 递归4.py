#求二叉树中指定节点所在层数      #法一法二 参考：https://blog.csdn.net/olizxq/article/details/84338296

#方法一：利用递归 getNodeLayer(kv, root, node)  和  全局变量 layer:层数

layer = 0      #全局变量   注意 全局变量在递归函数中的的使用

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

def getNodeLayer(kv, root, node):
    global  layer                  #用 gloabl 声明后才能在递归函数（或其他函数）中使用全局变量
    if root=="":
        return
    else:
        layer = layer+1
        if root==node:
            print(layer)
        getNodeLayer(kv, kv[root][0], node)
        getNodeLayer(kv, kv[root][1], node)
        layer = layer-1                    #必须恢复，所有函数调用使用同一个值

def main():
    kv = inputTree()
    node = "7"
    root = "1"
    getNodeLayer(kv, root, node)  #找节点"7"所在层数
main()