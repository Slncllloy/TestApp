
from django.urls import path
from . import views

urlpatterns = [
    path('lesson_status/',views.lesson_status.as_view()),
    path('lesson_status_by_product-<str:product_name>/',views.lesson_status_by_product.as_view()),
    path('is_viewed_lessons_count/',views.is_viewed_lessons_count.as_view()),
    path('is_viewed_lessons_count/',views.is_viewed_lessons_count.as_view()),
    path('watch_timer_sum/',views.watch_timer_sum.as_view()),
    path('user_count_in_product-<str:product_name>/',views.user_count_in_product.as_view()),
]