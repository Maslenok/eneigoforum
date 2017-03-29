from django.shortcuts import render

from energotechnology.models import EnergotechnologyAll, EnergotechnologySun, EnergotechnologyEast, \
    EnergotechnologyWater, EnergotechnologyOtoplenie, EnergotechnologyOsveshenie
from staticpages.models import MainText


def energotechnologyAll(request):
    context = {}
    try:
        info=EnergotechnologyAll.objects.get()
        context={"info":info,}
    except:
        pass

    return render(request, 'energotechnology.html', context)


def energotechnology(request,name):
    try:
        if name == "sun":  info=EnergotechnologySun.objects.get()
        if name == "east":  info = EnergotechnologyEast.objects.get()
        if name == "water":  info = EnergotechnologyWater.objects.get()
        if name == "otoplenie":  info = EnergotechnologyOtoplenie.objects.get()
        if name == "osveshenie":  info = EnergotechnologyOsveshenie.objects.get()
        context = {"info": info, }
    except:
        try:
            index = MainText.objects.get()
            context = {'index': index, }
        except:
            context = { }
        return render(request, 'index.html', context)

    return render(request, 'energotechnology.html', context)


# Create your views here.
