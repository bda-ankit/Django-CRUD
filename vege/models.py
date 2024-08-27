from django.db import models

class reciepe(models.Model):
    reciepe_name = models.CharField(max_length=100)
    reciepe_desc = models.TextField()
    reciepe_image = models.ImageField(upload_to="receipes")