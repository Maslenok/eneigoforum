from django import template
from django.apps import AppConfig
from energotechnology import models
import energotechnology
from content.models import Answer,Question, News, Testimonials
from energotechnology.apps import EnergotechnologyConfig
from energotechnology.models import EnergotechnologyAll, EnergotechnologySun, EnergotechnologyWater, \
    EnergotechnologyEast, EnergotechnologyOsveshenie, EnergotechnologyOtoplenie


register = template.Library()

@register.inclusion_tag("question_tag.html")
def tags_question():

    try:
        question = Question.objects.get(is_active=True)
        answer_list = Answer.objects.filter(question=question)
        return {"answer_list": answer_list, "question": question}
    except:
        error_answer = "Нет активных опросов "
        return {"error_answer": error_answer}

@register.inclusion_tag("news_tags.html")
def tags_news():

    if News.objects.all().count() >= 1:
        answer_list = News.objects.all()[:3]
        return {"news_list":answer_list}
    else:
        error_new="Нет новостей"
        return {"error_new": error_new}

@register.inclusion_tag("testimonials_tags.html")
def tags_testimonials():
    if Testimonials.objects.all().count()>=1:
        testimonials_list=Testimonials.objects.all()[:3]
        return {"testimonials_list":testimonials_list}
    else:
        error_new="Нет отзывов.Вы будете первым"
        return {"error_new": error_new}





@register.inclusion_tag("energoforum_tag.html")
def tags_energoforum(app_list):
    for app in app_list:
        if app['app_label'] == "energotechnology":
            list_model=app["models"]
            for model in list_model:
                perm= model["perms"]
                if perm["add"] != True:
                    nameModel= str(model["object_name"])
                    if nameModel == "EnergotechnologySun" : model["object"]=EnergotechnologySun.objects.get()
                    if nameModel == "EnergotechnologyEast" : model["object"]=EnergotechnologyEast.objects.get()
                    if nameModel == "EnergotechnologyWater" : model["object"]=EnergotechnologyWater.objects.get()
                    if nameModel == "EnergotechnologyOsveshenie" : model["object"]=EnergotechnologyOsveshenie.objects.get()
                    if nameModel == "EnergotechnologyOtoplenie" : model["object"]=EnergotechnologyOtoplenie.objects.get()


    return  {"list_model":list_model}

