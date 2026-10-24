from django.urls import path
from .views import GradeLevelListView

urlpatterns = [
    path('grade-levels/', GradeLevelListView.as_view(), name='grade-level-list'),
]