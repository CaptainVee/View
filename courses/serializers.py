from rest_framework.serializers import (
	ModelSerializer, 
	HyperlinkedIdentityField,
	HyperlinkedModelSerializer,
	SerializerMethodField)
from rest_framework import fields
from .models import Post, Lesson, OrderItem, Order, CATEGORY_CHOICES, LABEL_CHOICES
from django.contrib.auth.models import User
from rest_framework import fields, serializers

class CourseListSerializer(ModelSerializer):
	url = HyperlinkedIdentityField(view_name='course-detail', lookup_field='pk')
	author = SerializerMethodField()
	author_profile = HyperlinkedIdentityField(view_name='profile', lookup_field='pk')
	class Meta:
		model = Post
		fields = (
			'url','title', 'content', 'author', 'price', 'image', 'my_field2', 'author_profile'
			)
	def get_author(self, obj):
		return (obj.author.user.username)


class CourseDetailSerializer(serializers.HyperlinkedModelSerializer):
	my_field2 = fields.MultipleChoiceField(CATEGORY_CHOICES)
	author = serializers.PrimaryKeyRelatedField(read_only=True)
	class Meta:
		model = Post
		fields = (
		'title', 'content', 'price', 'image', 'author', 'my_field2'
		)

class LessonSerializer(ModelSerializer):
	class Meta:
		model = Lesson
		fields = (
			'title', 'course', 'video', 'position', 'description'
			)

class OrderSerializer(ModelSerializer):
	class Meta:
		model = Order
		fields = (
			'user', 'ordered', 'items',
			)
class PostSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = (
			'title'
			)	

class OrderItemSerializer(ModelSerializer):
	class Meta:
		model = OrderItem
		fields = (
			'user', 'ordered', 'item', 'quantity', 
			)