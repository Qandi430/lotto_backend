from rest_framework import routers
from .views import DrawHistoryViewSet
from django.urls import include,path

router = routers.DefaultRouter()
router.register('',DrawHistoryViewSet,'draw_history')

urlpatterns = router.urls
