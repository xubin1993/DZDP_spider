#coding=utf-8
import re
import string
import Queue
import os
from Open_page import Openpage
class MuLU:
    def __init__(self):
        self.muluhref=Queue.Queue()
        self.openpage=Openpage()
	self.name=[]
    def Get_href(self,url):
        myPage=self.openpage.Getpage(url)
        key={'健身中心','游泳馆','羽毛球馆','瑜伽','乒乓球馆','舞蹈','网球场','篮球场','足球场','高尔夫场','保龄球馆','滑雪场','台球馆','武术场馆','体育场馆','马术场','桌球馆'}#,'马术场''滑雪场'
        hrefs=re.findall('<a data-key="(.*?)" href="(.*?)"  onclick="(.*?)" alt="">(.*?)</a>',myPage,re.S)
        k=1
	f=open('Muluhref'+'.txt','w+')
        for i in hrefs:
            if i[3] in key:
                if i[3] not in self.name:
                    print i[1]
                    print i[3]
                    k=k+1
                    self.name.append(i[3])
		    self.name.append(i[0])
		    self.muluhref.put(i[1])
		    f.write(i[1])
		    f.write('\r\n')
		    f.write(i[3])
		    f.write('\r\n')
	f.close()
        #print k
	#for i in self.name:
	    #print i 
	print len(self.name)
	for i in range(0,len(self.name),2):
	    print 'sssss'
	    path='data0322'
	    title=self.name[i]
	    new_path=os.path.join(path,title)	
	    if not os.path.isdir(new_path):#创建文件夹
	    	os.makedirs(new_path)
	
	#f=open('Time/'+title+'/'+self.number+'.txt','w+')        
            
            
#ss=MuLU()
#ss.Get_href('http://www.dianping.com/shanghai/sports')


