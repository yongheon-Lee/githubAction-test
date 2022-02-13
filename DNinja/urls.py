from typing import Dict

from django.contrib import admin
from django.http import HttpRequest
from django.urls import path
from ninja import NinjaAPI  # ninja 객체 import

api = NinjaAPI()  # 객체 생성


@api.get("/add")  # view 함수를 데코레이터(@)로 감싸서 사용
def add(request: HttpRequest, a: int, b: int) -> Dict[str, int]:
    return {"result": a + b}


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]
