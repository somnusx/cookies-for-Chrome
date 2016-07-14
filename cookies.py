import re
import os
import sqlite3
import requests
from win32.win32crypt import CryptUnprotectData

def getcookiefromchrome(host='yaohuo.me'):
    cookiepath=os.environ['LOCALAPPDATA']+r"\Google\Chrome\User Data\Default\Cookies"
    sql="select host_key,name,encrypted_value from cookies where host_key='%s'" % host
    with sqlite3.connect(cookiepath) as conn:
        cu=conn.cursor()        
        cookies={name:CryptUnprotectData(encrypted_value)[1].decode() for host_key,name,encrypted_value in cu.execute(sql).fetchall()}
        
        return cookies

#运行环境windows 2012 server python3.4 x64 chrome 50
#以下是测试代码
#getcookiefromchrome()
#getcookiefromchrome('.baidu.com')

url='https://yaohw.com/myfile.aspx'

httphead={'User-Agent':'Safari/537.36',}


r=requests.get(url,headers=httphead,cookies=getcookiefromchrome(),allow_redirects=1)#,
s = r.text
lu =re.findall(r'http.+?mp4',s)
print(lu)
