from django.shortcuts import render

# Create your views here.
def index(request):

    context = {}
    return render(request, 'base.html', context)

def skipopros(request):
    if request.POST and (request.session["question"] != question):
        print("Эзапись значения")



    else:
        print("Метод НЕ Post")

    context = {}
    return render(request, 'base.html', context)


def energotechnology(request):
    context = {}
    return render(request, 'base.html', context)




