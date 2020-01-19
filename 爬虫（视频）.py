import requests
import os

url="http://video.pearvideo.com/mp4/adshort/20180825\
/cont-1420328-12741912_adpkg-ad_hd.mp4"       #火狐搜素视频，打开视频后，右键点击查看
                                              #页面信息，然后复制“位置”即可
root="D://代码练习//Python练习//"
path=root+url.split("/")[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r=requests.get(url)
        r.raise_for_status()

        writer=open(path, "wb")
        writer.write(r.content)
        writer.close()

        print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")
    
