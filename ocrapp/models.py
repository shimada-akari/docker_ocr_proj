from django.db import models

class ImageModel(models.Model):
    img = models.ImageField(blank=True, null=True, verbose_name="画像")
