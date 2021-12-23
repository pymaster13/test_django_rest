from django.urls import path

from .views import CreateUserView, DeleteUserView, UserListView


urlpatterns = [
    path('all/', UserListView.as_view(), name='users_set'),
    path('create/', CreateUserView.as_view(), name='create_user'),
    path('delete/', DeleteUserView.as_view(), name='delete_user'),
]

