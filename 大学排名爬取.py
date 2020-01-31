import requests
from bs4 import BeautifulSoup
import bs4

def getHTML(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""

def getList(html, uList):
   
    soup=BeautifulSoup(html, "html.parser")
    for tr in soup.find("tbody").children:
        if isinstance(tr, bs4.element.Tag):
            td=tr("td")
            uList.append([td[0].string, td[1].string, td[2].string, td[3].string])
    return uList

def printMeass(uList, num):
    form = "{0:^10}{1:{4}^10}{2:{4}^10}{3:^10}"
    print(form.format("排名","大学","省份","得分", chr(12288)))
    for i in range(num):
        print(form.format(uList[i][0], uList[i][1], uList[i][2], uList[i][3], chr(12288)))

def main():
    url="http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html"
    uList=[]
    html=getHTML(url)
    uList=getList(html, uList)
    printMeass(uList, 10)
main()  
    
