from rest_framework import serializers
from . models import UserProfile

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing the APIView"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True, 'style': {'input_type': 'password'}}} # set password to write only (create or update)

    def create(self, validated_data): # override the default create function to use the objects.create_user function (defined in models.py) 
        """Create and return a new user"""
        user = UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user