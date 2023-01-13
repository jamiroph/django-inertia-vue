from inertia import render
from django.contrib.auth.models import User
from .models import Post

# Create your views here.
def home(request):
    return render(request, 'Blogspot/Index', props={
        'posts': Post.objects.all()
    })

def contact(request):
    admin_user = User.objects.get(pk=1)
    return render(request, 'Contact', props={
        'supportEmail': admin_user.email
    })