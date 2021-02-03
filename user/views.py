from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm, StudentUpdateForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from .models import Profile

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView
    )

from .serializers import (  
  # UserCreateSerializer,
  # UserLoginSerializer,
  UserDetailSerializer,
  StudentDetailSerializer)

# class UserCreateView(CreateAPIView):
# 	serializer_class = UserCreateSerializer
# 	queryset = User.objects.all()

# class UserLoginView(APIView):
# 	serializer_class = UserLoginSerializer
# 	def post(self, request, *args, **kwargs):
# 		data = request.data
# 		serializer = UserLoginSerializer(data=data)
# 		if serializer.is_valid(raise_exception=True):
# 			return Response(serializer.data, status=HTTP_200_OK)
# 		else:
# 			return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class UserDetailView(RetrieveUpdateAPIView):
	serializer_class = UserDetailSerializer
	queryset = Profile.objects.all()


from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

	# def get(self, request, *args, **kwargs):
	# 	if request.user.profile.is_instructor == True:
	# 		serializer = StudentDetailSerializer(queryset)
	# 	else:
	# 		serializer = UserDetailSerializer(queryset)
	# 	return Response(serializer.data)


# def register(request):
# 	if request.method == 'POST':
# 		form = UserRegistrationForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			username = form.cleaned_data.get('username')
# 			messages.success(request, f'Account created for {username}!')
# 			return redirect('blog-home')

# 	else:
# 		form = UserRegistrationForm()
# 	return render(request, 'user/register.html', {'form' : form})

# @login_required
# def profile(request):
# 	if request.method == 'POST':
# 		u_form = UserUpdateForm(request.POST, instance=request.user)
# 		s_form = StudentUpdateForm(request.POST, instance=request.user.profile)
# 		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

# 		if u_form.is_valid() and p_form.is_valid():
# 			u_form.save()
# 			p_form.save()
# 			messages.success(request, f'Your Accounthas been updated!')
# 			return redirect('profile')
# 	else:
# 		u_form = UserUpdateForm(instance=request.user)
# 		p_form = ProfileUpdateForm(instance=request.user.profile)
# 		c_form = StudentUpdateForm(instance=request.user.profile)		

# 	context = {
# 		'u_form': u_form,
# 		'p_form': p_form,
# 		's_form': s_form
# 	}
# 	return render(request, 'user/profile.html', context)