from rest_framework import viewsets
from .models import Manager, Intern
from .serializers import Managerserializer, Internserializer

class
Mangerserializer(viewsets,ModelViewset):
  queryset = Manager.objects.all()
  serializer_class = ManagerSerializer

class
Internserializer(viewsets,ModelViewset():
  queryset = Intern.objects.all()
  serializer_class = InternSerializer
