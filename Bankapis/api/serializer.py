from rest_framework import serializers
from api.models import Bank,Branch




#Bank serializer

class BankSerializer(serializers.HyperlinkedModelSerializer):
    # branches=BranchSerializer(many=True)
    class Meta:
        model = Bank
        fields =["name"]
        # fields = "__all__"
        # fields =["bank_id","name","branches"]

class BranchSerializer(serializers.HyperlinkedModelSerializer):
    bank=BankSerializer(many=False)
    class Meta:
        model = Branch
        fields = ["branch_id","location","ifsc","bank"]