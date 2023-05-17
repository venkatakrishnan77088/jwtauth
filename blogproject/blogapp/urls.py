from django.contrib import admin
from django.urls import path
from .views import RegisterView, LoginView, LogoutView, CreatepostView
urlpatterns = [
    path('admin/', admin.site.urls),

    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),

    path('logout', LogoutView.as_view()),

    path('createpost', CreatepostView.as_view())
]
