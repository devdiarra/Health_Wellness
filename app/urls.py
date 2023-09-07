
from django.urls import path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('peer/', TemplateView.as_view(template_name='pages/peer.html'), name='peer'),
    path('therapeut/', TemplateView.as_view(template_name='pages/therapit.html'), name='prof'),
]
