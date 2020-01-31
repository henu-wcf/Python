import requests
from bs4 import BeautifulSoup
import bs4
def getHTML(url):
    try:
        r = requests.get(url, timeout=30)
        r.encoding = r.apparent_encoding
        r.raise_for_status()
        return r.text
    except:
        return ""

def getList(html, list):

    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find("tbody").children:
        if isinstance(tr, bs4.element.Tag):
            # ntr1 = tr("th")
            ntr2 = tr("td")
            # list.append([ntr1[0].string, ntr1[1].string, ntr1[2].string, ntr1[3].string, ntr1[4].string])
            list.append([ntr2[0].string, ntr2[1].string, ntr2[2].string, ntr2[3].string, ntr2[4].string, ntr2[5].string])
    return list

def printMess(list, num):
    form = "{0:^10}{1:^10}{2:^50}{3:^25}{4:^25}{5:^25}"
    print(form.format("排名", "上年排名", "公司名称", "营业收入", "利润", "国家"))
    for i  in range(num):
        print(form.format(list[i][0], list[i][1], list[i][2], list[i][3], list[i][4], list[i][5]))

def main():
    url="http://www.fortunechina.com/fortune500/c/2019-07/22/content_339535.htm"
    html = getHTML(url)
    list = []
    list = getList(html, list)
    printMess(list, 100)
main()