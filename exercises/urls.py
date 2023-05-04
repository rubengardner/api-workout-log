from django.urls import path
from exercises import views

urlpatterns = [
    path('exercises/', views.ExerciseList.as_view()),
    path('exercises/<int:pk>', views.ExerciseSpecific.as_view())
]
