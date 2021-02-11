from django.shortcuts import get_object_or_404
from django.db.models import Q

from django.contrib.auth.models import User
from .models import Course, OrderItem, Order, Address, Lesson
from django.urls import reverse
from user.models import Profile
from django.http import JsonResponse
from paystackapi.transaction import Transaction
from paystackapi.paystack import Paystack

from .pagination import CourseLimitOffsetPagination
from django.http import JsonResponse


from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
    )

from .serializers import (  
    CourseListSerializer,
    LessonSerializer,
    OrderSerializer, 
    OrderItemSerializer,
    CourseDetailSerializer)



class CourseListView(ListAPIView):
    serializer_class = CourseListSerializer
    queryset = Course.objects.all()
    pagination_class = CourseLimitOffsetPagination
    filter_backends = [SearchFilter]
    search_fields = ['title', 'content', 'author__user__username', 'caption', 'tags']


class CourseCreateView(CreateAPIView):
    serializer_class = CourseDetailSerializer
    queryset = Course.objects.all()

    def perform_create(self, serializer):
        ''' this function is to make the author to be the person requesting it'''
        serializer.save(author=self.request.user.profile)


class RetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CourseDetailSerializer
    queryset = Course.objects.all()

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class LessonListCreateView(ListCreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = Lesson.objects.filter(course = request.query_params['course_pk'])
        serializer = LessonSerializer(queryset, many=True)
        return Response(serializer.data)

class OrderListView(ListAPIView):
    def get(self, request, *args, **kwargs):
        try:
            queryset = Order.objects.filter(user = request.user, ordered=False)
            serializer = OrderSerializer(queryset, many=True)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response(serializer.errors)


class StartDetailView(ListAPIView):
    def get(self, request, *args, **kwargs):
        order = OrderItem.objects.filter(user=request.user, ordered=True)
        if order.exists():
            serializer = OrderItemSerializer(order, many=True)

            return Response(serializer.data)
        context ={'object':'you have not enrolled for any course'}
        return Response(context)


class AddtoCartView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        item = get_object_or_404(Course, pk=request.query_params['pk'])
        order_item, created = OrderItem.objects.get_or_create(
            item=item,
            user=request.user,
            ordered=False
        )
        order_qs = Order.objects.filter(user=request.user, ordered=False)
        if order_qs.exists():
            order = order_qs[0]
        #     # check if the order item is in the order
            if order.items.filter(item__pk=item.pk).exists():
                order_item.quantity += 1
                order_item.save()
                context ={'object':'this course was updated'}
                return Response(context)
            else:
                order.items.add(order_item)
                context ={'object':'you have added this course'}
                return Response(context)
        else:
            ordered_date = timezone.now()
            order = Order.objects.create(user=request.user, ordered_date=ordered_date)
            order.items.add(order_item)
            context = {'request': "This item was added to your cart."}
            return Response(context)

class RemoveFromCartView(APIView):
    # permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        item = get_object_or_404(Course, pk=request.query_params['pk'])
        order_qs = Order.objects.filter(
            user=request.user,
            ordered=False
        )
        if order_qs.exists():
            order = order_qs[0]
            # check if the order item is in the order
            if order.items.filter(item__pk=item.pk).exists():
                order_item = OrderItem.objects.filter(
                    item=item,
                    user=request.user,
                    ordered=False
                )[0]
                order.items.remove(order_item)
                order_item.delete()
                context ={'object':'This item was removed from your cart.'}
                return Response(context)
            else:
                context ={'object':'This item was not in your cart'}
                return Response(context)

        else:
            context ={'object':'You do not have an active order'}
            return Response(context)

class PaymentListView(APIView):
    # permission_classes = (IsAuthenticated, ) 

    def get(self, request, *args, **kwargs):
        queryset = Order.objects.filter(user=request.user, ordered=False)
        order = queryset[0]
        price = Order.get_total(order)
        serializer = OrderSerializer(queryset, many=True)
        context = {
                    'data':serializer.data,
                    'price':price
                  }
        return Response(context)

class EnrollView(APIView):
    def get(self, request, *args, **kwargs):
        item = get_object_or_404(Course, pk=request.query_params['pk'])
        try:
            order_item = OrderItem.objects.filter(
            item=item,
            user=request.user)[0]

            if order_item.ordered == True:
                context ={'object':'you have already enrolled for this course.'}
                return Response(context)
        except Exception:
            order_item = OrderItem.objects.create(user=request.user, item=item, ordered=True)
            context ={'object':'You have successfully enrolled for this course.'}
            return Response(context)

# class VerifyView(View):
#     def get(self, request, id, *args, **kwargs):
#         order = Order.objects.get(user=self.request.user, ordered=False)
#         paystack = Paystack(secret_key=settings.PAYSTACK_SECRET_KEY)

#         # transaction = Transaction(authorization_key= settings.PAYSTACK_SECRET_KEY )
#         # response = transaction.verify(id)
#         transaction = paystack.transaction.initialize(reference=id,
#                                   amount='amount', email='email')
#         response = paystack.transaction.verify(reference=id)

#         order_items = order.items.all()
#         order_items.update(ordered=True)
#         for item in order_items:
#             item.save()

#         order.ordered = True
#         order.ref_code = create_ref_code()
#         order.save()

#         return JsonResponse(response, safe=False)


# class UserPostDetailView(View):
#     model = InstructorProfile
#     template_name = 'courses/instructor_detail.html'




# Create your views here.

def create_ref_code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))

def is_valid_form(values):
    valid = True
    for field in values:
        if field == '':
            valid = False
    return valid





# def remove_single_item_from_cart(request, pk):
#     item = get_object_or_404(Item, pk=pk)
#     order_qs = Order.objects.filter(
#         user=request.user,
#         ordered=False
#     )
#     if order_qs.exists():
#         order = order_qs[0]
#         # check if the order item is in the order
#         if order.items.filter(item__pk=item.pk).exists():
#             order_item = OrderItem.objects.filter(
#                 item=item,
#                 user=request.user,
#                 ordered=False
#             )[0]
#             if order_item.quantity > 1:
#                 order_item.quantity -= 1
#                 order_item.save()
#             else:
#                 order.items.remove(order_item)
#             messages.info(request, "This item quantity was updated.")
#             return redirect("order-summary")
#         else:
#             messages.info(request, "This item was not in your cart")
#             return redirect("post-detail", pk=pk)
#     else:
#         messages.info(request, "You do not have an active order")
#         return redirect("post-detail", pk=pk)

       
