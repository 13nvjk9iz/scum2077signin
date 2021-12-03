import requests
import os
import re
import sys

def auto_func(user, psw):
    s = requests.Session()
    user_url = "http://2077.scumgame.cn:7998"
    signin_url = "http://2077.scumgame.cn:7998/index/user/login.html"
    qiandao_url = "http://2077.scumgame.cn:7998/index/user/qiandao"
    r = s.get(signin_url)
    captcha_token = re.findall(r"__token__\" value=\"(.+?)\"", r.text)[0]
    account = user
    password = psw
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
    form_data = "url=index%2Fhome&__token__=" + captcha_token+"&account="+account+"&password="+password+"&keeplogin=1"
    user_resp = s.post(signin_url, form_data, headers=headers)
    res_login = re.findall(r"<h1>(.+?)</h1>", user_resp.text)[0]
    qiandao_resp = s.post(qiandao_url, headers=headers)
    res_qiandao = re.findall(r"<h1>(.+?)</h1>", qiandao_resp.text)[0]
    print(res_login)
    print(res_qiandao)
username = str(sys.argv[1])
password = str(sys.argv[2])
print(username)
auto_func(username, password)

