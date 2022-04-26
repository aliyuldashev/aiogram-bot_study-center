from django.shortcuts import render
from .models import FirstField,SecandField,LastField, Post
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class ser_product(serializers.ModelSerializer):
    class Meta:
        model = FirstField
        fields = '__all__'
class product_view(APIView):
    def get(self,*args,**kwargs):
        all_agent = FirstField.objects.all()
        serlized_agent = ser_product(all_agent, many=True)
        return Response(serlized_agent.data)



class ser_secand(serializers.ModelSerializer):
    class Meta:
        model = SecandField
        fields = '__all__'
class secand_view(APIView):
    def get(self,*args,**kwargs):
        all_agent = SecandField.objects.filter(bigfield_id = int(self.kwargs['pk']))
        serlized_agent = ser_secand(all_agent, many=True)
        return Response(serlized_agent.data)



class ser_video(serializers.ModelSerializer):
    class Meta:
        model = LastField
        fields = '__all__'
class video_view(APIView):
    def get(self,*args,**kwargs):
        all_agent = LastField.objects.all()
        serlized_agent = ser_video(all_agent, many=True)
        return Response(serlized_agent.data)



class post_ser(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
class post_ser_view(APIView):
    def get(self,*args,**kwargs):
        all_agent = Post.objects.filter(id = int(self.kwargs['pk']))
        serlized_agent = post_ser(all_agent, many=True)
        return Response(serlized_agent.data)

