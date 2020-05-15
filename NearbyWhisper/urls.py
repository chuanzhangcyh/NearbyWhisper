"""NearbyWhisper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users.views import login_by_code  # 登陆
from infos.views import get_info  # 上传悄悄话
from apis.views.info import infos  # 获取悄悄话
from tipoff.views import get_tipoff  # 获取举报信息

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('nearby/V1.0.0/login/', login_by_code),
    path('nearby/V1.0.0/post/', get_info),
    path('nearby/V1.0.0/infos/', infos),
    path('nearby/V1.0.0/tipoff/', get_tipoff)
]
