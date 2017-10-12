from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext


from .models import Poll
from .models import Question


def index(request):
    polls = Poll.objects.order_by('-pub_date')[:100]
    context = {'polls': polls}

    return render_to_response('polls/index.html', context,
                              context_instance=RequestContext(request))


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
