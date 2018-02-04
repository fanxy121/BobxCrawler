import requests
from bs4 import BeautifulSoup
import shutil
import os
import winsound
import win32clipboard
import win32con
payload = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'SurferLoyaltyRewards=41411497050845761986',
    'Host':'www.bobx.com',
    'Referer':'https://www.google.com.tw/',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
          }
#header
def wii(self):
    htp= self
    htp=htp.split('-')
    htp[-3]=int(htp[-3])+(int(htp[-2])*(int((htp[-1]).rstrip('.html'))))
    htp[-3]=str(htp[-3])
    htp='-'.join(htp)
    return (htp)

def judge(self,response):
    htp= self
    htp=htp.split('-')
    return int(htp[-3]) < int(response)

win32clipboard.OpenClipboard()
website = str(win32clipboard.GetClipboardData(win32con.CF_TEXT))[2:-1]
win32clipboard.CloseClipboard()
#choose the website of gallery and auto get it from clipboard

count=0
res = requests.get(website, headers=payload)
soup = BeautifulSoup(res.text)
name=str('\\'+soup.select('b')[0].text)
name1=str('\\'+soup.select('font')[0].text)
route=str('D:\pictures')
domain ='http://www.bobx.com'
picq=str(soup.select('td td td td .bronze')[0].text)
picq=picq.lstrip('@0 of')
picq=picq.rstrip(' pix')
picq=int(picq)

if os.path.exists(route) !=True:
    os.mkdir(route)
if os.path.exists(route+name) != True:
    os.mkdir(route+name)
if os.path.exists(route+name+name1) != True:
    os.mkdir(route+name+name1)
os.chdir(route+name+name1)
#Make File Folder

for i in range(1,int(picq/2)):
    if(count<picq):
        res = requests.get(website, headers=payload)
        soup = BeautifulSoup(res.text)
        for img in soup.select('img'):
            if '.jpg' in img['src'] :
                
                a=(img['src'].split('/'))
                s=str (img['src'].split('/')[-1])
                s=s.replace('preview','')
                
                ur=domain +( '/'+a[2] +'/' +a[3] +'/'+s)
                ur=ur.replace('--','-')  #��j��
            
                res2 = requests.get(ur, stream=True, headers=payload)
                f = open(s , 'wb')
                shutil.copyfileobj(res2.raw, f)
                f.close()
                count +=1
                print(str(ur) +'\n'+'�o�O��'+str(count)+'�i')
                del res2
        website=wii(website)
    else:
        break

winsound.Beep(600,500) 
#make a beep sound after this crawl downloader done

