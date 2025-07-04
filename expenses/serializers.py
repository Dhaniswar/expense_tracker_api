from rest_framework import serializers
from .models import ExpenseIncome
from authentication.models import User




class ExpenseIncomeSerializer(serializers.ModelSerializer):
    total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = ExpenseIncome
        fields = [
            'id', 'user', 'title', 'description', 'amount', 
            'transaction_type', 'tax', 'tax_type', 'total',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['user', 'created_at', 'updated_at', 'total']
    
    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be greater than zero.")
        return value
    
    def validate_tax(self, value):
        if value < 0:
            raise serializers.ValidationError("Tax cannot be negative.")
        return value







class ExpenseIncomeListSerializer(serializers.ModelSerializer):
    total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    
    class Meta:
        model = ExpenseIncome
        fields = [
            'id', 'title', 'amount', 'transaction_type', 
            'total', 'created_at'
        ]
        read_only_fields = fields