from rest_framework import serializers
from .models import USER,Developer,Education,Experience,Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = USER
        fields = ('username','email','password',)
        extra_kwargs = {'password':{'write_only':True},'email':{'write_only':True}}

    def create(self, validated_data):
        user = USER(username=validated_data['username'],email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = ('user','career','company','portfolioweb','location','skills','bio','github',
                  'tweetlink','fblink','instalink','youtubelink','linkedinlink','username',)


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ('id','whose','job_title','aff_company','loc_company','frm_date',
                  'to_date','job_des',)


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ('id','whose','degree','college','frm_date','to_date',)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','whose','text','date','username',)