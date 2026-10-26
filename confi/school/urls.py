from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AcademicYearViewSet, GradeLevelViewSet, ClassRoomViewSet, StudentViewSet

router = DefaultRouter()
router.register(r'academic-years', AcademicYearViewSet)
router.register(r'grade-levels', GradeLevelViewSet)
router.register(r'classrooms', ClassRoomViewSet)
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]