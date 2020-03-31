from django.shortcuts import render
from rest_framework import viewsets
from .serializers import (UserSerializer,DeveloperSerializer,EducationSerializer,
                          ExperienceSerializer)
from .models import USER,Developer,Education,Experience
from .permissions import DeveloperPermission,EEPermission,UserPermission

class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (UserPermission,)
    queryset = USER.objects.all()
    
class DeveloperViewset(viewsets.ModelViewSet):
    serializer_class = DeveloperSerializer
    permission_classes = (DeveloperPermission,)
    queryset = Developer.objects.all()
    
class ExperienceViewset(viewsets.ModelViewSet):
    serializer_class = ExperienceSerializer
    permission_classes = (EEPermission,)
    queryset = Experience.objects.all()
    
class EducationViewset(viewsets.ModelViewSet):
    serializer_class = EducationSerializer
    permission_classes = (EEPermission,)
    queryset = Education.objects.all()