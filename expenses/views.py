from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db import models
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import ExpenseIncome
from .serializers import ExpenseIncomeSerializer, ExpenseIncomeListSerializer
from .permissions import IsOwnerOrAdmin
from .filters import ExpenseIncomeFilter
from drf_yasg.utils import swagger_auto_schema
from expense_tracker_api.custom_response import StandardResponseMixin







class ExpenseIncomeViewSet(StandardResponseMixin, viewsets.ModelViewSet):
    """
    A viewset for viewing and managing expense/income records.
    """
    queryset = ExpenseIncome.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ExpenseIncomeFilter
    filterset_fields = ['transaction_type', 'tax_type']
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ExpenseIncomeListSerializer
        return ExpenseIncomeSerializer
    
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return self.queryset.all()
        return self.queryset.filter(user=user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    @action(detail=False, methods=['get'])
    def summary(self, request):
        """
        Provides a summary of expenses and incomes
        """
        user = request.user
        queryset = self.filter_queryset(self.get_queryset())
        
        total_expenses = queryset.filter(transaction_type='debit').aggregate(
            total=models.Sum('amount')
        )['total'] or 0
        
        total_incomes = queryset.filter(transaction_type='credit').aggregate(
            total=models.Sum('amount')
        )['total'] or 0
        
        net_balance = total_incomes - total_expenses
        
        return Response({
            'total_expenses': total_expenses,
            'total_incomes': total_incomes,
            'net_balance': net_balance
        })