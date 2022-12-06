from email.policy import default
from django.db import models
from django.forms import CharField
from datetime import datetime
from django.utils.text import slugify




# Create your models here.




class Öğrenci(models.Model):
     isim_soyisim=models.CharField('İsim, Soyisim',max_length=25)
     
     def __str__(self):
         return self.isim_soyisim
     
        


    

class ÖzelDers(models.Model):
    öğrenci=models.ForeignKey(Öğrenci,max_length=25, on_delete=models.CASCADE, null=True, blank=True)
    ders_ad= models.CharField('Dersin adı',max_length=25)
    ders_konu= models.CharField('Ders konu',max_length=50)
    ders_tarihi=models.DateField()
    ders_saati=models.CharField(max_length=5)
    ders_yeri= models.CharField('Ders yeri',max_length=100, blank=True)
    fiyat= models.IntegerField(verbose_name='Ders ücreti', default=250)
    slug= models.SlugField(blank=True, unique=False, db_index=True)

    def __str__(self):
        return str(self.öğrenci)+ ' / ' + str(self.ders_tarihi) + ' / ' + str(self.ders_saati)

    def save(self,*args, **kwargs):
        self.slug=slugify(self.öğrenci)
        super().save(*args,**kwargs)




class Ucretler(models.Model):
    isim=models.CharField(max_length=20, null=False)
    ders_tarihi=models.DateField(null=True)
    ders_saati=models.CharField(max_length=5,null=False)
    fiyat= models.IntegerField(verbose_name='Ders ücreti', default=250,null=False)

    def __str__(self):
        return self.isim + '    -->   ' + str(self.ders_tarihi) + '    --->   ' + str(self.ders_saati)

# Öğrenci modelleri:

class Miray(models.Model):
    isim=models.CharField(max_length=20,null=False)
    ders_tarihi=models.DateField(null=False)
    ders_saati=models.CharField(max_length=5,null=False)
    fiyat=models.CharField(max_length=3,default=250)

    def __str__(self):
        return self.isim + '    -->   ' + str(self.ders_tarihi) + '    --->   ' + str(self.ders_saati)

class İpek(models.Model):
    isim=models.CharField(max_length=20,null=False)
    ders_tarihi=models.DateField(null=False)
    ders_saati=models.CharField(max_length=5,null=False)
    fiyat=models.CharField(max_length=3,default=250)

    def __str__(self):
        return self.isim + '    -->   ' + str(self.ders_tarihi) + '    --->   ' + str(self.ders_saati)

class Eflin(models.Model):
    isim=models.CharField(max_length=20,null=False)
    ders_tarihi=models.DateField(null=False)
    ders_saati=models.CharField(max_length=5,null=False)
    fiyat=models.CharField(max_length=3,default=250)

    def __str__(self):
        return self.isim + '    -->   ' + str(self.ders_tarihi) + '    --->   ' + str(self.ders_saati)

class Berkin(models.Model):
    isim=models.CharField(max_length=20,null=False)
    ders_tarihi=models.DateField(null=False)
    ders_saati=models.CharField(max_length=5,null=False)
    fiyat=models.CharField(max_length=3,default=250)

    def __str__(self):
        return self.isim + '    -->   ' + str(self.ders_tarihi) + '    --->   ' + str(self.ders_saati)

class Ceren(models.Model):
    isim=models.CharField(max_length=20,null=False)
    ders_tarihi=models.DateField(null=False)
    ders_saati=models.CharField(max_length=5,null=False)
    fiyat=models.CharField(max_length=3,default=250)

    def __str__(self):
        return self.isim + '    -->   ' + str(self.ders_tarihi) + '    --->   ' + str(self.ders_saati)

class Teoman(models.Model):
    isim=models.CharField(max_length=20,null=False)
    ders_tarihi=models.DateField(null=False)
    ders_saati=models.CharField(max_length=5,null=False)
    fiyat=models.CharField(max_length=3,default=250)

    def __str__(self):
        return self.isim + '    -->   ' + str(self.ders_tarihi) + '    --->   ' + str(self.ders_saati)
        
class Duru(models.Model):
    isim=models.CharField(max_length=20,null=False)
    ders_tarihi=models.DateField(null=False)
    ders_saati=models.CharField(max_length=5,null=False)
    fiyat=models.CharField(max_length=3,default=250)

    def __str__(self):
        return self.isim + '    -->   ' + str(self.ders_tarihi) + '    --->   ' + str(self.ders_saati)
class Emir(models.Model):
    isim=models.CharField(max_length=20,null=False)
    ders_tarihi=models.DateField(null=False)
    ders_saati=models.CharField(max_length=5,null=False)
    fiyat=models.CharField(max_length=3,default=250)

    def __str__(self):
        return self.isim + '    -->   ' + str(self.ders_tarihi) + '    --->   ' + str(self.ders_saati)

class Dilara(models.Model):
    isim=models.CharField(max_length=20,null=False)
    ders_tarihi=models.DateField(null=False)
    ders_saati=models.CharField(max_length=5,null=False)
    fiyat=models.CharField(max_length=3,default=250)

    def __str__(self):
        return self.isim + '    -->   ' + str(self.ders_tarihi) + '    --->   ' + str(self.ders_saati)

class Zeynep(models.Model):
    isim=models.CharField(max_length=20,null=False)
    ders_tarihi=models.DateField(null=False)
    ders_saati=models.CharField(max_length=5,null=False)
    fiyat=models.CharField(max_length=3,default=250)

    def __str__(self):
        return self.isim + '    -->   ' + str(self.ders_tarihi) + '    --->   ' + str(self.ders_saati)
