from rest_framework import serializers
from .models import Set


class SetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    workout_id = serializers.ReadOnlyField(source='workout.id')
    exercise_name = serializers.ReadOnlyField(source='exercise.name')

    


    class Meta:
        model = Set
        fields = [
            'id', 'owner', 'workout_id', 'created_at', 'reps','exercise', 
            'value_of_unit_1', 'value_of_unit_2', 'exercise_name', 'workout'
        ] 