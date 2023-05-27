from django.urls import path
from workouts import views

urlpatterns = [
    path('workouts/', views.WorkoutList.as_view()),
    path('workouts/<int:pk>', views.WorkoutSpecific.as_view())
]
