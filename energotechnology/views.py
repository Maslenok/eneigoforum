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
        elif  name == "east":  info = EnergotechnologyEast.objects.get()
        elif  name == "water":  info = EnergotechnologyWater.objects.get()
        elif  name == "otoplenie":  info = EnergotechnologyOtoplenie.objects.get()
        elif  name == "osveshenie":  info = EnergotechnologyOsveshenie.objects.get()

        context = {"info": info, }
    except:
        context = { }


    return render(request, 'energotechnology.html', context)


# Create your views here.
