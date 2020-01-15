#元组tuple()
#元组属于不可变序列，

#元组支持的操作:
#1.元组的定义：注意当元组只有一个元素时，定义如下
#tuple()可以接收列表，字符串，其他序列类型，迭代器等生成元组
a=(10, 20, 30)
print(type(a))
a=(10,)
print(type(a))
b=tuple("abc")
b=tuple(range(4))
b=tuple([1, 2, 3])

#2.元组也支持切片
a="abcdefghijk"
print(a[0:4])
print(a[::-1])

#3.元组的排序只能使用内置函数sorted(tuple),且返回的是列表
#  注意列表可以使用对象自身的函数list.sorted(),修改的是原对象自身。
a=(10, 30, 20, 10, 50)
print(sorted(a))
print(sorted(a, reverse=True))

#4.
a=(1, 2, 3, 4)
print(len(a))
print(max(a))
print(min(a))
print(sum(a))

#5.zip(列表1，列表2，。。。)，将各个列表对象组合成各个元组，并返回这个zip对象
a=[1,2,3,4]
b=["a", "b", "c", "d"]
c=["张三","李四","王五"]
print(type(zip(a,b,c)))
d=zip(a,b,c)
print(d)  #此时的d为一个迭代器
d=list(d)
print(d)
