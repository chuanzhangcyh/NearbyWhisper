from django.shortcuts import render

# Create your views here.

import json
import requests
from.models import User
from django.http import HttpResponse

def login_by_code(request):
    code = request.GET.get('code')
    appid = 'wx02d312003a5fec07'
    appsecret = '39d7b4c593192f23844eadbffd6f37b8'
    url = 'https://api.weixin.qq.com/sns/jscode2session?appid=%s&secret=%s&js_code=%s&grant_type=authorization_code' % (appid, appsecret, code)
    url_response = requests.get(url=url)
    data = json.loads(url_response.text)
    openid = data.get('openid')  # 获得用户的openid
    request.session['openid'] = openid  # 保存session
    if not User.objects.filter(open_id=openid):
        new_user = User(open_id=openid)
        new_user.save()
        return HttpResponse('new ok')
    else:
        return HttpResponse('login ok')