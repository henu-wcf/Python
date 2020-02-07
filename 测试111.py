'''你可能以为输出的结果会是：
[1]
[2]
[11, 12, 13, 14, 3]
[4]
但事实上，该程序输出的结果是：
[1]
[1, 2]
[11, 12, 13, 14, 3]
[1, 2, 4]
这是为什么呢？
函数add的功能是当x不在列表中时，将x追加给列表lst。
当函数第一次执行时，参数lst的默认值[]被创建。这个默认值只会被创建一次。
add(1)将1加到lst。当函数再次被调用时，lst是[1]而不是[]，因为lst只被创建一次。
当参数的lst为[11,12,13,14]时，lst就是[11,12,13,14]。
list4调用函数时，使用默认参数，因此，现在默认参数lst为[1,2]。
'''
'''如果想要使默认列表在每次函数调用时都是[]，可以像测试222.py那样修改函数参数：'''



def add(x, lst=[]):
    print(id(lst))

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