"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from user.views import  UserDetailView, FacebookLogin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_swagger.views import get_swagger_view




urlpatterns = [
    path('', include('courses.urls')),
    path('api/docs/', get_swagger_view(title='Tollgator')),
    # path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    # path('api/login/', obtain_auth_token, name='obtain-token'),
    # path('api/login2/', UserLoginView.as_view(), name='login2'),
    path('admin/', admin.site.urls),
    path('api/profile/<int:pk>/', UserDetailView.as_view(), name='profile'),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    # path('api/register/', UserCreateView, name='register'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
