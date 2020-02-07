#求二叉树中根节点到指定节点的路径

#注意： 此方法是错误的
#方法二：利用递归 getNodePath(kv, root, node, result)  将result作为参数
#但是会出现问题  对比 递归5.py知，它的layer参数对于每层调用是独立的（传递的是副本），
#而result列表作为函数参数时，是它的地址
#所以每层调用的是同一个result
#故 此法错误
#   关于“列表作为函数参数”的详细的介绍：请看测试111.py 和 测试222.py

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

def getNodePath(kv, root, node, result):
    if root=="":
        return
    else:
        result.append(root)
        if root==node:
            print(result)
        getNodePath(kv, kv[root][0], node, result)
        getNodePath(kv, kv[root][1], node, result)
                                                      #不必恢复  result, 各函数调用层独立使用
    return

def main():
    kv = inputTree()
    root = "1"
    node = "7"
    layer = 1
    result = []
    getNodePath(kv, root, node, result)    #找节点"7"所在层数

main()