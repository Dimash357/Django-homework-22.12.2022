from django.db import models

class Data(models.Model):
    data = models.CharField()

from rest_framework import serializers

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['data']
