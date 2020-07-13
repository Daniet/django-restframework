from rest_framework.viewsets import ModelViewSet

from . import models
from . import serializer

# Create your views here.
class ReportViewSet(ModelViewSet):

    queryset = models.Reporter.objects.all()
    serializer_class = serializer.ReporterSerializer

class ArticleViewSet(ModelViewSet):

    queryset = models.Article.objects.all()
    serializer_class = serializer.ArticleSerializer

