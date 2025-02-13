from django.urls import path, include

from apps.views import CustomTokenObtainPairView, CustomTokenRefreshView, RegisterView, ExpenseListView, \
    ExpenseDetailView, ExpenseCreateView, ExpenseUpdateView, ExpenseDeleteView, BalanceAPIView, CategoryListAPIView

urlpatterns = [
    path('auth/token/', CustomTokenObtainPairView.as_view()),
    path('auth/token/refresh/', CustomTokenRefreshView.as_view()),
]


urlpatterns += [
    path('user/register', RegisterView.as_view())
]



urlpatterns += [
    path('expenses/list', ExpenseListView.as_view()),
    path('expenses/detail/<int:pk>', ExpenseDetailView.as_view()),
    path('expenses/create', ExpenseCreateView.as_view()),
    path('expenses/update/<int:pk>', ExpenseUpdateView.as_view()),
    path('expenses/delete/<int:pk>', ExpenseDeleteView.as_view())
]




urlpatterns += [
    path('expenses/balance', BalanceAPIView.as_view()),
]



urlpatterns += [
    path('category/<str:type>', CategoryListAPIView.as_view(), name='category-list'),
]

