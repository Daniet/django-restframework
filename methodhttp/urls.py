from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register(r'methodhttp', views.MethodHttp, basename='method http')

urlpatterns = router.urls