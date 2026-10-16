from rest_framework import serializers
from Repository.models import QuestionsDb




class QuestionSerialoizer(serializers.Serializer):

        title = serializers.CharField(max_length =100)
        language =serializers.ChoiceField(choices=QuestionsDb.LANGUAGE_CHOICES, default ="python")
        difficulty_levels = serializers.ChoiceField(choices=QuestionsDb.DIFFICULTY_CHOICES, default= "easy")
        topic = serializers.CharField(max_length=200)
        notes =serializers.CharField()
        published_date = serializers.DateTimeField(read_only=True)
        sample_input = serializers.CharField()
        sample_output = serializers.CharField()
        is_active = serializers.BooleanField(default=True)
        score = serializers.IntegerField()
