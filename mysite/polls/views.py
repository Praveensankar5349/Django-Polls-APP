from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Choice,Question
from django.urls import reverse
# Create your views here.

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list':latest_question_list,}
    # return HttpResponse(template.render(context,request))
    return render(request,'polls/index.html',context)
def test(request):
    return HttpResponse("Hai")
def members(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())
def detail(request,question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question,pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',
                      {
            'question':question,
            'error_message' : "You didn't make a choice"
            
                      })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect
