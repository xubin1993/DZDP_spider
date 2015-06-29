#coding=utf-8
import re 
import string
import Queue
from Open_page import Openpage
from Shop_href import ShopHerf
from Get_Jingwei import GetJinWei
from Muluget import MuLU
import xlwt
import os
import urllib2
#from bs4 import BeautifulSoup
class ShopMessage():
    def __init__(self):
        self.Openpage=Openpage()
        #self.Shophref=ShopHerf()
        self.Getjinwei=GetJinWei()
        #self.Mulu=MuLU()
        self.shophref=[]
	self.path=''
    def Get_photo(self,url):
	urlss=url+'/photos?'
	myPage=self.Openpage.Getpage(urlss)
	page_numbers=re.findall('class="PageLink" title="(.*?)"',myPage,re.S)
	if  page_numbers:
	    #print page_numbers
	    page_number=page_numbers[-1]#[0]
	    #print 'page_number=%s'%page_number
	    for i in range(1,int(page_number)+1):
		urls=url+'/photos?pg='+str(i)
		if i==1:
		    page_hrefs=re.findall('<img src="(.*?)"',myPage,re.S)
		    f12=open(self.path+'/'+'photo_href'+'.txt','a+')
		    for href in page_hrefs:
			href=href.replace('(249c249)','(700c700)')
			href=href.replace('(249x249)','(700x700)')	
			href=href.replace('(240c180)','(700x700)')
			f12.write(href)
			f12.write('\r\n')
		    f12.close()
		else:
		    myPage=self.Openpage.Getpage(urls)
		    page_hrefs=re.findall('<img src="(.*?)"',myPage,re.S)
		    f12=open(self.path+'/'+'photo_href'+'.txt','a+')
		    for href in page_hrefs:
			href=href.replace('(249c249)','(700c700)')
			href=href.replace('(249x249)','(700x700)')
			href=href.replace('(240c180)','(700x700)')
			f12.write(href)
			f12.write('\r\n')
		    f12.close()
	else:
	    page_hrefs=re.findall('<img src="(.*?)"',myPage,re.S)
	    f12=open(self.path+'/'+'photo_href'+'.txt','a+')
	    for href in page_hrefs:
		href=href.replace('(249c249)','(700c700)')
		href=href.replace('(249x249)','(700x700)')	
		href=href.replace('(240c180)','(700x700)')
		f12.write(href)
		f12.write('\r\n')
	    f12.close()    
	    
    def Save_message(self,a,j):
	new_path=self.path
	if not os.path.isdir(new_path):
	    os.makedirs(new_path)
	f=open(new_path+'/'+a[0]+'.txt','w+')	
	files=open('DZDP0322'+'.txt','a+')
        for i in range(len(a)):
            files.write(str(a[i]))
	    files.write('qq')
	    f.writelines(str(a[i]))
	    f.write('\r\n')
	f.close()
        files.write('\r\n')
	files.write('fenjiexian')
	files.write('\r\n')
	files.close()
    def Deal_mypage(self,myPage,uid,cate):
       #myPage=''''''
	self.path=''
        a=[]
        message=[]
	shopnamess=''
	if myPage:
        	fenji=re.findall('<a href="http://www.dianping.com/search/category/(.*?)" itemprop="url">(.*?)</a>',myPage,re.S)# 
	else:
	    self.Openpage.key=self.Openpage.key+1
	    return 0
	    
	#print fenji
	#raw_input('ssssssss')
        shopname=re.findall('<h1 class="shop-name">(.*?)<a class=',myPage,re.S)
        address=re.findall('<span itemprop="locality region">(.*?)</span></a>',myPage,re.S)
        address2=re.findall('<span class="item" itemprop="street-address" title="(.*?)">',myPage,re.S)
        tel=re.findall('<span class="item" itemprop="tel">(.*?)</span>',myPage,re.S)
        time=re.findall('<span class="info-name">营业时间：</span>(.*?)<span class="item">(.*?)</span>',myPage,re.S)
        tag=re.findall('rel="tag" target="_blank">(.*?)</a>',myPage,re.S)
        poi=re.findall('poi: "(.*?)"',myPage,)
        shanghujieshao=re.findall('<span class="info-name">商户简介：</span>(.*?)</p>',myPage,re.S)
        photo_href=re.findall('<a class="item" target="_blank" rel="nofollow" href="(.*?)" title="(.*?)">(.*?)<img src="(.*?)"/>(.*?)</a>',myPage,re.S)
        message.append(uid)
	self.path='data0322/'+cate
        for i in shopname:
            i=i.replace('\n','')
	    i=i.replace('\n    ','')
	    shopnamess=i
            message.append(i)
        city='苏州'
	self.path=self.path+'/'+city
        message.append(city)
        k=0
        for i in fenji:
	    if len(fenji)<=2:
		if k<1:
		    t=i[1]
		    t=t.replace('\n            ','')
		    t=t.replace('\n        ','')
		    message.append(t)
	    else:
		if k<3:
		    t=i[1]
		    t=t.replace('\n            ','')
		    t=t.replace('\n        ','')
		    message.append(t)		
		    k=k+1
        message.append(cate)
	if len(tel):
	    for i in tel :
		if len(tel)<2:
		    message.append(' ')
		    message.append(i)
		else:
		    message.append(i)
	else:
	    message.append('null')
	    message.append('null')
        for i in time:
            t=i[1]
            t=t.replace('\n                    ','')
            t=t.replace('\n                ','')
            t=t.replace('\r\n\n                ','')
            t=t.replace('\r\n','')  	    
            message.append(t) 
        j=''   
        for i in tag:
            j=j+i+' '
        message.append(j)
	if poi:
	    key=poi[0]
	    a=self.Getjinwei.decode(key)
	    for i in a:
		message.append(i)
	else:
	    for i in range(2):
		message.append('0.0')
	if address and address2:   
	    adds=address[0]+address2[0]
	    adds=adds.replace(',','')
	    message.append(adds)
        if shanghujieshao:
            for i in shanghujieshao:
                message.append(i)
        else:
            message.append('暂无商户简介')
        #for i in message:
            #print i 
	self.path=self.path+'/'+str(uid)
	
	
        return message
    def Get_Message(self,p):
	self.shophref=[]
        f=open('shop_href'+'.txt','r')
	j=1
        for line in f.readlines():
	    if j>p:
		line=line.strip('\r\n')
		#if line.find('" rel="nofollow')!=-1:
		line=line.replace('" rel="nofollow','')
		self.shophref.append(line)
	    j=j+1
        print len(self.shophref)
        f.close()	
        for i in range(0,len(self.shophref),2):
            message=[]
	    self.path=''
            url=self.shophref[i]
            print url
            key=self.shophref.index(url)
            cate=self.shophref[i+1]
            #url='http://www.dianping.com/shop/11563687'
            uids=re.findall('\d+',url)
            uid=uids[0]
	    try:
		myPage=self.Openpage.Getpage(url)
		message=self.Deal_mypage(myPage,uid,cate)
		if message==0:
		   #self.Get_Message(p)
		    myPage=self.Openpage.Getpage(url)
		    message=self.Deal_mypage(myPage,uid,cate)		    
		self.Save_message(message,j)
		self.Get_photo(url)
		p=p+2
		print "now is %d page"%p
		#raw_input('wwwwwwwww')
	    except urllib2.HTTPError:
		#print j
		
		self.Get_Message(p)            
	    except Exception , e:
		print e
		self.Get_Message(p)
            
            
        
        #print len(self.shophref)
ss=ShopMessage()
ss.Get_Message(0)




