from django.shortcuts import get_object_or_404
from pytz import timezone
from rest_framework import generics, status
from rest_framework.response import Response
from datetime import datetime, timedelta

from rest_framework.views import APIView

from elib.settings import TIME_ZONE
from apps.book.models import Book
import calendar
from apps.order.models import Order
from api.v1.order.serializers import OrderSerializer, OrderDetailSerializer, OrderCreateSerializer, OrderListSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# Create your views here.
class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    # queryset = Order.objects.all().prefetch_related('user', 'book').order_by('-time_of_get')
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Order.objects.filter(user__id=user.id).prefetch_related('user', 'book').order_by('-time_of_get')
        return queryset


class OrderIdentifyView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            response = []
            update = request.data['update']
            for data in request.data['orders']:
                order = Order.objects.filter(user__userlabel__inventory=data['user'], book__label__inventory=data['book'], retrieved=False).last()
                if order:
                    if update:
                        order.progress()
                    data['order'] = OrderListSerializer(order).data
                else:
                    data['order'] = None
                response.append(data)
            return Response({'orders': response}, status=status.HTTP_200_OK)
        except:
            return Response({"ok": False}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        try:
            response = []

            for data in request.data['orders']:
                order = Order.objects.filter(user_id=data['user'], book_id=data['book'], retrieved=False).last()
                if order:
                    data['order'] = OrderSerializer(order).data
                else:
                    data['order'] = None
                response.append(data)
            return Response({'orders': response}, status=status.HTTP_200_OK)
        except:
            return Response({"ok": False}, status=status.HTTP_400_BAD_REQUEST)


class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderCreateSerializer
    # queryset = Order.objects.all().prefetch_related('user', 'book').order_by('-time_of_get')
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Order.objects.all().prefetch_related('user', 'book').order_by('-time_of_get')
        user = self.request.user
        if not user.is_staff:
            queryset = queryset.filter(user__id=user.id)
        return queryset

    def perform_create(self, serializer):
        book_id = self.request.data.get('book')
        Book.decrement_book(Book, book_id)
        return serializer.save()


class ActiveOrderListView(generics.ListAPIView):
    serializer_class = OrderDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Order.objects.filter(active=True).order_by('-time_of_get')
        user = self.request.user
        if not user.is_staff:
            queryset = queryset.filter(user__id=user.id)
        return queryset


class ActiveOrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderDetailSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'order_id'

    def get_queryset(self):
        queryset = Order.objects.filter(id=self.kwargs['order_id'])
        return queryset


class BookInUseListView(generics.ListAPIView):
    serializer_class = OrderDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Order.objects.filter(active=False, done=True, retrieved=False).order_by('-time_of_get')
        user = self.request.user
        if not user.is_staff:
            queryset = queryset.filter(user__id=user.id)
        return queryset


class BookInUseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderDetailSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'order_id'

    def get_queryset(self):
        queryset = Order.objects.filter(id=self.kwargs['order_id'])
        return queryset


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        book_id = self.request.data.get('book')
        Book.increment_book(Book, book_id)
        return serializer.save()
    # pagination_class = None


# ADMIN VIEW


class OrderListAdminView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        queryset = Order.objects.all().prefetch_related('user', 'book').order_by('-time_of_get')
        user = self.request.user
        if not user.is_staff:
            queryset = queryset.filter(user__id=user.id)
        return queryset


class OrderShortListAdminView(generics.ListAPIView):
    serializer_class = OrderListSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        queryset = Order.objects.all().prefetch_related('user', 'book').order_by('-time_of_get')
        user = self.request.user
        if not user.is_staff:
            queryset = queryset.filter(user__id=user.id)
        return queryset


class OrderCreateAdminView(generics.CreateAPIView):
    serializer_class = OrderCreateSerializer
    # queryset = Order.objects.all().prefetch_related('user', 'book').order_by('-time_of_get')
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        queryset = Order.objects.all().prefetch_related('user', 'book').order_by('-time_of_get')
        user = self.request.user
        if not user.is_staff:
            queryset = queryset.filter(user__id=user.id)
        return queryset

    def perform_create(self, serializer):
        book_id = self.request.data.get('book')
        Book.decrement_book(Book, book_id)
        return serializer.save()


class ActiveOrderListAdminView(generics.ListAPIView):
    serializer_class = OrderDetailSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        queryset = Order.objects.filter(active=True).order_by('-time_of_get')
        user = self.request.user
        if not user.is_staff:
            queryset = queryset.filter(user__id=user.id)
        return queryset


class ActiveOrderDetailAdminView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderDetailSerializer
    permission_classes = [IsAdminUser]
    lookup_url_kwarg = 'order_id'

    def get_queryset(self):
        queryset = Order.objects.filter(id=self.kwargs['order_id'])
        return queryset


class BookInUseListAdminView(generics.ListAPIView):
    serializer_class = OrderDetailSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        queryset = Order.objects.filter(active=False, done=True, retrieved=False).order_by('-time_of_get')
        user = self.request.user
        if not user.is_staff:
            queryset = queryset.filter(user__id=user.id)
        return queryset


class BookInUseDetailAdminView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderDetailSerializer
    permission_classes = [IsAdminUser]
    lookup_url_kwarg = 'order_id'

    def get_queryset(self):
        queryset = Order.objects.filter(id=self.kwargs['order_id'])
        return queryset


class OrderDetailAdminView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAdminUser]

    def perform_update(self, serializer):
        book_id = self.request.data.get('book')
        Book.increment_book(Book, book_id)
        return serializer.save()


