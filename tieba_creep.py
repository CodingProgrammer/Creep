#!/usr/bin/python
#-*-coding:utf-8 -*-
import urllib
import urllib2

def loadPage(url, filename):
    '''
    根据URL发送请求，获取服务器相应文件
    URL：需要爬取的URL地址
    '''
    print("正在下载" + filename)
    ua_headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    request = urllib2.Request(url, headers = ua_headers)
    return urllib2.urlopen(request).read()


def writePage(html, filename):
    '''
    作用：将html内容写入到本地
    html:服务器相应文件内容
    '''
    print("正在保存"+filename)
    #文件写入
    with open(filename, 'w') as f:
        f.write(html)
    print('*'*30)

def tiebaSpider(url, beginPage, endPage):
    for page in range(beginPage, endPage + 1):
        pn = (page - 1) * 50
        filename = "第" + str(page) + "页.html"
        fullurl = url + "&pn=" + str(pn)
        html = loadPage(fullurl, filename)
        writePage(html, filename)
    print("谢谢使用！")
if __name__ == "__main__":
    kw = raw_input("请输入贴吧名：")
    beginPage = int(raw_input("请输入起始页："))
    endPage = int(raw_input("请输入结束页："))

    url = "http://tieba.baidu.com/f?"
    key = urllib.urlencode({"kw":kw})
    fullurl = url + key
    tiebaSpider(fullurl, beginPage, endPage)
  
