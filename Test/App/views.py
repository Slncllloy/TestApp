from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from django.db.models import Sum


USER_IN_PRODUCT_COUNT_ERROR = {
    "detail": "count of product does not exist."
}
WATCH_TIMER_SUM_ERROR = {
    "detail": "watch timer sum does not exist."
}
IS_VIEWED_LESSONS_COUNT_ERROR = {
    "detail": "is viewed lessons count does not exist."
}
LESSON_STATUS_ERROR = {
    "detail": "lesson_status does not exist."
}

class lesson_status(ListAPIView):
    serializer_class = sLesson_status_with_lesson_and_product
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        try:
            lesson_status_by_user = LessonStatus.objects.filter(user=user)

            if not lesson_status_by_user.exists():
                return Response(LESSON_STATUS_ERROR, status=404)
            return lesson_status_by_user
        except:
            return Response(LESSON_STATUS_ERROR, status=404)
        
class lesson_status_by_product(ListAPIView):
    serializer_class = sLesson_status
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        product_name = self.kwargs['product_name']
        user = self.request.user

        try:
            product_by_name = Product.objects.filter(name = product_name).first()
            lesson_by_product = Lesson.objects.filter(products = product_by_name)
            lesson_status_by_lesson = LessonStatus.objects.filter(lesson__in = lesson_by_product,user = user)

            return lesson_status_by_lesson
        except:
            return Response(LESSON_STATUS_ERROR, status=404)
        
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        
        if not queryset.exists():
            return Response(LESSON_STATUS_ERROR, status=404)
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)
        
    
class is_viewed_lessons_count(APIView):

    @staticmethod
    def resp(val):
            return Response(
                            {
                                'is_viewed_lessons_count':val
                            }
                        )
        
    def get(self,request):
        global IS_VIEWED_LESSONS_COUNT_ERROR

        try:
            count = LessonStatus.objects.filter(is_viewed=True).count()
            
            return is_viewed_lessons_count.resp(count)
        except:
            return Response(IS_VIEWED_LESSONS_COUNT_ERROR,status=404)
        

class watch_timer_sum(APIView):

    @staticmethod
    def resp(val):
            return Response(
                            {
                                'watch_timer_sum':val
                            }
                        )
    
    def get(self,requset):
        global WATCH_TIMER_SUM_ERROR

        try:
            sum = LessonStatus.objects.aggregate(Sum('watch_timer'))

            if sum is None:
                return Response(WATCH_TIMER_SUM_ERROR, status=404)
            
            return Response(sum)
        except:
            return Response(WATCH_TIMER_SUM_ERROR,status=404)

class user_count_in_product(APIView):

    @staticmethod
    def resp(val):
            return Response(
                            {
                                'user_in_product_count':val
                            }
                        )
    
    def get(self, request, *args, **kwargs):
        global USER_IN_PRODUCT_COUNT_ERROR

        product_name = self.kwargs['product_name']

        try:
            product_by_name = Product.objects.filter(name=product_name).first()

            if product_by_name is None:
                return Response(USER_IN_PRODUCT_COUNT_ERROR, status=404)
            users_count = ProductAccess.objects.filter(products=product_by_name).count()

            return user_count_in_product.resp(users_count)
        except:
            return Response(USER_IN_PRODUCT_COUNT_ERROR,status=404)
