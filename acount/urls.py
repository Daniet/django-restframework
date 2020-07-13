from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register(r'acount', views.UserViewSet, basename='acount')

urlpatterns = router.urls