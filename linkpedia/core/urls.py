from django.urls import path

from .views import (
    home,
    login,
    logout,
    create,
    update,
    delete,
    list_links,
    edit_links,
    delete_links
)

urlpatterns = [

    path(
        '',
        home,
        name='home'
    ),

    path(
        'login/',
        login,
        name='login'
    ),

    path(
        'logout/',
        logout,
        name='logout'
    ),

    path(
        'create/',
        create,
        name='create'
    ),

    path(
        'update/<int:id>/',
        update,
        name='update'
    ),

    path(
        'delete/<int:id>/',
        delete,
        name='delete'
    ),

    path(
'list/',
list_links,
name='list'
),
    
    path(
    'edit/',
    edit_links,
    name='edit'
),

path(
    'delete-list/',
    delete_links,
    name='delete_list'
),
]
