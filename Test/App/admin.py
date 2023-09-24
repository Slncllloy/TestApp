from django.contrib import admin
from App.models import Product,ProductAccess,Lesson,LessonStatus

# Register your models here.

admin.site.register(Product)
admin.site.register(ProductAccess)
admin.site.register(Lesson)
admin.site.register(LessonStatus)
