#爬取网站内容

import requests
import os
url="http://www.henu.edu.cn/"
try:
    kv={"User-Agent":"Mozilla/5.0"}
    r=requests.get(url, headers=kv) #kv的作用是让网站认为是浏览器在进行访问
    r.raise_for_status   #返回200，表示与网站连接成功；否则出现异常
    r.encoding=r.apparent_encoding  #r.apparent_encoding是爬虫自己通过内容判断其编码方式
    print(r.text)

    path="D://代码练习//Python练习//爬取网站案例"
    writer=open(path, "wb")
    writer.write(r.content)
    writer.close()       #注意关闭打开的文件
    print("文件保存成功")
except:
    print("爬取失败")
