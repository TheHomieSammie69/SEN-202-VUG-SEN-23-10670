from rest_framework import serializers
from .models import StaffBase, Manageer, Intern


class
StaffBaseSerializer(serializers.ModelSerializer):
  class Meta:
    model=StaffBase
    fields=['Id','name','email','intership ends']

class
ManagerSerializer(serializers.ModelSerializer):
  role=
  serializers.SerializerMethodField()

class Meta:
  model=Manager
  fields=['Id', 'name','email','company_card','intership_ends','role']

def get_role(self,obj):
  return obj.get_role()

class
InternSerisalizer(serializers.ModelSerializer):
  role=
  serializers.SerializerMethodField()
  class Meta:
    model=Intern
    fields=['Id','name','email','mentor','Intership_ends','role']

def get_role(self,obj):
  return obj.get_role()
