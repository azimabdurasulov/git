from django.urls import path
from .views import TaskView,UserView


urlpatterns = [
    path('task', TaskView.as_view()),
    path('task/<int:pk>', TaskView.as_view()),
    path('user/<str:user>', UserView.as_view()),
]
