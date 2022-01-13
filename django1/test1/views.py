from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Tests,Test_name

# Create your views here.
class Test_ser(serializers.ModelSerializer):
    class Meta:
        model = Tests
        fields = '__all__'

class product_view1(APIView):
    def get(self,*args,**kwargs):
        print(self.kwargs['pk'])
        all_agent = Tests.objects.filter(id=int(self.kwargs['pk']))
        serlized_agent = Test_ser(all_agent, many=True)
        return Response(serlized_agent.data)
class Test_name_ser(serializers.ModelSerializer):
    class Meta:
        model = Test_name
        fields = '__all__'

class product_view2(APIView):
    def get(self,*args,**kwargs):
        all_agent = Test_name.objects.all()
        serlized_agent = Test_name_ser(all_agent, many=True)
        return Response(serlized_agent.data)