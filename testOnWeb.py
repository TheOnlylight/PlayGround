import requests
import sys
import io
import ssl
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '4'
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  #改变标准输出的默认编码
# ssl._create_default_https_context = ssl._create_unverified_context
#登录时需要POST的数据
data = {
    'userAccount': '2019212992',
    'userPassword': '',
    'encoded': 'MjAxOTIxMjk5Mg==%%%cG9vaDIyMDNB'
}

#设置请求头
headers = {
    'User-agent':
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}

#登录时表单提交到的地址（用开发者工具可以看到）
login_url = 'https://10.3.58.19/jsxsd/xk/LoginToXk'

#构造Session
session = requests.Session()

#在session中发送登录请求，此后这个session里就存储了cookie
#可以用print(session.cookies.get_dict())查看
resp = session.post(login_url,data,headers,verify=False)

#登录后才能访问的网页
url = 'https://10.3.58.19/jsxsd/'
xuankeurl = 'https://10.3.58.19/jsxsd/xsxkkc/xxxkOper?kcid=3412110160&cfbs=null&jx0404id=202020211001756&xkzy=&trjf=&_=1601873522893'
xuanke = 'https://10.3.58.19/jsxsd/xsxk/xsxk_index?jx0502zbid=11CB38D49596468FAA892BC16E67AAA9';
#发送访问请求
resp = session.get(xuanke)
# resp = session.get('http://10.3.58.10:8080/jsxsd/xspj/xspj_find.do')
xuankedata={
    "kcid": '3412110160',
    'cfbs': 'null',
    'jx0404id': '202020211001756',
    'xkzy': '',
    'trjf': '',
    '_': '1601873522893'
}
while(1):
    resp = session.post(
    xuankeurl,xuankedata,headers,
    verify=False
    )
    pass
