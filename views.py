from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from app.serializers import UserSerializer, TransactionSerializer
from django.http import HttpResponse
from app.models import User, Transaction


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TransactionList(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

@api_view(['GET', 'POST'])
def healthz(request):
    return Response(status=200,data={"status": "ok"})