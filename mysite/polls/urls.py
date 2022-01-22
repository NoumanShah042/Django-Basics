from django.urls import path

from . import views

urlpatterns = [

    path('index1', views.index1, name="index1"),
    path('index3/<int:id>', views.index3, name="index3"),
    path('index4/<str:name>', views.index4, name="index4"),

    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
