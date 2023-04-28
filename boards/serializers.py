from rest_framework import serializers
from boards.models import Board

class BoardSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.email

    class Meta:
        model = Board
        fields = "__all__"

class BoardCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ("title", "content")

class BoardListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.email

    class Meta:
        model = Board
        fields = ("id","title","user","updated_at")