from django.urls import path
from accounts.views import UsersListView, UsersDetailView


urlpatterns = [
    path('', UsersListView.as_view(), name='users-all'),
    path('<str:username>/', UsersDetailView.as_view(), name='user-details'),
]
