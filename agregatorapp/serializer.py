from rest_framework import serializers

from agregatorapp.models import Log


class LogListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        exclude = ("id", "created_at", "updated_at")
