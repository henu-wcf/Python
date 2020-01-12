#"".format()格式化输出 <左对齐 >右对齐 ^中间对齐  {0:*^9.2f}
print("我是{0},我今年{1:*>8.2f}岁".format("张三", 18))
c="她是{0},她今年{1:#^8}岁"
print(c.format("甜甜", 6))

import io
#io.StringIO()方法
a=""
a=io.StringIO(a)
a.write("aa")
print(a.getvalue())
#可以通过io.StringIO(a)的方法修改字符串a指定位置的字符
a="I love you!"
a=io.StringIO(a)
#此时迭代器 a的指针在首位
a.seek(7)
a.write("Y")
print(a.getvalue())
