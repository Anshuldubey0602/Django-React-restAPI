from rest_framework import serializers
from .models import *

class taskSerializer(serializers.ModelSerializer):
    class Meta:
        model = todoList
        fields = '__all__'