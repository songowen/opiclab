# config/urls.py (프로젝트의 메인 urls.py)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('dj_rest_auth.urls')),  # 로그인, 로그아웃, 비밀번호 변경
    path('api/v1/auth/registration/', include('dj_rest_auth.registration.urls')),  # 회원가입
]
