from django.contrib import admin
from django.urls import path,include
from api.views import BankViewSet,BranchViewSet
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'bank',BankViewSet)
router.register(r'branch',BranchViewSet)
urlpatterns = [
    path("",include(router.urls))
]