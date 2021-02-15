from rest_framework.serializers import (
	CharField,
	EmailField,
	ModelSerializer,
	ValidationError,
	HyperlinkedIdentityField,
	SerializerMethodField)

from django.contrib.auth.models import User
from user.models import Profile
from courses.models import Course
from rest_auth.registration.serializers import RegisterSerializer

# from rest_framework.response import Response
from rest_framework import serializers
# from allauth.account import app_settings as allauth_settings
# from allauth.utils import (email_address_exists, get_username_max_length)


# class RegisterSerializer(RegisterSerializer):
# 	phone = serializers.IntegerField()
# 	gender = serializers.CharField()

# 	def get_cleaned_data(self):
# 		return {
# 		    'gender': self.validated_data.get('gender', ''),
# 		    'email': self.validated_data.get('email', ''),
# 		    'phone': self.validated_data.get('phone', ''),

# 		}

# 	def save(self, request):
#         adapter = get_adapter()
#         user = adapter.new_user(request)
#         self.cleaned_data = self.get_cleaned_data()
#         adapter.save_user(request, user, self)
#         self.custom_signup(request, user)
#         setup_user_email(request, user, [])
#         return user

# user_obj = User(username=username, email=email)
# class RegisterSerializer(serializers.Serializer):
#     username = serializers.CharField(
#         max_length=get_username_max_length(),
#         min_length=allauth_settings.USERNAME_MIN_LENGTH,
#         required=allauth_settings.USERNAME_REQUIRED
#     )
#     email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
#     password1 = serializers.CharField(write_only=True)
#     password2 = serializers.CharField(write_only=True)
#     phone = serializers.IntegerField()

#     def validate_username(self, username):
#         username = get_adapter().clean_username(username)
#         return username

#     def validate_email(self, email):
#         email = get_adapter().clean_email(email)
#         if allauth_settings.UNIQUE_EMAIL:
#             if email and email_address_exists(email):
#                 raise serializers.ValidationError(
#                     _("A user is already registered with this e-mail address."))
#         return email

#     def validate_password1(self, password):
#         return get_adapter().clean_password(password)

#     def validate(self, data):
#         if data['password1'] != data['password2']:
#             raise serializers.ValidationError(_("The two password fields didn't match."))
#         return data

#     def custom_signup(self, request, user):
#         pass

#     def get_cleaned_data(self):
#         return {
#             'username': self.validated_data.get('username', ''),
#             'password1': self.validated_data.get('password1', ''),
#             'email': self.validated_data.get('email', ''),
#             'phone': self.validated_data.get('phone'),
#             'gender': self.validated_data.get('gender')
#         }

    # def save(self, request):
    #     adapter = get_adapter()
    #     user = adapter.new_user(request)
    #     self.cleaned_data = self.get_cleaned_data()
    #     adapter.save_user(request, user, self)
    #     self.custom_signup(request, user)
    #     setup_user_email(request, user, [])
    #     return user


class UserDetailSerializer(ModelSerializer):
	user = SerializerMethodField()
	email = SerializerMethodField()
	courses = SerializerMethodField()

	class Meta:		
		model = Profile
		fields = ('user', 'image', 'email', 'phone', 'gender', 'courses','is_instructor')

	def get_user(self, obj):
		return (obj.user.username)

	def get_email(self, obj):
		return (obj.user.email)

	def get_courses(self, obj):
		course_queryset = Course.objects.filter(author=obj.id)
		courses = UserCourseListSerializer(course_queryset, many=True).data
		return courses

class StudentDetailSerializer(ModelSerializer):
	user = SerializerMethodField()
	email = SerializerMethodField()
	class Meta:		
		model = Profile
		fields = ('user', 'image', 'email')

	def get_user(self, obj):
		return (obj.user.username)

	def get_email(self, obj):
		return (obj.user.email)

class UserCourseListSerializer(ModelSerializer):
	class Meta:
		# url = HyperlinkedIdentityField(view_name='course-detail', lookup_field='pk')
		model = Course
		fields = (
			'title', 'caption', 'price', 'cover_photo'
			)

# class UserCreateSerializer(ModelSerializer):
# 	email = EmailField(label='Email')
# 	class Meta:		
# 		model = User
# 		fields = (
# 			'username', 'email', 'password'
# 			)
# 		extra_kwargs = {'password': {'write_only': True}}

# 	def validate_email(self, value):
# 		email = value
# 		user_qs = User.objects.filter(email=email)
# 		if user_qs.exists():
# 			raise ValidationError('This user has already registered!.')
# 		return data

# 	def create(self, validated_data):

# 		print(validated_data)
# 		username = validated_data['username']
# 		email = validated_data['email']
# 		password = validated_data['password']
# 		user_obj = User(username=username, email=email)
# 		user_obj.set_password(password)
# 		user_obj.save()
# 		return validated_data

# class UserLoginSerializer(ModelSerializer):
# 	token = CharField(allow_blank=True, read_only=True)
# 	username = CharField()
# 	email = EmailField(label='Email')
# 	class Meta:		
# 		model = User
# 		fields = (
# 			'username', 'email', 'password', 'token'
# 			)
# 		extra_kwargs = {'password': {'write_only': True}}

# 	# def validate_email(self, value):
# 	# 	email = value
# 	# 	user_qs = User.objects.filter(email=email)
# 	# 	if user_qs.exists():
# 	# 		raise ValidationError('This user has already registered!.')
# 	# 	return data


