import urllib2
import time 
class GETIP:
    def Get_ip(self):
            time.sleep(1)
            url='ip_api'
            opener=urllib2.build_opener()
            request=urllib2.Request(url)
            response=opener.open(request)
            ip=response.read()
            response.close()
            f22=open('IP2'+'.txt','w+')
            f22.writelines(ip)
            f22.close()
#ss=GETIP()
#ss.Get_ip()
