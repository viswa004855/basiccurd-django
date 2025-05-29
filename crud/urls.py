from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_student, name='create_student'),
    path('',views.read_students, name='read_students'),
    path('update/<str:student_id>/',views.update_students, name='update_students'),
    path('delete/<str:student_id>/',views.delete_student, name='delete_student'),
]