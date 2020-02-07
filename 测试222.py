'''
注意 lst=[] 和lst=None 是不同的:
首先type(lst)=<class 'NoneType'>  , type(lst)=<class 'list'>
其次二者的 not lst 均为 True
有关详细内容：参考：
https://blog.csdn.net/jclian91/article/details/86664387
https://www.cnblogs.com/JackLi07/p/9917631.html
https://blog.csdn.net/crisschan/article/details/70312764
'''



def add(x, lst=None):
    print(id(lst))

    if lst is None:
        lst = []
    if x not in lst:
        lst.append(x)

    return lst

def main():
    list1 = add(1)
    print(list1)

    list2 = add(2)
    print(list2)

    list3 = add(3, [11, 12, 13, 14])
    print(list3)

    list4 = add(4)
    print(list4)

main()