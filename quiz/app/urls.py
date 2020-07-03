from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/', startQuiz, name='start-quiz'),
    path('update_question/', updateQuestion, name='update-question'),
    path('update_choice/', updateChoice, name='update-choice')
]