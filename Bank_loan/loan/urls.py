from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('loan', views.ApprovalsView)
urlpatterns =[
    path('api', include(router.urls)),
    path('status/', views.approve_reject),
    path('form',views.cxcontact, name='csform')
]