from django.shortcuts import render
from staticpages.models import MainText, InfoText, Contact


def index(request):
    try:
        index = MainText.objects.get()
        context={ 'index': index,}
    except:
        context={

            }
    return render(request, 'index.html', context)


def info(request):
    try:
        info = InfoText.objects.get()
        context={"info":info}
    except:
        context={
        }

    return render(request, 'info.html', context)


def contact(request):

    try:
        index = Contact.objects.get()
        context={ 'index': index,}
    except:
        context={

            }
    return render(request, 'contact.html', context)