class StatsPerDay(OrderListView):
    @staticmethod
    def summarize(request, *args, **kwargs):
        """This can be moved to a Mixin class."""
        # make sure the filters of the parent class get applied
        tz = timezone(TIME_ZONE)
        date = datetime.now().astimezone(tz)
        time1 = date.replace(hour=9, minute=0, second=0)
        list1 = []
        list2 = []
        for i in range(1, 10):
            count = Order.objects.filter(time_of_get__gte=time1,
                                         time_of_get__lt=time1.replace(hour=time1.hour + 1))
            count1 = count.filter(active=False, done=True).count()
            count2 = count.filter(active=False, done=False).count()
            time1 = time1.replace(hour=time1.hour + 1)
            list1.append(count1)
            list2.append(count2)
        total_accepted = sum(list1)
        total_rejected = sum(list2)
        total = total_accepted + total_rejected
        stats = {
            'count_accepted': list1,
            'count_rejected': list2,
            'total_accepted': total_accepted,
            'total_rejected': total_rejected,
            'total': total,
        }
        return Response(stats)

    def get(self, request, *args, **kwargs):
        return self.summarize(request, *args, **kwargs)


class StatsPerWeek(OrderListView):

    @staticmethod
    def summarize(request, *args, **kwargs):
        date = datetime.today().date()
        start_week = date - timedelta(date.weekday())
        end_week = start_week + timedelta(7)
        list1 = []
        list2 = []
        while start_week != end_week:
            count = Order.objects.filter(time_of_get__year=start_week.year, time_of_get__month=start_week.month,
                                         time_of_order__day=start_week.day)
            start_week = start_week + timedelta(days=1)
            count1 = count.filter(active=False, done=True).count()
            count2 = count.filter(active=False, done=False).count()
            list1.append(count1)
            list2.append(count2)
        total_accepted = sum(list1)
        total_rejected = sum(list2)
        total = total_accepted + total_rejected
        stats = {
            'count_accepted': list1,
            'count_rejected': list2,
            'total_accepted': total_accepted,
            'total_rejected': total_rejected,
            'total': total,
        }
        return Response(stats)

    def get(self, request, *args, **kwargs):
        return self.summarize(request, *args, **kwargs)


class StatsPerMonth(OrderListView):

    @staticmethod
    def summarize(request, *args, **kwargs):
        date = datetime.today().date()
        print(date)
        start_month = date.replace(day=1)
        end_month = calendar.monthrange(date.year, date.month)[1]

        list1 = []
        list2 = []
        for i in range(1, end_month + 1):
            count = Order.objects.filter(time_of_get__year=start_month.year, time_of_get__month=start_month.month,
                                         time_of_get__day=start_month.day)
            start_month = start_month + timedelta(days=1)
            count1 = count.filter(active=False, done=True).count()
            count2 = count.filter(active=False, done=False).count()
            list1.append(count1)
            list2.append(count2)
        total_accepted = sum(list1)
        total_rejected = sum(list2)
        total = total_accepted + total_rejected
        stats = {
            'count_accepted': list1,
            'count_rejected': list2,
            'total_accepted': total_accepted,
            'total_rejected': total_rejected,
            'total': total,
        }
        return Response(stats)

    def get(self, request, *args, **kwargs):
        return self.summarize(request, *args, **kwargs)


class StatsPerYear(OrderListView):

    @staticmethod
    def summarize(request, *args, **kwargs):
        date = datetime.today().date()
        list1 = []
        list2 = []
        for i in range(1, 13):
            # print(i)
            start_month = date.replace(month=i)
            count = Order.objects.filter(time_of_get__year=start_month.year, time_of_get__month=start_month.month)
            count1 = count.filter(active=False, done=True).count()
            count2 = count.filter(active=False, done=False).count()
            list1.append(count1)
            list2.append(count2)
        total_accepted = sum(list1)
        total_rejected = sum(list2)
        total = total_accepted + total_rejected
        stats = {
            'count_accepted': list1,
            'count_rejected': list2,
            'total_accepted': total_accepted,
            'total_rejected': total_rejected,
            'total': total,
        }
        return Response(stats)

    def get(self, request, *args, **kwargs):
        return self.summarize(request, *args, **kwargs)

#
# class BookInUseListView(generics.ListCreateAPIView):
#     serializer_class = BookInUseSerializer
#     queryset = BookInUse.objects.all().prefetch_related('book', 'order_id')
#     permission_classes = [IsAuthenticated]
#     # pagination_class = None
#
#
# class BookInUseDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = OrderSerializer
#     queryset = Order.objects.all().prefetch_related('user', 'book')
#     permission_classes = [IsAuthenticated]
#     # pagination_class = None
#
#
# @csrf_exempt
# def order_list(request):
#     if request.method == 'GET':
#         orders = Order.objects.all()
#         serializer = OrderSerializer(orders, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = OrderSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
#
# @csrf_exempt
# def order_detail_search(request, user_id, book_id):
#     try:
#         user = Profile.objects.get(pk=user_id)
#         book = Book.objects.get(pk=book_id)
#     except Order.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         users_orders = Order.objects.filter(user == user_id)
#         print(users_orders)
#
#
# #
#
# @csrf_exempt
# def order_detail(request, pk):
#     try:
#         order = Order.objects.get(pk=pk)
#     except Order.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = OrderSerializer(order)
#         return JsonResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = OrderSerializer(order, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         order.delete()
#         return HttpResponse(status=204)
#
#
# @csrf_exempt
# def book_inuse_list(request):
#     if request.method == 'GET':
#         book = BookInUse.objects.all()
#         serializer = OrderSerializer(book, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = BookInUseSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
#
# @csrf_exempt
# def book_inuse_detail(request, pk):
#     try:
#         book_inuse = BookInUse.objects.get(pk=pk)
#     except BookInUse.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = BookInUseSerializer(book_inuse)
#         return JsonResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = BookInUseSerializer(book_inuse, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         book_inuse.delete()
#         return HttpResponse(status=204)
