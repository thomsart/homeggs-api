from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from .views import UserLogin, UserLogout


app_url_marker = 'account/'
account_urlpatterns = [
    path(app_url_marker, include('djoser.urls')),
    path(app_url_marker, include('djoser.urls.authtoken')),
    path(app_url_marker, include('djoser.urls.jwt')),
    # ####################
    # path(app_url_marker + 'login/', UserLogin.as_view(), name='login'),
    # path(app_url_marker + 'logout/', UserLogout.as_view(), name='logout'),
    # ####################
    # path('users/', users_views.CustomUserList.as_view(), name='users-list'),
    # path('users/<int:pk>/', users_views.CustomUserDetail.as_view(), name='users-detail'),
    # path('memberships/', memberships_views.MembershipList.as_view(), name='memberships-list'),
    # path('memberships/<int:pk>/', memberships_views.MembershipDetail.as_view(), name='memberships-detail'),
]
# account_urlpatterns = format_suffix_patterns(account_urlpatterns, allowed=['json'])