from django.urls import path, include
from rest_framework.routers import DefaultRouter

from questions.api import views as question_views

router = DefaultRouter()
router.register(r"questions", question_views.QuestionViewSet)

urlpatterns = [
    path("", include(router.urls))
]
