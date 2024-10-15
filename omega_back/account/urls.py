from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

# from .views import status_views, users_views, memberships_views


account_urlpatterns = [
    # ####################
    # path('login/', users_views.CustomUserLogin.as_view(), name='login'),
    # path('logout/', users_views.CustomUserLogout.as_view(), name='logout'),
    # ####################
    # path('status/', status_views.StatusViews.as_view({'get':'list'}), name='status-list'),
    # path('status/<int:pk>/', status_views.StatusViews.as_view({'get':'retrieve'}), name='status-detail'),
    # path('users/', users_views.CustomUserList.as_view(), name='users-list'),
    # path('users/<int:pk>/', users_views.CustomUserDetail.as_view(), name='users-detail'),
    # path('memberships/', memberships_views.MembershipList.as_view(), name='memberships-list'),
    # path('memberships/<int:pk>/', memberships_views.MembershipDetail.as_view(), name='memberships-detail'),
]

account_urlpatterns = format_suffix_patterns(account_urlpatterns)