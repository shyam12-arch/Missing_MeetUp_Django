from rest_framework import serializers
from .models import MissingPerson

class MissingPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissingPerson
        fields = "__all__"