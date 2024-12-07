from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = [
            'id',
            'title',
            'description',
            'main_image_url',
            'footage_images',
            'genres',
            'os',
            'publisher',
            'developer',
            'created_at',
        ]  

class GameCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = [
            'id',
            'title',
            'main_image_url',
            'genres',
            'os',
        ]  