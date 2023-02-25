from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='polls'),
    path('<int:question_id>/', views.details, name='details'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='results')
]