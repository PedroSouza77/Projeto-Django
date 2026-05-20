from django.urls import path

from .views import (
    home,
    login,
    logout,
    create,
    update,
    delete
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
]