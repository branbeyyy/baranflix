from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "list"),
    path('update_movie/<str:pk>', views.updateMovie, name = "update_movie"),
    path('delete/<str:pk>', views.deleteMovie, name = "delete")
]