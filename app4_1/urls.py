from django.urls import path
from .views import index, Update_view,delete

urlpatterns = [
    path("", index),
    path("Update_view/", Update_view),
    path("delete/", delete),
]
