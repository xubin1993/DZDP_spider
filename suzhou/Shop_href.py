#coding=utf-8
import re 
import os
import string
from Muluget import MuLU
import Queue
from Open_page import Openpage
class ShopHerf:
    def __init__(self):
        self.shophref_queue=Queue.Queue()
        self.MuLU=MuLU()
        self.OpenPage=Openpage()
    def Next_href(self,urls):
        f=open('next_href'+'.txt','w+')
        ss.MuLU.Get_href(urls)
        i=0
        while(self.MuLU.muluhref.qsize()):
            url=self.MuLU.muluhref.get()
            print url
            myPage=self.OpenPage.Getpage(url)
            if not myPage:
                myPage=self.OpenPage.Getpage(url)
                #return 0
            #获取总页数
            page_number=re.findall('<a href="(.*?)"  data-ga-page="(.*?)" class="PageLink"',myPage,re.S)
            if page_number:
                number=page_number[-1][1]
                for i in range(1,int(number)+1):
                    shopurl=url+'p'+str(i)+'?'
                    print shopurl
                    f.write(shopurl)
                    f.write('\r\n')
	    
            else:
                page_number=re.findall('<a href="(.*?)" rel="nofollow" data-ga-page="(.*?)" class="PageLink"',myPage,re.S)
                if page_number:
                    number=number=page_number[-1][1]
                    for i in range(1,int(number)+1):
                        shopurl=url+'p'+str(i)+'?'
                        print shopurl
                        f.write(shopurl)
                        f.write('\r\n') 
		else:
		    f.write(url)
		    f.write('\r\n')
                        
        f.close()    
    def Get_shop_href(self,urls):
        #hh=self.Next_href(urls)
        #if hh==0:
            
        #f=open('next_href'+'.txt','r')
        #i=1
        #for line in f.readlines():
            #if i>0:
                #line=line.strip('\r\n')
	line='http://www.dianping.com/search/category/8/45/g27852'
	self.shophref_queue.put(line)
           # i=i+1
        while (self.shophref_queue.qsize()):
            f2=open('shop_href'+'.txt','a+')
            url=self.shophref_queue.get()
            print url
            pp=re.findall('\d+',url)
            #mm=pp[-2]
            #j=self.MuLU.name.index(mm) 
            #name=self.MuLU.name[j-1]
            try:
            	myPage=self.OpenPage.Getpage(url)

           
            	shophrefs=re.findall('" data-hippo-type="shop" title="(.*?)" target="_blank" href="(.*?)"  >',myPage,re.S)
            except Exception,e:
            	myPage=self.OpenPage.Getpage(url)
          
            url2='http://www.dianping.com'
            for href in shophrefs:

                shophref=url2+href[1]
                print shophref
                f2.write(shophref)
                f2.write('\r\n')
                f2.write('乒乓球馆')
                f2.write('\r\n')
            f2.close()
            #raw_input('wwwwww')
            
            
            
        
#ss=ShopHerf()
#ss.Get_shop_href('http://www.dianping.com/search/category/6/45/g6712')
    


















