from rest_framework import serializers
from .models import Set
from .models import Exercise

class SetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    workout_id = serializers.ReadOnlyField(source='workout.id')
    exercise_name = serializers.ReadOnlyField(source='exercise.name')
    is_owner = serializers.SerializerMethodField()
    exercise = serializers.PrimaryKeyRelatedField(queryset=Exercise.objects.all())

    
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = self.context['request'].user
        if user.is_authenticated:
            self.fields['exercise'].queryset = Exercise.objects.filter(owner=user)

    class Meta:
        model = Set
        fields = [
            'id', 'owner', 'workout_id', 'created_at', 'reps','exercise', 
            'value_of_unit_1', 'value_of_unit_2', 'exercise_name', 'workout',
            'is_owner'
        ] 