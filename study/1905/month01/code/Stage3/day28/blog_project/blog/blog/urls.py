"""blog URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from . import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^test/$',views.test_api),
    re_path(r'^v1/users',include('user.urls')),
    re_path(r'^v1/tokens',include('btoken.urls')),
    re_path(r'^v1/topics',include('topic.urls')),
]

# 生成媒体资源路由
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)