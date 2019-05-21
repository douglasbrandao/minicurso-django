from django.contrib import admin
from django.urls import path

from todo_list import views

urlpatterns = [
    path('todo/', views.todoView, name='index'),
    path('addTodo/', views.addTodo, name='addTodo'),
    path('deleteTodo/<int:id>', views.deleteTodo, name='deleteTodo'),
]