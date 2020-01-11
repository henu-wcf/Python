import time
import io

#用“+”拼接字符串 效率低
#因为拼接一次会生成一个新的对象
time1=time.time()
a=""
for i in range(1000000):
    a+="aa"
time2=time.time()
print(str(time2-time1))

#用io.StringIO(a)方法可以提高效率
time3=time.time()
a=""
a=io.StringIO(a)
for i in range(1000000):
    a.write("aa")
time4=time.time()
print(str(time4-time3))

