#coding=utf-8
import string
import xlwt
import re
workbook = xlwt.Workbook(encoding = 'utf-8') 
sheet = workbook.add_sheet("DZDP_suzhou",cell_overwrite_ok=True) 
style = xlwt.XFStyle()
font = xlwt.Font()
font.name = 'SimSun'    # 指定“宋体”
style.font = font 
#workbook.add_sheet('foobar', cell_overwrite_ok=True) 
#d.decode('utf-8')
sheet.write(0, 0,'shop_id' )
sheet.write(0, 1, 'shop_name')
sheet.write(0, 2, 'city')
sheet.write(0, 3, 'area')
sheet.write(0, 4, 'small_area')
sheet.write(0, 5, 'big_cate')
sheet.write(0, 6, 'phone')
sheet.write(0, 7, 'tel')
sheet.write(0, 8, 'time')
sheet.write(0, 9, 'tag')
sheet.write(0, 10, 'address')
sheet.write(0, 11, 'lat')
sheet.write(0, 12, 'lng')
sheet.write(0, 13, 'summary')
f=open('DZDP0322'+'.txt','r')
j=1
t=''
a=[]
mypage=f.read()
f.close()
mypage=mypage.replace('\r\n','')
mypage=mypage.split('fenjiexian')
for line in mypage:
    line=line.strip('\r\n')
    line=line.split('qq') 
    print line
    
    if len(line)>8:
        if line[0] not in a:
            a.append(line[0])
            del line[6]
            if len(line)==14:
                line.insert(6,'null')
                
            for i in range(len(line)):
                t=line[i].replace('\r\n','')
                t=line[i].replace('\n','')
                sheet.write(j, i, t)
            j=j+1
workbook.save("DZDP_suzhou.xls")   
