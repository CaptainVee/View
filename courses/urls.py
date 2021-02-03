from django.urls import path
from .views import(
	EnrollView,
	AddtoCartView,
	OrderListView,
	StartDetailView,
	PaymentListView,
	CourseCreateView,
	RetrieveUpdateDestroyView,
	RemoveFromCartView,
	LessonListCreateView,
	CourseListView
	)

urlpatterns = [
path('api/enroll/', EnrollView.as_view(), name='enroll'),
path('api/course/', CourseCreateView.as_view(), name='course-create'),
path('api/detail/<int:pk>/', RetrieveUpdateDestroyView.as_view(), name='course-detail'),
path('api/courses/', CourseListView.as_view(), name='courses-api'),
path('api/lesson/', LessonListCreateView.as_view(), name='lesson-create'),
path('api/order-summary/', OrderListView.as_view(), name='order-summary'),
path('api/add-to-cart/', AddtoCartView.as_view(), name='add-to-cart'),
path('api/remove-from-cart/', RemoveFromCartView.as_view(), name='remove-from-cart'),
# path('remove-item-from-cart/<int:pk>/', remove_single_item_from_cart,name='remove-single-item-from-cart'),
path('api/payment/', PaymentListView.as_view(), name='payment'),
# path('verify/', VerifyView.as_view(), name='verify'),
path('api/start/', StartDetailView.as_view(), name='start'),
]
