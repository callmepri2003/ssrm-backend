from django.urls import include, path

from .views import *

urlpatterns = [
    path('dashboard/', dashboard_view, name='tutors-dashboard'),
    path('calendar/', calendar_view),
    path('create-lesson/', create_lesson, name='create_lesson'),
] 