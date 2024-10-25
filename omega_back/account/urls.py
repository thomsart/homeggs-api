from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import UserLogin, UserLogout


account_urlpatterns = [
    # ####################
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    # ####################
    # path('users/', users_views.CustomUserList.as_view(), name='users-list'),
    # path('users/<int:pk>/', users_views.CustomUserDetail.as_view(), name='users-detail'),
    # path('memberships/', memberships_views.MembershipList.as_view(), name='memberships-list'),
    # path('memberships/<int:pk>/', memberships_views.MembershipDetail.as_view(), name='memberships-detail'),
]

account_urlpatterns = format_suffix_patterns(account_urlpatterns)