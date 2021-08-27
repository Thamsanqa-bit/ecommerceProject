from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models
from accounts.models import Customer

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=270)
    slug = models.SlugField(max_length=270)
    ordering = models.IntegerField(default=0)

    class Meta:
        ordering = ['ordering']

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, related_name='product', on_delete=models.CASCADE)
    title = models.CharField(max_length=270)
    slug = models.SlugField(max_length=270)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='upload/', null=True, blank=True)
    thumbnail = models.ImageField(upload_to='upload/', null=True, blank=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240*180.jpg'

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_oi = BytesIO()
        img.save(thumb_oi, 'JPEG', quality=85)

        thumbnail = File(thumb_oi, name=image.name)

        return thumbnail
