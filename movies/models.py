from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Kategori(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Movies(models.Model):
    filmismi=models.CharField(max_length=200,verbose_name="Film Adı")
    aciklama=models.TextField(max_length=400,verbose_name="Açıklama")
    resim=models.FileField(upload_to='afis',blank=True,null=True,verbose_name="Resim")
    kategori=models.ForeignKey(Kategori,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.filmismi
    
class Izlenenler(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    izlenen=models.ManyToManyField('Movies',null=True)
    
    def __str__(self):
        return self.user.username