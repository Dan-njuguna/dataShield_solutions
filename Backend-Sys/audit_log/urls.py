from django.urls import path
from . import views

urlpatterns = [
    path("logs/", (views.audit_log_list), name="audit_log_list"),
    path("logs/<slug:slug>/", (views.audit_log_detail), name="audit_log_detail"),
    path("logs/log_action/", (views.log_action_view), name="log_action"),
]