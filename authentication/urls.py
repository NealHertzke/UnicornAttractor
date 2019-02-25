from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

app_name = 'authentication'
urlpatterns = [
    path('authentication/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    url(r'^login/$', auth_views.LoginView.as_view(),
        {'template_name': 'authentication/login.html'}, name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
]
