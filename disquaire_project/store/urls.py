from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.index, name='home'),
    path('list/', views.listing, name='listing'),
    path('<int:id>/', views.detail, name='detail'),
    path('search/', views.search, name='search'),
]