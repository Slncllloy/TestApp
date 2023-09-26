from rest_framework import serializers

from .models import Product,ProductAccess,Lesson,LessonStatus,User,Video


class sUser(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class sProduct(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('name',
                  'owner')
        
class sProduct_access(serializers.ModelSerializer):

    class Meta:
        model = ProductAccess
        fields = ('users',
                  'products',
                  'access')

class sLesson(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ('name',
                  'products',
                  'video_link',
                  'duration')

class sLesson_status(serializers.ModelSerializer):


    class Meta:
        model = LessonStatus
        fields = ('lesson',
                  'user',
                  'watch_timer',
                  'is_viewed',
                  'last_updated')
        
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

#-------------------------------------------------------------------------------------#

class sLesson_with_product(serializers.ModelSerializer):

    products = sProduct()

    class Meta:
        model = Lesson
        fields = '__all__'

class sLesson_status_with_lesson_and_product(serializers.ModelSerializer):

    lesson = sLesson_with_product()


    class Meta:
        model = LessonStatus
        fields = '__all__'

class sLesson_with_products(serializers.ModelSerializer):

    products = sProduct()

    class Meta:
        model = Lesson
        fields = '__all__'
