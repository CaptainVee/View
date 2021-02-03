from rest_framework.serializers import (
	CharField,
	EmailField,
	ModelSerializer,
	ValidationError,
	HyperlinkedIdentityField,
	SerializerMethodField)

from django.contrib.auth.models import User
from user.models import Profile




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


class UserDetailSerializer(ModelSerializer):
	user = SerializerMethodField()
	email = SerializerMethodField()
	class Meta:		
		model = Profile
		fields = ('user', 'image', 'email', 'is_instructor')

	def get_user(self, obj):
		return (obj.user.username)

	def get_email(self, obj):
		return (obj.user.email)

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