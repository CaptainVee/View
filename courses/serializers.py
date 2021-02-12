from rest_framework.serializers import (
	ModelSerializer, 
	HyperlinkedIdentityField,
	HyperlinkedModelSerializer,
	SerializerMethodField)
from rest_framework import fields
from .models import Course, Lesson, OrderItem, Order, Reviews, TAGS, STATUS
from django.contrib.auth.models import User
from rest_framework import fields, serializers

class CourseListSerializer(ModelSerializer):
	url = HyperlinkedIdentityField(view_name='course-detail', lookup_field='pk')
	author = SerializerMethodField()
	author_profile = HyperlinkedIdentityField(view_name='profile', lookup_field='pk')
	class Meta:
		model = Course
		fields = (
			'url','title', 'caption', 'author', 'price', 'cover_photo', 'tags', 'author_profile', 'average_star_rating'
			)
	def get_author(self, obj):
		return (obj.author.username)

class CourseDetailSerializer(serializers.HyperlinkedModelSerializer):
	tags = fields.MultipleChoiceField(TAGS)
	lessons = SerializerMethodField()
	reviews = SerializerMethodField()
	author = serializers.PrimaryKeyRelatedField(read_only=True)
	class Meta:
		model = Course
		fields = (
		'title', 'caption', 'price', 'cover_photo', 'author', 'tags', 'reviews', 'lessons', 'average_star_rating'
		)

	def get_lessons(self, obj):
		review_queryset = Lesson.objects.filter(course=obj.id)
		lesson = LessonSerializer(review_queryset, many=True).data
		return lesson[0], lesson[1]

	def get_reviews(self, obj):
		# to get all the reviews on the course
		review_queryset = Reviews.objects.filter(course=obj.id)
		reviews = ReviewSerializer(review_queryset, many=True).data
		return reviews

class ReviewSerializer(ModelSerializer):
	class Meta:
		model = Reviews
		fields = (
			'updated_at', 'course', 'body', 'created_by', 'star'
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