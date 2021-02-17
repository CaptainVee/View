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
from rest_auth import views as rest_view




urlpatterns = [
    path('', include('courses.urls')),
    path('api/docs/', get_swagger_view(title='Tollgator')),
    path('rest-auth/', include('rest_auth.urls')),
    path('admin/', admin.site.urls),
    path('api/profile/<int:pk>/', UserDetailView.as_view(), name='profile'),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    
    path('password-reset-confirm/<uidb64>/<token>/',
    rest_view.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),




    # path('api-auth/', include('rest_framework.urls')),
    # path('api/login/', obtain_auth_token, name='obtain-token'),
    # path('api/login2/', UserLoginView.as_view(), name='login2'),
    # path('password-reset/', rest_view.PasswordResetView.as_view(template_name='user/password_reset.html'), 
    #     name='password_reset'),
    # path('password-reset-complete/', rest_view.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'), 
    #     name='password_reset_complete'),
    # path('password-reset/done/', 
    #     rest_view.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'), 
    #     name='password_reset_done'),
    # path('api/register/', UserCreateView, name='register'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
