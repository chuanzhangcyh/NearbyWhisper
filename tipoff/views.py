from django.shortcuts import render
from django.http import HttpResponse
from users.models import User
from django.forms import model_to_dict
from tipoff.models import Tipoff
def get_tipoff(request):
    session = request.session
    open_id = session.get('openid')
    poster_data = User.objects.get(open_id=open_id)
    poster_data = model_to_dict(poster_data)  # 把查询来的object数据转换成字典
    poster_id = poster_data['id']
    info_id = request.GET.get('info_id')
    new_tipoff = Tipoff(poster_id=poster_id,
                        info_id=info_id
                        )
    new_tipoff.save()
    return HttpResponse('ok')