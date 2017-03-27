from django.shortcuts import render, get_object_or_404
from django.template.context_processors import csrf
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from content.form import TestimonialsForm
from content.models import Answer, Question, Testimonials, News, FAQ
from staticpages.models import MainText


def skipopros(request):
    if request.POST :
        answer = Answer.objects.get(id=request.POST.get("cash", ""))
        try:
            request.session[str(answer.question)]
            pass
        except:
            answer.valueAnswer +=1
            answer.save()
            question=answer.question
            question.usersAnswers +=1
            question.save()
            request.session[str(question)] = True
            questionUsersAnswers=question.usersAnswers
            for answer in Answer.objects.filter(question=question):
                answer.persent=int((answer.valueAnswer/questionUsersAnswers)*100)
                answer.save()


    question = Question.objects.filter(is_active=True)[0]
    answer_list = Answer.objects.filter(question=question)

    try:
        index = MainText.objects.get()
        context={ 'index': index,
                  "answer_list": answer_list,
                  "usersAnswers": question.usersAnswers,
                  }
    except:
        context = {
            "answer_list": answer_list,
            "usersAnswers": question.usersAnswers,

        }
    return render(request, 'index.html', context)

def testimonials(request):
    if request.method == 'POST':
        print("Пытаемся записать форму")
        form = TestimonialsForm(request.POST)
        if form.is_valid():
            try:
                request.session["testimonials"]
                pass
            except:
                form.save()
                request.session["testimonials"] = True

    context = {}
    context.update(csrf(request))
    testimonials_list=Testimonials.objects.all()
    paginator = Paginator(testimonials_list, 10)
    page = request.GET.get('page')
    try:
        testimonials = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        testimonials = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        testimonials = paginator.page(paginator.num_pages)

    form = TestimonialsForm

    context={

        "form":form,
        "testimonials":testimonials,
    }
    return render(request, 'testimonials.html', context)

def newslist (request):
    news_list=News.objects.all()
    paginator = Paginator(news_list, 5)
    page = request.GET.get('page')
    try:
        news_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        news_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        news_list = paginator.page(paginator.num_pages)
    context = {"news_list":news_list,}
    return render(request, 'newsList.html', context)


def news (request, news):
    news_out = get_object_or_404(News, id=news)
    print("news_out", news_out)
    context = {
        "news":news_out,
    }
    return render(request, 'news.html', context)

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