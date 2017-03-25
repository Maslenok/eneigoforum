from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from staticpages.models import MainText, InfoText, FAQ, Contact
from staticpages.models import EnergotechnologyAll, EnergotechnologySun, \
    EnergotechnologyEast, \
    EnergotechnologyWater, EnergotechnologyOsveshenie, EnergotechnologyOtoplenie


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


def energotechnologyAll(request):
    print("Общая энерготехнология")
    context = {}
    try:
        info=EnergotechnologyAll.objects.get()
        context={"info":info,}
    except:
        pass

    return render(request, 'energotechnology.html', context)


def energotechnology(request,name):
    print("Солнце энерготехнология")
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


def faq(request):
    faq_list=FAQ.objects.all()
    paginator = Paginator(faq_list, 5)
    page = request.GET.get('page')
    try:
        faq_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        faq_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        faq_list = paginator.page(paginator.num_pages)
    context = {"faq_list":faq_list,}
    return render(request, 'faq.html', context)


def contact(request):

    try:
        index = Contact.objects.get()
        context={ 'index': index,}
    except:
        context={

            }
    return render(request, 'contact.html', context)
