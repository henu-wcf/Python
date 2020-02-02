'''
给定一个层数小于等于10的二叉树，输出对其中序遍历的节点名序列。

输入包括一行，为由空格分隔开的各节点，按照二叉树的分层遍历顺序给出，每个节点形式如X(Y,num)，
X表示该节点，Y表示父节点，num为0,1,2中的一个，0 表示根节点，1表示为父节点的左子节点，
2表示为父节点的右子节点。输出为一行，为中序遍历的结果。

样例输入复制
A(0,0) B(A,1) C(A,2) D(B,1) E(B,2) F(C,1) G(D,1) H(D,2)
样例输出复制
G D H B E A F C
题目来源
北京大学软件与微电子学院 2015级新生编程技能测验

题目：计蒜客A1004 非递归二叉树的中序遍历
算法思路参考：B站 https://www.bilibili.com/video/av35339922?from=search&seid=10230205043748743772
'''


def main():
    result = []
    kv = {}
    line = input().split(" ")
    for li in line:
        newline = li.split("(")
        key = newline[1][0:3]
        value = newline[0]
        kv[key] = value


#算法核心部分***********************************************************
    
    stack = []            #用来存放各个子树的根节点的栈
    child = "0,0"         #child初始化为整个树的根节点
    while(child in kv or len(stack)!=0):
        if child in kv:                 #当此节点在树中时，将此节点入栈
            stack.append(child)
            child = kv[child]+",1"      #更新为上一个节点的左子节点，用于下次循环判断：如果他在树中，则将其入栈
        else:
            result.append(kv[stack[-1]])    # 否则输出栈中最后进栈的元素，
            child = kv[stack[-1]]+",2"      #然后将节点更新为上一节点的右节点，
            del(stack[-1])                  #接着删除已经输出的栈中的末尾元素， 进行下次循环判断

    result = " ".join(result)
    print(result)
main()