from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import AdminManagmentViewSet, CurrentUserViewSet, sign_up, recieve_token

app_name = 'api'

router = SimpleRouter()
router.register('users', AdminManagmentViewSet, basename='admin_managment')

urlpatterns = [
    path('v1/auth/signup', sign_up, name='sign_up'),
    path('v1/auth/token', recieve_token, name='recieve_token'),
    path('v1/users/me', CurrentUserViewSet.as_view({'get': 'retrieve', 'patch': 'update'}), name='current_user'),
    path('v1/', include(router.urls))
]
