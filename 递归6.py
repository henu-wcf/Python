#求二叉树中根节点到指定节点的路径

#方法一：利用递归 getNodePath(kv, root, node)  和  全局列表变量 result:存储路径的列表
#类比   ：递归4.py

# layer = 0
result = []     #全局变量   注意 全局变量在递归函数中的的使用
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

def getNodePath(kv, root, node):
    # global  layer
    global  result                   #用 gloabl 声明后才能在递归函数（或其他函数）中使用全局变量
    if root=="":
        return
    else:
        # layer = layer+1
        result.append(root)
        if root==node:
            # print(layer)
            print(result)                    #找到所求节点后将路径输出
        getNodePath(kv, kv[root][0], node)
        getNodePath(kv, kv[root][1], node)

        # layer = layer-1
        del(result[-1])                      #必须删除列表末尾元素，因为所有函数调用使用同一个列表result

def main():
    kv = inputTree()
    node = "7"
    root = "1"
    getNodePath(kv, root, node)  #找节点"7"到根节点的路径
main()