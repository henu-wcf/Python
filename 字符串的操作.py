#字符串的相关操作
a="abcdefg123"
print(a)
print("1"+"*"*20)

#定义字符串时，''' 的使用
b='''asd
ddddf
fff'''
print(b)
print("2"+"*"*20)

#当字符串过长，可分多行写（但实际仍未一行）
a="aaaaaa\
bbbbbb\
cccccc\
dddddd"
print(a)
print("3"+"*"*20)

#获取字符串长度
print(len(a))
print("4"+"*"*20)

#字符串的拼接
c="aa"
c+="a"
print(c)
c*=3
print(c)
print("5"+"*"*20)

#不换行的打印
print("hunu123", end="\t")
print("hunu123", end="\t")
print("hunu123", end="\t")
print()
print("6"+"*"*20)

#str()实现其他类型转字符串类型
print(str(5.20), end="\t")
print(str(3.14e2))
print("7"+"*"*20)

#a.replace()方法并不是直接改变的字符串a，而是新生成了一个字符串对象
a="aaabbbccc"
print(a.replace("a", "凡"))  #将所有“a”全部替换掉
print(a)
print("8"+"*"*20)

#字符串切片操作a[start;end;步长](包头不包尾)
a="abcdefg1234567"
print(a[::]) #从头到尾
print(a[1:5:2]) #输出为：bd
print(a[-3::1]) #输出为：567
print(a[::-1]) #为倒序输出

#a.split(str)是按str分割字符串a，返回一个列表
#"str".join(list)是用str将列表list中的元素连接成字符串
a="I love you   !!"
print(a.split(" ")) #输出为：['I', 'love', 'you', '', '', '!!']
print(a.split("you")) #输出为：['I love ', '   !!']
b=["I", "love", "you"]
print("(￣▽￣)".join(b)) #输出为：I(￣▽￣)love(￣▽￣)you
print("9"+"*"*20)

#字符串的比较和同一性
'''==用来比较两个字符串是否相同，is/not is 用来比较两个字符串对象是否是
同一个对象，比较的是地址（id()）'''

#in/not in的操作
''' 用来判断某个字符（串）是否是某个字符串的字串'''

#a.startwuith(str)判断字符串a是否是以str开头的
#a.endwith(str)判断字符串a是否是以str结尾的
#a.find(str)查找字符串a中str第一次出现的位置
#a.rfind(str)查找字符串a中str最后一次出现的位置
#a.count(str)查看str出现了几次
#a.isalnum()判断字符串中是否全为字母或数字
a="王森是个好小伙，王森买报纸，遇到一个女孩，从此爱上了她，女孩也爱上了他"
print(a.startswith("王森"))
print(a.endswith("女孩"))
print(a.find("女孩"))
print(a.rfind("女孩"))
print(a.count("女孩"))
print(a.isalnum())
print("10"+"*"*20)

#a.strip(str)去除首尾的str
a="  abcdef  1234567  "
print(a.strip(" "))
print("11"+"*"*20)

#字符串大小写转换
a="abcDEF ghijKLM"
print(a.capitalize()) #产生新的字符串，首字母大写
print(a.title()) #产生新的字符串，每个单词的首字母大写
print(a.upper()) #全大写
print(a.lower()) #全小写
print(a.swapcase()) #所有字母大小写转换
print("12"+"*"*20)

#字符串的输出格式排版
a="王森"
print(a.center(10, "*")) #输出为：****王森****
print(a.ljust(10, "*"))  #输出为：王森********
print(a.rjust(10, "*"))  #输出为：********王森
print("13"+"*"*20)

#方法补充a.isalnum() a.isalpha() a.isdigit() a.isspace() a.isupper() a.islower()
a="王森sbb666"
print(a.isalnum()) #看是否都为数字或字母
print(a.isalpha()) #看是否都为字母（包括汉字）
print(a.isdigit()) #看是否都为数字
print(a.isspace()) #看是否都为空白符
print(a.isupper()) #看是否都为大写字母
print(a.islower()) #看是否都为小写字母
print("14"+"*"*20)
