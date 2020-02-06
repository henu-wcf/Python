#递归 对表达式树进行结果计算 calculate(kv, root)

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

#核心
def calculate(kv, root):
    if kv[root][0]=="" and kv[root][1]=="":        #只有叶子节点才是运算数， 所以当某个节点的左右子节点均为空时，则返回这个运算数
        return eval(root[0])
    else:
        left = calculate(kv, kv[root][0])
        right = calculate(kv, kv[root][1])
    return calSum(left, right, root[0])            #注意 此处一定要return  返回至上一层

def calSum(left, right, root):
    if root=="+" :
        return left + right
    elif root=="-":
        return left - right
    elif root == "*":
        return left * right
    elif root == "/":
        return left / right

def main():
    kv = inputTree()
    root = ("-", 1)
    sum = calculate(kv, root)
    print("{:.2f}".format(sum))
main()