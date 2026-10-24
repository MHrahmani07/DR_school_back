from rest_framework import generics
from .models import GradeLevel
from .serializers import GradeLevelSerializer


class GradeLevelListView(generics.ListAPIView):
    queryset = GradeLevel.objects.all()
    serializer_class = GradeLevelSerializer