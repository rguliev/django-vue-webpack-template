from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('page1/', TemplateView.as_view(template_name="firstapp/page1.html"), name="page1"),
    path('page2/', TemplateView.as_view(template_name="firstapp/page2.html"), name="page2"),
    path('', TemplateView.as_view(template_name="firstapp/index.html"), name="index"),
]