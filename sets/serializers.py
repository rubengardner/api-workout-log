from rest_framework import serializers
from .models import Set


class SetSerializer(serializers.ModelSerializer):
    workout_id = serializers.ReadOnlyField(source='workout.id')

    
    class Meta:
        model = Set
        fields = [
            'id', 'owner', 'workout_id', 'created_at', 'reps', 
            'value_of_unit_1', 'value_of_unit_2',
        ]