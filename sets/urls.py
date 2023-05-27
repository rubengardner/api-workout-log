from django.urls import path
from sets import views

urlpatterns = [
    path('sets/', views.SetList.as_view()),
    path('sets/<int:pk>', views.SetSpecific.as_view())
]
