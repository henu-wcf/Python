
#网络爬取图片
import requests
import os
url="http://dl.ppt123.net/pptbj/201603/2016030410211241.jpg"
                    #在网站上找到一张图片，右键得到图片的地址
root="D://代码练习//Python练习//"
path=root+url.split("/")[-1] #将图片的命名为2016030410211241.jpg
try:
    if not os.path.exists(root):  #如果root路径不存在，则建立root文件夹路径
        os.mkdir(root)
    if not os.path.exists(path):  #如果path路径不存在，说明该图片的文件未建立，
                                  #可以开始爬取
        r=requests.get(url)
        with open(path,"wb") as f:
            f.write(r.content)    #r.content直接获取的是二进制，
                                  #无需：r.encoding=r.apparent_encoding
            f.close()
            print("文件保存成功")
    else :
        print("文件已存在")
except:
    print("爬取失败")

