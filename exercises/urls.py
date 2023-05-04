from django.urls import path
from profiles import views

urlpatterns = [
    path('exercises/', views.ExerciseList.as_view())
]
