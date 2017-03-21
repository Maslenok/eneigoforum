from django.shortcuts import render
from django.template.context_processors import csrf

from content.models import InfoText,MainText, InfoText
# Create your views here.


def index(request):

    info = MainText.objects.get()

    context={ "info":info,

    }
    print("Запускаем отображение  Index")

    return render(request, 'index.html', context)

def info(request):

    info = InfoText.objects.get()
    context={"info":info}
    print("Запускаем отображение  Info")

    return render(request, 'info.html', context)


def energotechnology(request):
    context = {}
    return render(request, 'base.html', context)



def newslist (request):
    context = {}
    return render(request, 'newsList.html', context)

def news (request, news):
    context = {}
    return render(request, 'news.html', context)

