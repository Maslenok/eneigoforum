from django.shortcuts import render
from content.models import InfoText,MainText
# Create your views here.


def index(request):
    info = MainText.objects.get()
    context={"info":info}
    print("Вывод обьекта",info.mainText)

    return render(request, 'index.html', context)




def energotechnology(request):
    context = {}
    return render(request, 'base.html', context)




