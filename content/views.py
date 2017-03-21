from django.shortcuts import render

from content.models import Answer, Question


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

    context = {
             "answer_list":answer_list,
             "usersAnswers": question.usersAnswers,

             }
    return render(request, 'base2.html', context)

def testimonials(request):
    context={

    }
    return render(request, 'testimonials.html', context)

# Create your views here.
