from django.urls import path, include
from rest_framework.routers import DefaultRouter

from questions.api import views as question_views

router = DefaultRouter()
router.register(r"questions", question_views.QuestionViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "questions/<slug:slug>/answers/",
        question_views.AnswerListApiView.as_view(),
        name="answers-list"
    ),
    path(
        "questions/<slug:slug>/answer/",
        question_views.AnswerCreateAPIView.as_view(),
        name="answer_create"
    ),
    path(
        "answers/<int:pk>/",
        question_views.AnswerRUDAPIView.as_view(),
        name="answer_detail"
    ),
    path(
        "answers/<int:pk>/like/",
        question_views.AnswerLikeAPIView.as_view(),
        name="answer_like"
    ),
]
