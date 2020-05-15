from django.http import HttpResponse
from django.forms import model_to_dict
from users.models import User
from util.get_info import get_info
from util.get_distance import get_distance
from util.extra_info import extra_info
import json
def infos(request):
    session = request.session
    open_id = session.get('openid')
    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')
    latitude = float(latitude)
    longitude = float(longitude)
    reader_data = User.objects.get(open_id=open_id)
    reader_data = model_to_dict(reader_data)
    reader_id = reader_data['id']  # 获得观看者的id，以免他看到自己发布的内容
    limits = 0
    info_num = 0
    while info_num < 50:  # 当用户获得超过50条信息或者已经经纬度已经超过1的范围时，停止循环
        limits += 0.01
        info_data = get_info(longitude, latitude, reader_id, limits)  # 从数据库获得数据
        info_num = len(info_data)
        if limits > 1:
            break
    data = []
    for info in info_data:  # 通过数据库的数据生成新的给前端的数据
        new_info = {}
        info = model_to_dict(info)  # 将info转换成字典
        info_text = info['info']
        info_longitude = info['longitude']
        info_latitude = info['latitude']
        distance = get_distance(latitude, longitude, info_latitude, info_longitude)  # 用haversine公式计算球面两点间的距离，保留两位有效数字
        new_info['text'] = info_text
        new_info['distance'] = distance
        new_info['id'] = info['id']
        data.append(new_info)
    if len(data) < 50:  # 如果数据不够50条，从自建文案库挑选50条（距离在0-10随机）以补充
        num = 50 - len(data)
        extra_data = extra_info(num)
        data = data + extra_data
    data = json.dumps(data)
    return HttpResponse(data, content_type='application/json')
