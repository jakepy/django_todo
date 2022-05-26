from django.urls import path
from .views import task_list, task_detail, task_create, task_update, task_delete, custom_login, register_page
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', custom_login.as_view(), name='login'),
    path('register/', register_page.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', task_list.as_view(), name='tasks'),
    path('task/<int:pk>/', task_detail.as_view(), name='task'),
    path('update/<int:pk>/', task_update.as_view(), name='update'),
    path('delete/<int:pk>/', task_delete.as_view(), name='delete'),
    path('create', task_create.as_view(), name='create')
]