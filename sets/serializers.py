from rest_framework import serializers
from .models import Set
from exercises.models import Exercise
from workouts.models import Workout


class SetSerializer(serializers.ModelSerializer):
    """
    Serializer for the Set model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    workout_id = serializers.ReadOnlyField(source='workout.id')
    exercise_name = serializers.ReadOnlyField(source='exercise.name')
    is_owner = serializers.SerializerMethodField()
    exercise = serializers.PrimaryKeyRelatedField(
        queryset=Exercise.objects.all()
        )
    workout = serializers.PrimaryKeyRelatedField(
        queryset=Workout.objects.all()
        )
    exercise_unit_1 = serializers.ReadOnlyField(source='exercise.unit_1')
    exercise_unit_2 = serializers.ReadOnlyField(source='exercise.unit_2')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    # Function that returns exercise and workouts that are owned by the user
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = self.context['request'].user
        if user.is_authenticated:
            self.fields['exercise'].queryset = Exercise.objects.filter(owner=user)
            self.fields['workout'].queryset = Workout.objects.filter(owner=user)

    class Meta:
        model = Set
        fields = [
            'id', 'owner', 'workout_id', 'created_at', 'reps', 'exercise',
            'value_of_unit_1', 'value_of_unit_2', 'exercise_name', 'workout',
            'is_owner', 'exercise_unit_1', 'exercise_unit_2'
        ]
