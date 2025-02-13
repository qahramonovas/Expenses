from django.db.models.aggregates import Sum
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.models import User, Expenses, Category
from apps.serializer import RegisterSerializer, ExpenseSerializer


@extend_schema(tags=['Auth'])
class CustomTokenObtainPairView(TokenObtainPairView):
    pass

@extend_schema(tags=['Auth'])
class CustomTokenRefreshView(TokenRefreshView):
    pass



@extend_schema(tags=['Auth'])
class RegisterView(CreateAPIView):
   serializer_class = RegisterSerializer
   query = User.objects.all()









# ===========================================================
@extend_schema(tags=['Expenses'])
               # responses=ExpenseSerializer
class ExpenseCreateView(CreateAPIView):
    queryset = Expenses.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@extend_schema(tags=['Expenses'])
class ExpenseListView(ListAPIView):
    queryset = Expenses.objects.all()
    serializer_class = ExpenseSerializer


@extend_schema(tags=['Expenses'])
class ExpenseDetailView(RetrieveAPIView):
    queryset = Expenses.objects.all()
    serializer_class = ExpenseSerializer


@extend_schema(tags=['Expenses'])
class ExpenseUpdateView(UpdateAPIView):
    queryset = Expenses.objects.all()
    serializer_class = ExpenseSerializer


@extend_schema(tags=['Expenses'])
class ExpenseDeleteView(DestroyAPIView):
    queryset = Expenses.objects.all()
    serializer_class = ExpenseSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        response_data = {
            "pk": instance.pk,
            "price": instance.price,
            "description": instance.description
        }
        instance.delete()


@extend_schema(tags=['Balance'])
class BalanceAPIView(APIView):
    def get(self, request):
        income_sum = Expenses.objects.filter(type='income').aggregate(total=Sum('amount'))['total'] or 0
        expense_sum = Expenses.objects.filter(type='expense').aggregate(total=Sum('amount'))['total'] or 0
        balance = income_sum - expense_sum
        return Response({"balance": balance}, status=status.HTTP_200_OK)


@extend_schema(tags=['Category'])
class CategoryListAPIView(APIView):
    def get(self, request, type):
        categories = Category.objects.filter(type=type).values('id', 'name')
        return Response(categories, status=status.HTTP_200_OK)
