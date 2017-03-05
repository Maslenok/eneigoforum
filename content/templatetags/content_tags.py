from django import template
from content.models import Answer,Question, News, Testimonials

register = template.Library()

@register.inclusion_tag("question_tag.html")
def tags_question():
    if Question.objects.all().count()>=1:
        question=Question.objects.all()[0]
        answer_list=Answer.objects.all()
        return {"answer_list":answer_list, "question":question}
    else:
        error_answer="Нет активных опросов "
        return {"error_answer":error_answer}

@register.inclusion_tag("news_tags.html")
def tags_news():
    if News.objects.all().count() >= 1:
        answer_list = News.objects.all()
        return {"news_list":answer_list}
    else:
        error_new="Нет новостей"
        return {"error_new": error_new}

@register.inclusion_tag("testimonials_tags.html")
def tags_testimonials():

    testimonials_list=Testimonials.objects.all()
    return {"testimonials_list":testimonials_list}
