from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from questions.api.serializers import QuestionSerializer, AnswerSerializer
from questions.models import Question, Answer
from questions.api.permissions import IsAuthenticatedOrReadOnly


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    lookup_field = "slug"
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AnswerCreateAPIView(generics.CreateAPIView):
    """Create Answer for specific question"""

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        """Overriding create default create method"""

        request_user = self.request.user
        kwarg_slug = self.kwargs.get("slug")
        question = get_object_or_404(Question, slug=kwarg_slug)

        if question.answers.filter(author=request_user).exists():
            raise ValidationError("You Already Have Answered this Question!!")

        serializer.save(author=request_user, question=question)


class AnswerListApiView(generics.ListAPIView):
    """Return all answers for specifiq quesiton"""

    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        """Overriding default get query method"""

        kwarg_slug = self.kwargs.get("slug")
        return Answer.objects.filter(question__slug=kwarg_slug).order_by("-created_at")
