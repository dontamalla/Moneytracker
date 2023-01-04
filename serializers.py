from rest_framework import serializers
from app.models import User, Transaction

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name']

class TransactionSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Transaction
        fields = ['id', 'description', 'spending_category', 'amount', 'users']