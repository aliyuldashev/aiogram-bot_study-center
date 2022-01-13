from django.shortcuts import render
from .models import BigFieald,SecandField,VideoLessans
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class ser_product(serializers.ModelSerializer):
    class Meta:
        model = BigFieald
        fields = ['name','id']

class product_view(APIView):
    def get(self,*args,**kwargs):
        all_agent = BigFieald.objects.all()
        serlized_agent = ser_product(all_agent, many=True)
        return Response(serlized_agent.data)
class ser_secand(serializers.ModelSerializer):
    class Meta:
        model = SecandField
        fields = ['name','id','bigfield_id']

class secand_view(APIView):
    def get(self,*args,**kwargs):
        all_agent = SecandField.objects.all()
        serlized_agent = ser_secand(all_agent, many=True)
        return Response(serlized_agent.data)
class ser_video(serializers.ModelSerializer):
    class Meta:
        model = VideoLessans
        fields = ['id','Video','secondfield_id','character','name']

class video_view(APIView):
    def get(self,*args,**kwargs):
        all_agent = VideoLessans.objects.all()
        serlized_agent = ser_video(all_agent, many=True)
        return Response(serlized_agent.data)