from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'dashboard'

urlpatterns = [
    path("", views.home, name="home"),
    path("features", TemplateView.as_view(template_name='dashboard/features.html'), name="features"),
]
