# 뷰셋 정의 후, DRF에서 제공하는 라우터 기능을 사용하여 원하는 API 엔드포인트를 주어진 뷰셋으로 라우팅가능

from django.urls import include, path
from rest_framework import routers
from my_api.views import PersonViewSet, SpeciesViewSet

router = routers.DefaultRouter()
router.register(r'people', PersonViewSet)
router.register(r'species', SpeciesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]