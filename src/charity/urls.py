from rest_framework.routers import DefaultRouter

from charity import views


router = DefaultRouter()
router.register('charity', views.CharityViewSet, basename='charity')
urlpatterns = router.urls
