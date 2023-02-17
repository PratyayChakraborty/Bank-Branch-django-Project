from django.shortcuts import render
from rest_framework import viewsets
from api.models import Bank,Branch
from api.serializer import BankSerializer,BranchSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.

# Bank View

class BankViewSet(viewsets.ModelViewSet):
    queryset=Bank.objects.all()
    serializer_class=BankSerializer
    #Bank/{bank_id}/branches
    @action(detail=True,methods=['get'])
    def branches(self, request,pk=None):
        try:
            bank=Bank.objects.get(pk=pk)
            brns=Branch.objects.filter(bank=bank)
            brns_seri=BranchSerializer(brns,many=True,context={'request':request})
            return Response(brns_seri.data)
        except Exception as e:
            return Response({
                'message':"Bank with this id not exist, please give a valid id"
            })
#Branch View
class BranchViewSet(viewsets.ModelViewSet):
    queryset=Branch.objects.all()
    serializer_class=BranchSerializer
