from rest_framework import serializers
from .models import Exercise
from django.contrib.auth.models import User

class ExerciseSerializer(serializers.ModelSerializer):
    """
    Serializer for the Exercise model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='owner.id',
        write_only=True,
        required=False
    )

    def create(self, validated_data):
        profile_id = validated_data.pop('owner')['id']
        exercise = Exercise.objects.create(owner_id=profile_id, **validated_data)
        return exercise

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
