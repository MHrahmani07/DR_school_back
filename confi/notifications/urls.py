from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SMSTemplateViewSet, SMSLogViewSet

router = DefaultRouter()
router.register(r'templates', SMSTemplateViewSet)
router.register(r'logs', SMSLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]