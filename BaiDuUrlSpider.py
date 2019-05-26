#coding:utf-8
#!/usr/bin/env python
# code by aedoo
# github: https://github.com/aedoo/

import requests,queue,sys,threading,time
from bs4 import BeautifulSoup
import re

class BaiDuUrlSpider(threading.Thread):

    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.__queue = queue

    def run(self):
        while not self.__queue.empty():
            page_url = self.__queue.get(timeout=0.5)
            try:
                self.spider(page_url)
            except Exception as e:
                pass

    def spider(self,page_url):
        f1 = open('original_url.txt','a+')
        f2 = open('home_url.txt','a+')
        r = requests.get(url=page_url, headers=head)

        soup = BeautifulSoup(r.content,'lxml')
        raw_url = soup.find_all(name='a',attrs={'data-click':re.compile('.'),'class':None})

        for raw in raw_url:
            # print raw['href']
            trick_url = raw['href']
            response = requests.get(url=trick_url,headers=head,timeout=3)

            if response.status_code==200:
                print (response.url)
                original_url = response.url



                f1.write(original_url+'\n')
                url_tmp = response.url
                url_list = url_tmp.split('/')
                print (url_list[0]+'//'+url_list[2])
                home_url = url_list[0]+'//'+url_list[2]
                f2.write(home_url+'\n')
            else:
                print (response.status_code)

        f1.close()
        f2.close()


def quchong():
    rFile = open('home_url.txt','r')
    wFile = open('qc_home_url.txt','w') #去重后的txt
    allLine = rFile.readlines()
    rFile.close()
    s = set()
    for i in allLine:
        s.add(i)
    for i in s:
        wFile.write(i)




def main():

    global  head
    head = {

    'Connection': 'close',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch, br',
    'Accept-Language': 'zh-CN,zh;q=0.8',
}
    q = queue.Queue()
    threads = []
    threads_count = 200   #设置线程数目,最好不要大于爬取的页码数

    if len(sys.argv)!=2:
        print ('python Usage: %s keyword'% sys.argv[0])
        sys.exit(-1)
    else:
        keyword = sys.argv[1]

        for i in range(0,750,10):   #百度默认最多75页,每页10个,根据规则定义的
            url_start = 'https://www.baidu.com/s?wd=' + keyword + '&pn=%s'%(str(i))  #拼接百度搜索的URL
            #url = url_start+str(i)
            q.put(url_start)

        for i in range(threads_count):
            threads.append(BaiDuUrlSpider(q))

        for i in threads:
            i.start()
        for i in threads:
            i.join()

if __name__ == '__main__':
    f1 = open('original_url.txt','w')
    f1.close()
    f2 = open('home_url.txt','w')
    f2.close()
    time_start = time.time()
    main()
    print (time.time()-time_start)
    quchong()

