from django.urls import path
from . import views
from .views import QuizListView, quiz_view, quiz_data_view, save_quiz_view

app_name = 'quizes'

urlpatterns = [
    path('<reg_number>/', QuizListView, name='main-view'),
    path('<reg_number>/<pk>/', quiz_view, name='quiz-view'),
    path('<reg_number>/<pk>/save/', save_quiz_view, name='save-view'),
    path('<reg_number>/<pk>/data/', quiz_data_view, name='quiz-data-view'),
]