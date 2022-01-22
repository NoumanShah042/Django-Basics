from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import *


# Create your views here.

def index1(request):
    return HttpResponse("hello world")


def index3(request, id):
    return HttpResponse(f"hello world {id}")


def index4(request, name):
    return HttpResponse(f"hello world {name}")


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
