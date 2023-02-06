from django.shortcuts import render
# 직렬 변환기 생성된 후, API에 대한 view를 생성하고 django url에 연결함
# 새 파일에서 생성한 각 모델에 대한 2개의 뷰 세트를 추가함
from rest_framework import viewsets
from my_api.serializers import PersonSerializer, SpeciesSerializer
from my_api.models import Person, Species

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class SpeciesViewSet(viewsets.ModelViewSet):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer

