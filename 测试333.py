#当传递的参数是可变对象时（如:列表，集合等），实际传递的是对象的引用
#当是不可便=变对象 参考测试444.py
def f(lis):        #实际传递的是对象的引用
    print(id(lis))
    lis.append(8)
    print(id(lis))
    print(lis)

def main():
    lis = [1,2,3]
    print(id(lis))
    f(lis)
    print(lis)

main()