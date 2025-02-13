from django.contrib.auth.hashers import make_password
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from apps.models import User, Category, Expenses


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['full_name', 'phone_number', 'password']


    def validate_password(self, value):
        return make_password(value)


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'type', 'icon']




class ExpenseSerializer(ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = Expenses
        fields = ['id', 'amount', 'category', 'category_id', 'description', 'type']

