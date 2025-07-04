from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExpenseIncomeViewSet

router = DefaultRouter()
router.register(r'', ExpenseIncomeViewSet, basename='expenses')

urlpatterns = [
    path('', include(router.urls)),
]