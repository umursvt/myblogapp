# Create your views here.
from django.shortcuts import render
from datetime import datetime
from .models import *
from django.contrib import messages
from django.shortcuts import redirect, render

def get_current_time():
    #Get current time
    now = datetime.now()
    time = now.strftime('%H:%M')
    return time

def get_current_date():
    #Get current date
    date= datetime.now().date()
    return date
   




   


def current_lesson():
    current_time= get_current_time()
    current_date=get_current_date()
    
   
 #Tablodan gelen özel ders verisinin bilgilerini gerçek tarihe göre çeker
    current_lesson=ÖzelDers.objects.filter(ders_tarihi=current_date)
    print('Current lesson',current_lesson)   


       

    #Ucretler tablosuna veri girer 
    for i in (current_lesson):

        derslerin_tarihi=i.ders_tarihi
        if derslerin_tarihi == current_date:           
            derslerin_saati=i.ders_saati
            if (derslerin_saati) == current_time:
                öğrenci=i.öğrenci
                print('Verisi girilecek dersin öğrencisi:',öğrenci)
                if Ucretler.objects.filter(ders_tarihi=current_date, ders_saati=derslerin_saati).exists():
                    print('obje mevcut')
            
                else:
                    #Ders ücret kaydını hem öğrencinin tablosuna hem de ÜCRETLER tablosuna girer
                    ucret=Ucretler(isim=i.öğrenci,ders_tarihi=i.ders_tarihi,ders_saati=i.ders_saati,fiyat=i.fiyat)
                    print('Ucret tablosuna kayıt yapıldı.',i.öğrenci)
                    ucret.save()
                    print(str(i.öğrenci),type(str(i.öğrenci)),i.öğrenci)
                    if str(i.öğrenci) == 'MİRAY':
                        miray=Miray(isim=i.öğrenci,ders_tarihi=i.ders_tarihi,ders_saati=i.ders_saati,fiyat=i.fiyat)
                        miray.save()
                        print(i.öğrenci,'isimli öğrencinin dersi kaydedildi.')
                    elif str(i.öğrenci) == 'ZEYNEP YILMAZ':
                        zeynep=Zeynep(isim=i.öğrenci,ders_tarihi=i.ders_tarihi,ders_saati=i.ders_saati,fiyat=i.fiyat)
                        zeynep.save()
                        print(i.öğrenci,'isimli öğrencinin dersi kaydedildi.')  
                    elif str(i.öğrenci) == 'CEREN':
                        ceren=Ceren(isim=i.öğrenci,ders_tarihi=i.ders_tarihi,ders_saati=i.ders_saati,fiyat=i.fiyat)
                        ceren.save()
                        print(i.öğrenci,'isimli öğrencinin dersi kaydedildi.')
                    elif str(i.öğrenci) == 'DİLARA BİRDANE':
                        dilara=Dilara(isim=i.öğrenci,ders_tarihi=i.ders_tarihi,ders_saati=i.ders_saati,fiyat=i.fiyat)
                        dilara.save()
                        print(i.öğrenci,'isimli öğrencinin dersi kaydedildi.')
                    elif str(i.öğrenci) == 'DURU ÇİROZLAR':
                        duru=Duru(isim=i.öğrenci,ders_tarihi=i.ders_tarihi,ders_saati=i.ders_saati,fiyat=i.fiyat)
                        duru.save()
                        print(i.öğrenci,'isimli öğrencinin dersi kaydedildi.') 
                    elif str(i.öğrenci) == 'TEOMAN ÇİROZLAR':
                        teoman=Teoman(isim=i.öğrenci,ders_tarihi=i.ders_tarihi,ders_saati=i.ders_saati,fiyat=i.fiyat)
                        dilara.save()
                        print(i.öğrenci,'isimli öğrencinin dersi kaydedildi.')
                    elif str(i.öğrenci) == 'İPEK ATAKLI':
                        ipek=İpek(isim=i.öğrenci,ders_tarihi=i.ders_tarihi,ders_saati=i.ders_saati,fiyat=i.fiyat)
                        ipek.save()
                        print(i.öğrenci,'isimli öğrencinin dersi kaydedildi.')
                    elif str(i.öğrenci) == 'EMİR YEŞİL':
                        emir=Emir(isim=i.öğrenci,ders_tarihi=i.ders_tarihi,ders_saati=i.ders_saati,fiyat=i.fiyat)
                        emir.save()
                        print(i.öğrenci,'isimli öğrencinin dersi kaydedildi.') 
                    elif str(i.öğrenci) == 'BERKİN':
                        berkin=Berkin(isim=i.öğrenci,ders_tarihi=i.ders_tarihi,ders_saati=i.ders_saati,fiyat=i.fiyat)
                        berkin.save()
                        print(i.öğrenci,'isimli öğrencinin dersi kaydedildi.')
                    elif str(i.öğrenci) == 'EFLİN':
                        eflin=Eflin(isim=i.öğrenci,ders_tarihi=i.ders_tarihi,ders_saati=i.ders_saati,fiyat=i.fiyat)
                        eflin.save()
                        print(i.öğrenci,'isimli öğrencinin dersi kaydedildi.')
                    else:
                        print('Derse kaydı yapılamadı. Kontrol ediniz.')
            else:
                print('Bu tarihteki ders saatleri uygun değil')
        else:
            print('tarihler uyuşmuyor') 
 
    return 

    
    


       
            
    

def home(request):
    current_date=get_current_date()
    current_lesson()
   
    #öğrenci listesi
    öğrenci=Öğrenci.objects.all()

    #Filter the lessons to show in html by months
    all_lessons = ÖzelDers.objects.all()
   

    #Get only today's objects
    today=ÖzelDers.objects.filter(ders_tarihi=current_date)
    #Get ucretler for all
    ucretler=Ucretler.objects.all()
    time=get_current_time()

    #Bu ayın derslerini verir
    real_month=[]
    #Gerçek zamanın ay verisini alır.
    real_date=str(current_date)
    y=real_date.split('-')
    real_month.append(str(y[1]))
   
    month=ÖzelDers.objects.filter(ders_tarihi__month=real_month[0])

    ucretler=Ucretler.objects.all()
    toplam=0
    for i in ucretler:
        toplam += i.fiyat
    print('Ücretler tablosundaki toplam',toplam)
    


           


        
    context={
        'time':time,
        'ucret':ucretler,
        'today':today,
        'all_lessons':all_lessons,
        'öğrenci':öğrenci,
        'month':month
       
    }
    return render(request,'özelders/base.html',context)



def view_404(request,exception):
    return redirect('/')