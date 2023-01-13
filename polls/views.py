from inertia import render
from .models import Poll

# Create your views here.
def home(request):
    all_polls = Poll.objects.all()
    results = []
    for poll in all_polls:
        poll.choices = poll.choice_set.all()
        results.append(poll)
    return render(request, 'Polls/Index', props={
        'polls': results
    })
