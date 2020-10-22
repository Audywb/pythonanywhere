from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.loginPage, name='login'),
    path('register', views.registerPage, name='register'),
    path('logout', views.logout, name='logout'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]