from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register(r'article', views.ArticleViewSet, basename='article')
router.register(r'report', views.ReportViewSet, basename='resport')

urlpatterns = router.urls