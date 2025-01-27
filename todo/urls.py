from django.urls import path
from .views import TaskCreateView, TaskRetrieveUpdateDestroy, RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('tasks/', TaskCreateView.as_view(), name='task_list_ceate'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroy.as_view(), name='task_retrieve_update_destroy'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]