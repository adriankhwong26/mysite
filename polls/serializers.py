from rest_framework import serializers

from .models import Question, Choice

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'choice_text', 'votes']
    # id = serializers.IntegerField()
    # choice_text = serializers.CharField(max_length=200)
    # votes = serializers.DecimalField(max_digits=3, decimal_places=2)


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'question_text_with_q', 'pub_date']
    # id = serializers.IntegerField()
    # question_text = serializers.CharField(max_length=200)
    question_text_with_q = serializers.SerializerMethodField(method_name='add_question_mark')

    def add_question_mark(self, question: Question):
        return question.question_text+'?'
