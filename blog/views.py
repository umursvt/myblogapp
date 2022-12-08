from django.shortcuts import render
from .models import*
from django.shortcuts import redirect, render
from email import message
from django.contrib import messages


# Create your views here.

def kripto(request):
    kripto=Kripto.objects.all().order_by('-id')
    for i in kripto:
        print(i.baslik, i.resim)

    context={
        'kripto':kripto
    }
    return render(request,'blog/kripto.html',context)

def kripto_detay(request,slug):
    kripto=Kripto.objects.filter(slug=slug)
    context={
        'kripto':kripto
    }
    return render(request, 'blog/kripto_detay.html',context)





def yazilim(request):
    yazilim=Yazilim.objects.all()
    for i in yazilim:
        print(i.baslik, i.resim)

    context={
        'yazilim':yazilim
    }
    return render(request,'blog/yazilim.html',context)

def yazilim_detay(request,slug):
    yazilim=Yazilim.objects.filter(slug=slug)
    context={
        'yazilim':yazilim
    }
    return render(request, 'blog/yazilim_detay.html',context)


def matematik(request):
    matematik=Matematik.objects.all()
    for i in matematik:
        print(i.baslik, i.resim)

    context={
        'matematik':matematik
    }
    return render(request,'blog/matematik.html',context)

def matematik_detay(request,slug):
    matematik=Matematik.objects.filter(slug=slug)
    context={
        'matematik':matematik
    }
    return render(request, 'blog/matematik_detay.html',context)

def iletisim(request):
    if request.method == 'POST':
        kullanici=request.POST['kullanici']
        email=request.POST['email']
        mesaj=request.POST['mesaj']

        if kullanici != '' and email != '' and mesaj != '':
            yeni_mesaj=Contact.objects.create(name=kullanici,email=email,mesaj=mesaj)
            yeni_mesaj.save()
            messages.success(request,'Mesajınız gönderildi')

        else:
            messages.error(request,'Tüm alanları doldurmalısınız')
            return redirect('yazilim')


    return render(request,'blog/iletisim.html')
