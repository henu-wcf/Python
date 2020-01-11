#列表.sort()是列表对象的函数，所以是对该列表对象本身进行排序
#列表.sort():小到大   列表.sort(reverse=True):大到小
a=[10,20,30,40,50,10,20,30,40,50]
print("a的ID:{}".format(id(a)))
a.sort()
print(a)
print("a的ID:{}".format(id(a)))
a.sort(reverse=True)
print(a)
print("a的ID:{}".format(id(a)))

print("*"*50)

#列表.sorted()是内置函数，是对列表的副本操作 生成了新的对象
a=sorted(a)
print(a)
print("a的ID:{}".format(id(a)))
a=sorted(a, reverse=True)
print(a)
print("a的ID:{}".format(id(a)))
      
