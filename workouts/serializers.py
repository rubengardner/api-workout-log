from rest_framework import serializers
from .models import Workout


class WorkoutSerializer(serializers.ModelSerializer):
    sets_count = serializers.ReadOnlyField()
    owner = serializers.ReadOnlyField(source='owner.username')
    exercise_count = serializers.ReadOnlyField()
    
    class Meta:
        model = Workout
        fields = [
            'id', 'created_at', 'sets_count', 'owner', 'exercise_count'
        ]