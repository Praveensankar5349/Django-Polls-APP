from django.urls import path

from . import views
app_name = 'polls'
urlpatterns = [
    path('polls/', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('members/', views.members, name='members'),
    # path('',views.index,name='index'),
    path('polls/<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('polls/<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('polls/<int:question_id>/vote/', views.vote, name='vote'),
]