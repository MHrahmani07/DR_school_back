from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AttendanceViewSet, DisciplineRecordViewSet

router = DefaultRouter()
router.register(r'attendances', AttendanceViewSet)
router.register(r'disciplines', DisciplineRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]