from django.urls import path,include
from source.API.user import *
from source.API.task import *


user_urlpattern = [
    path('list/',UserListApi.as_view(),name = 'list-user'),
    path('<int:pk>/detail/',UserRetrieveApi.as_view(),name = 'detail-user'),
    path('create/',UserCreateApi.as_view(),name = 'user-create'),
    path('<int:pk>/delete/',UserDeleteApi.as_view(),name = 'delete-user'),
    path('<int:pk>/update/',UserUpdateApi.as_view(),name= 'update-user'),
    path('login/',UserLoginApi.as_view(),name = 'user-login'),

]

task_urlpattern = [ 
    path('list/',TaskListApi.as_view(),name='list-task'),
    path('<int:pk>/detail/',TaskRetrieveApi.as_view(),name='detail-user'),
    path('create/',TaskCreateApi.as_view(),name='task-create'),
    path('<int:pk>/update/',TaskUpdateApi.as_view(),name='task-update'),
    path('<int:pk>/delete/',TaskDeleteApi.as_view(),name='task-delete')
]


source_urlparttern = [ 
    path('user/',include((user_urlpattern,'user'))),
    path('task/',include((task_urlpattern,'task'))),
]