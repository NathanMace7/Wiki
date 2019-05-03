from django.urls import path

from . import views

app_name = 'wiki'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.DetailView.as_view(), name='detail'),
    path('save/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]
