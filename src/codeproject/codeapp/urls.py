from django.urls import path,include
from rest_framework import routers
from .views import UserViewset,DeveloperViewset,ExperienceViewset,EducationViewset,PostViewset
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)

router = routers.DefaultRouter()
router.register('users', UserViewset)
router.register('developers', DeveloperViewset)
router.register('experiences', ExperienceViewset)
router.register('educations', EducationViewset)
router.register('posts', PostViewset)


urlpatterns = [
    path('',include(router.urls)),
    path('verify/',TokenObtainPairView.as_view(),name='token_verify'),
]