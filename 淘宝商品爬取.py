import requests
import re

def getHTML(url):
    #解决淘宝反爬虫机制：
    # 1.谷歌浏览器打开淘宝网页
    # 2.登录淘宝账号
    # 3.搜索关键字“手机”
    # 4.右击点击检查，刷新界面，找到第一项search?开头的 复制
    # 5.打开https://curl.trillworks.com/#，在curl command一栏进行粘贴
    # 6.复制Python requests一栏中的headers{。。。。}， 使其作为requests.get()中的headers参数
    try:
        header = {
    'authority': 's.taobao.com',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'sec-fetch-user': '?1',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'navigate',
    'referer': 'https://www.taobao.com/',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'thw=cn; t=59e17ce61ad0a66cbfc4f46eb056c4c2; cna=Yxq7FuJnqAwCAT2emEW+fSpI; uc3=nk2=F5RBwKVuKn6KEHo%3D&lg2=VT5L2FSpMGV7TQ%3D%3D&id2=VyyZHQ44m4pBVA%3D%3D&vt3=F8dBxdsSHEeX4J35cD4%3D; lgc=tb456318578; uc4=nk4=0%40FY4KpX0sgeFBmog%2Bg0u%2B%2BzPfhR218g%3D%3D&id4=0%40VXtWA0Re4Nu6dNToZoq2qZA1xulW; tracknick=tb456318578; _cc_=VT5L2FSpdA%3D%3D; tg=0; enc=Nch0Bgjc8GaA8spKxfmUQlp5pUV5F5%2FvnR3u2Rv%2Fb8I%2FoXV4FZYFthzayeWG9y7ZF6%2BGByG5r1Y5jKwqW0GZGQ%3D%3D; mt=ci=103_1; hng=CN%7Czh-CN%7CCNY%7C156; _uab_collina=158047874658490387635421; v=0; cookie2=1459eed6fcf1e194241ec789a6688ec5; _tb_token_=bae5bb7710a3; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; JSESSIONID=32B1546737BA5F2DFB5C2CFA8BA128D8; x5sec=7b227365617263686170703b32223a223633313430613036656336346633393461393066333436316431326230666465434c6635305045464550664535726675774a57355a526f4d4e4441344d6a4d304d7a49344d547330227d; uc1=cookie14=UoTUOqS0Bu%2B%2F9g%3D%3D; l=cBSVVMi7Q_aHxo1jBOCZlurza77TDIRfguPzaNbMi_5Ih1L1TU_Oo4hTaep6cjWdtzTW4Tn8Nr29-etkidHx3mDgcGAN.; isg=BJiYJonkck8yHl7Lrhqym15aacYqgfwLt1Xi79KJZlOGbTlXcpHMm65PoaXd_bTj',
}

        r = requests.get(url, timeout=30, headers = header)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def getList(ls, html):
    #利用正则表达式进行匹配
    priceList = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html) #匹配"view_price":"xx.xx"
    nameList = re.findall(r'\"raw_title\"\:\".*?\"', html)       #匹配"raw_title":"xxxxxxxx"

    for i in range(len(priceList)):
        #这里eval的作用是将元素的双引号去掉
        price = eval(priceList[i].split(":")[1])
        name = eval(nameList[i].split(":")[1])
        ls.append([price, name])
    return ls

def printMess(ls):
    form = "{:^10}{:^10}{:^10}"
    print(form.format("编号", "价格", "名称"))
    count = 0
    for i in ls:
        count = count + 1
        print(form.format(count, i[0], i[1]))

def main():
    goodName = "手机"
    #deep的作用是控制爬取的深度（即网页下方的第几页 翻页）
    deep = 5
    for i in range(deep):
        # 44 表示一页中显示的商品数量
        url = "https://s.taobao.com/search?q=" + goodName + "&s=" + str(i*44)
        html = getHTML(url)
        ls = []
        ls = getList(ls, html)
        printMess(ls)
main()

