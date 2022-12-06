from django.db import models
from django.utils.text import slugify

# Create your models here.


class Kripto(models.Model):
    baslik=models.CharField(max_length=50)
    resim=models.ImageField(upload_to='media/')
    aciklama=models.TextField(max_length=1500)
    yazar=models.CharField(max_length=25)
    tarih=models.DateTimeField(auto_now_add=True)
    guncelleme_tarih=models.DateTimeField(auto_now=True)
    aktif=models.BooleanField()
    slug=models.SlugField(blank=True,default=" ", db_index=True,editable=False)

    def __str__(self):
        return self.baslik

    def save(self,*args, **kwargs):
        self.slug=slugify(self.baslik)
        super().save(*args,**kwargs)

class Yazilim(models.Model):
    baslik=models.CharField(max_length=50)
    resim=models.ImageField(upload_to='media/')
    aciklama=models.TextField(max_length=200)
    yazar=models.CharField(max_length=25)
    tarih=models.DateTimeField(auto_now_add=True)
    guncelleme_tarih=models.DateTimeField(auto_now=True)
    aktif=models.BooleanField()
    slug=models.SlugField(blank=True,default=" ", db_index=True,editable=False)

    def __str__(self):
        return self.baslik
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.baslik)
        super().save(*args,**kwargs)



class Matematik(models.Model):
    baslik=models.CharField(max_length=50)
    resim=models.ImageField(upload_to='media/')
    aciklama=models.TextField(max_length=200)
    yazar=models.CharField(max_length=25)
    tarih=models.DateTimeField(auto_now_add=True)
    guncelleme_tarih=models.DateTimeField(auto_now=True)
    aktif=models.BooleanField()
    slug=models.SlugField(blank=True,default=" ", db_index=True,editable=False)

    def __str__(self):
        return self.baslik
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.baslik)
        super().save(*args,**kwargs)



class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField(max_length=25)
    mesaj=models.TextField(max_length=350)

    def __str__(self):
        return self.name + ' ' + self.email