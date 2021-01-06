from django.urls import path
from todolist import views
urlpatterns = [
    
    path('', views.todolist , name = 'todolist'),
    path('companycalendar', views.companycalendar , name = 'companycalendar'),
    path('applyleave', views.applyleave , name = 'applyleave')
]
