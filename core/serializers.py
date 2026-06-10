from rest_framework import serializers
from .models import Team, Player, TeamGroup, Coach

class TeamGroupSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = TeamGroup
        fields = '__all__'  

class TeamSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Team
        fields = '__all__'

class PlayerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    team = TeamSerializer(read_only=True)

    class Meta:
        model = Player
        fields = '__all__'

class CoachSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Coach
        fields = '__all__'