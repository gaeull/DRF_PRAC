# DRF에 모델을 직렬화하는 과정
# 직렬 변환기는 models.py에 생성한 Person모델과 Species모델을 API에서 사용자에게 데이터를 반환하는데 사용할 JSON으로 변환함.
# 즉, serializers.py를 만들어 직렬 변환기를 추가함.

from rest_framework import serializers
from my_api.models import Person, Species

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'name', 'birth_year', 'eye_color', 'species')

class SpeciesSerializer(serializers.ModelSerializer):
        class Meta:
            model = Species
            fields = ('id', 'name', 'classification', 'language')
