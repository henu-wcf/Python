#当传递的参数是不可变对象时（如:int,float,字符串，元组，布尔值）
#实际传递的还是对象的引用，但如果在函数体内改变不可变对象的值时，
#系统会新创建一个对象

def f(n):
    print(id(n))
    n = n+1
    print(id(n))
    print(n)

def main():
    n = 3
    print(id(n))
    f(n)
    print(id(n))
    print(n)

main()