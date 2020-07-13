from rest_framework import serializers

from . import models

class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Article
        fields = '__all__'

class ReporterSerializer(serializers.ModelSerializer):

    class Meta:
        models = models.Reporter
        fields = '__all__'
