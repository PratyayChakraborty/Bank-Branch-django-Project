from django.db import models

# Create your models here.

#Bank Model
class Bank(models.Model):
    bank_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name

# Branch Model

class Branch(models.Model):         
    branch_id=models.AutoField(primary_key=True)
    location=models.CharField(max_length=25)
    bank=models.ForeignKey(Bank, related_name="branches", on_delete=models.CASCADE)
    ifsc=models.CharField(max_length=11)

    # def __str__(self):
    #     return{
    #         self.location,
    #         self.ifsc,
    #     }