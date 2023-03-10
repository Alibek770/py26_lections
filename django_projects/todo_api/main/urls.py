from django.urls import path

from main import views

# from . import views
# from .views import task_detail_view

urlpatterns = [
    # class urls
    path('tasks/', views.TaskListCreateView.as_view()),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view()),




    # path('tasks/', views.tasks_list), # id не нужно GET
    # path('tasks/<int:pk>/', views.task_detail), # id нужно GET
    # path('tasks-create/', views.task_create), # id не нужно POST
    # path('tasks-update/<int:pk>/', views.task_update), # id нужно put/patch
    # path('tasks-delete/<int:pk>/', views.task_delete),# id нужно DELETE
]

#api/v1/books GET - list POST - create
# api/v1/books/<id> GET - detail PUT/PATCH - update DELETE - delete
