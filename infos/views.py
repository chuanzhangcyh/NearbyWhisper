from django.shortcuts import render

# Create your views here.
from.models import Infos
from django.http import HttpResponse
import json
from users.models import User
from django.forms import model_to_dict
import requests

def get_info(request):
    post_data = request.body.decode('utf-8')
    post_data = json.loads(post_data)
    longitude = post_data['longitude']
    latitude = post_data['latitude']
    info = post_data['info']
    # 安全接口
    access_token_url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx02d312003a5fec07&secret=39d7b4c593192f23844eadbffd6f37b8'
    access_token_response = requests.get(url=access_token_url)
    atres = json.loads(access_token_response.text)
    access_token = atres.get('access_token')
    url = 'https://api.weixin.qq.com/wxa/msg_sec_check?access_token=' + access_token
    msg = '{ "content":"%s" }' % (info)
    msg = msg.encode('utf-8')
    res = requests.post(url=url, data=msg)
    res = json.loads(res.text)
    errcode = res.get('errcode')
    # 接口出错则无法保存
    if errcode == 87014:
        return HttpResponse('wrong')
    else:
        session = request.session
        open_id = session.get('openid')
        poster_data = User.objects.get(open_id=open_id)
        poster_data = model_to_dict(poster_data)  # 把查询来的object数据转换成字典
        poster_id = poster_data['id']
        new_info = Infos(poster_id=poster_id,
                         latitude=latitude,
                         longitude=longitude,
                         info=info
                         )
        new_info.save()
        return HttpResponse('ok')