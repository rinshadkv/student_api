from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_student),
    path('add-student', views.add_student),
    path('update-student', views.update_student),
    path('delete-student', views.delete_student),




]

