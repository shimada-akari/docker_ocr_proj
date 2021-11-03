from django.db import models

class ImageModel(models.Model):
    img = models.ImageField(blank=False, null=False, verbose_name="画像")
