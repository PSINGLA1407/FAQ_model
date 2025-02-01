from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    translated_question = serializers.SerializerMethodField()
    translated_answer = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        fields = ["id", "translated_question", "translated_answer"]

    def get_translated_question(self, obj):
        lang = self.context.get("lang", "en")
        translation = obj.get_translated_content("question", lang)
        return translation if translation else obj.question  # Fallback to original question if empty

    def get_translated_answer(self, obj):
        lang = self.context.get("lang", "en")
        translation = obj.get_translated_content("answer", lang)
        return translation if translation else obj.answer  # Fallback to original answer if empty
