from rest_framework.serializers import (
	ModelSerializer, 
	HyperlinkedIdentityField,
	SerializerMethodField)
from .models import Post, Lesson, OrderItem, Order
from django.contrib.auth.models import User

class CourseListSerializer(ModelSerializer):
	url = HyperlinkedIdentityField(view_name='course-detail', lookup_field='pk')
	author = SerializerMethodField()
	class Meta:
		model = Post
		fields = (
			'url','title', 'content', 'author', 'price', 'image', 'category'
			)
	def get_author(self, obj):
		return (obj.author.user.username)


class CourseDetailSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = (
			'title', 'content', 'author', 'price'
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
		

class OrderItemSerializer(ModelSerializer):
	class Meta:
		model = OrderItem
		fields = (
			'user', 'ordered', 'item', 'quantity', 
			)