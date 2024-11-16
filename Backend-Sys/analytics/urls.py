import sys
sys.dont_write_bytecode = True
from django.urls import path
from .views import MetricsView

urlpatterns = [
    path('metrics/', MetricsView.as_view(), name='metrics'),  # Endpoint for metrics
]