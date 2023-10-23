from inertia import render
from .models import Poll
from django.http import HttpResponse

# Create your views here.
def home(request):
    all_polls = Poll.objects.order_by('-pub_date')[:5]
    return render(request, 'Polls/Index', props={
        'polls': all_polls
    })

def details(request, question_id):
    return HttpResponse("You're looking at question %s" % question_id)

def results(request, question_id):
    return HttpResponse("You're looking at the results  of question %s" % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)