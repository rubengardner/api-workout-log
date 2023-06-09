from rest_framework import serializers
from .models import Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    """
    Serializer for the Exercise model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Exercise
        fields = [
            'id', 'owner', 'profile_id', 'created_at',
            'updated_at', 'name', 'is_owner',
            'unit_1', 'unit_2',
        ]
