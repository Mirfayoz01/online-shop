from django.urls import path

from api.views import RegisterApiView, LoginApiView, UserUpdateView

urlpatterns = [
    path("register", RegisterApiView.as_view(), name="register"),
    path("user/<int:pk>/update", UserUpdateView.as_view(), name='user-update'),
    path("login", LoginApiView.as_view(), name="login"),
]