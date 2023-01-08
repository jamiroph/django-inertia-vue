from inertia import render
from .models import Poll

# Create your views here.
def home(request):
    return render(request, 'Polls/Index', props={
        'polls': Poll.objects.all()
    })

def contact(request):
    return render(request, 'Contact', { 'supportEmail': "jamiroph@googlemail.com"})