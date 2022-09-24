
from django.urls import path
from .views import poll_list, poll_detail

urlpatterns = [
    path('polls/', poll_list),
    path('polls/<int:id>', poll_detail),
]
