from django.shortcuts import render
from rest_framework import viewsets
from .serializers import (UserSerializer,DeveloperSerializer,EducationSerializer,
                          ExperienceSerializer,PostSerializer)
from .models import USER,Developer,Education,Experience,Post
from .permissions import DeveloperPermission,EEPermission,UserPermission,PostPermission
from rest_framework import response,authentication,permissions



class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (UserPermission,)
    queryset = USER.objects.all()
    
    
    
class DeveloperViewset(viewsets.ModelViewSet):
    serializer_class = DeveloperSerializer
    permission_classes = (DeveloperPermission,)
    queryset = Developer.objects.all()
    
    def create(self,request):
        if request.user.is_authenticated:
            developer = Developer(user=USER.objects.get(id=request.user.id),career=request.data['career'],
                                  company=request.data['company'],portfolioweb=request.data['portfolioweb'],
                                  location=request.data['location'],skills=request.data['skills'],
                                  githublink=request.data['githublink'],tweetlink=request.data['tweetlink'],
                                  fblink=request.data['fblink'],instalink=request.data['instalink'],
                                  youtubelink=request.data['youtubelink'],)
            developer.save()
            return response.Response({'Developer':request.user.username})
        return response.Response({'details':'Authentication Error'})
    
    
    
class ExperienceViewset(viewsets.ModelViewSet):
    serializer_class = ExperienceSerializer
    permission_classes = (EEPermission,)
    queryset = Experience.objects.all()

    def create(self,request):
        if request.user.is_authenticated:
            experience = Experience(whose=Developer.objects.get(user=request.user),
                                    job_title=request.data['job_title'],aff_company=request.data['aff_company'],
                                    loc_company=request.data['loc_company'],frm_date=request.data['frm_date'],
                                    to_date=request.data['to_date'],job_des=request.data['job_des'])
            experience.save()
            return response.Response({'Experience':request.data['job_title']})
        return response.Response({'details':'Authentication Error'})
    
    
    
class EducationViewset(viewsets.ModelViewSet):
    serializer_class = EducationSerializer
    permission_classes = (EEPermission,)
    queryset = Education.objects.all()
    
    def create(self,request):
        if request.user.is_authenticated:
            education = Education(whose=Developer.objects.get(user=request.user),degree=request.data['degree'],
                                  college=request.data['college'],frm_date=request.data['frm_date'],
                                  to_date=request.data['to_date'])
            education.save()
            return response.Response({'Education':request.data['degree']})
        return response.Response({'details':'Authentication Error'})
    
    
class PostViewset(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (PostPermission,permissions.IsAuthenticated,) #posts must occur only wher usr is authnd
    queryset = Post.objects.all()                                       

    def create(self,request):
        if request.user.is_authenticated:
            post = Post(whose=Developer.objects.get(user=request.user),text=request.data['text'])
            post.save()
            return response.Response({'PostText':request.data['text']})
        return response.Response({'details':'Authentication Error'})