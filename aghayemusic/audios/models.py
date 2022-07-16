from statistics import mode
from django.db.models import Q
from django.db import models
class Category(models.Model):
    slug = models.SlugField()
    name = models.TextField()
    def ___str___(self):
        return self.name
class Singer(models.Model):
    name = models.TextField(verbose_name='نام خواننده')
    slug = models.SlugField()
    def ___str___(self):
        return self.name

class product_manager(models.Manager):
    def search(self,que):
        lookup = (
            Q(name__icontains=que)|
            Q(Singer__name__icontains=que)|
            Q(id__icontains=que)
            )
        return self.get_queryset().filter(lookup).distinct()

class Audios_file(models.Model):
    name = models.TextField(verbose_name='نام آهنگ')
    src = models.TextField(default='none')
    img = models.ImageField(default=None,upload_to="photos/",blank=False)
    Singer = models.ManyToManyField(Singer)
    view = models.IntegerField(verbose_name='تعداد نمایش',default=10)
    category = models.ManyToManyField(Category)
    time = models.DateTimeField()
    objects = product_manager()
    def __str__(self):
        return self.name