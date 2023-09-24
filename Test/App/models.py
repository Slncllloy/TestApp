from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=256)
    owner = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ProductAccess(models.Model):
    users = models.ForeignKey(User,on_delete=models.CASCADE)
    products = models.ForeignKey(Product,on_delete=models.CASCADE)
    access = models.IntegerField()


class Lesson(models.Model):
    name = models.CharField(max_length=256)
    products = models.ForeignKey(Product,on_delete=models.CASCADE)
    video_link = models.URLField()
    duration = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
class LessonStatus(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    watch_timer = models.PositiveIntegerField(verbose_name='Длительность просмотра (в секундах)')
    is_viewed = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True,null=True)

    def save(self, *args, **kwargs):
        if self.watch_timer >= self.lesson.duration * 0.8:
            self.is_viewed = True
        super().save(*args, **kwargs)

