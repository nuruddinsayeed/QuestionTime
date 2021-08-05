from rest_framework import serializers
from questions.models import Answer, Question


class AnswerSerializer(serializers.ModelSerializer):
    """Serializes Answer model"""

    author = serializers.StringRelatedField(read_only=True)
    # this serializer method field takes method if not given it will call
    # get_<field_name> and also by default it is read_only = True
    created_at = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    user_has_voted = serializers.SerializerMethodField()

    class Meta:
        model = Answer
        exclude = ["question", "voters", "updated_at"]

    def get_created_at(self, instance):
        """Return created at field in american date time format"""
        return instance.created_at.strftime("%B %d %Y")  # %B->Month %d->day th

    def get_like_count(self, instance):
        """Return total likes of the Answer"""
        return instance.voters.count()

    def get_user_has_voted(self, instance):
        """Return if current user has voted for the answer"""
        request = self.context.get("request")
        return instance.voters.filter(pk=request.user.pk).exists()


class QuestionSerializer(serializers.ModelSerializer):
    """Serializes Question Model"""

    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    slug = serializers.SlugField(read_only=True)
    answer_count = serializers.SerializerMethodField()
    user_has_answered = serializers.SerializerMethodField()

    class Meta:
        model = Question
        exclude = ["updated_at", ]

    def get_created_at(self, instance):
        """Return created at field in american date time format"""
        return instance.created_at.strftime("%B %d %Y")  # %B->Month %d->day th

    def get_answer_count(self, instance):
        """return the number of total answer"""
        return instance.answers.count()

    def get_user_has_answered(self, instance):
        """Return if user has answered the question"""
        request = self.context.get("request")
        return instance.answers.filter(author=request.user).exists()
