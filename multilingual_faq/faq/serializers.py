from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    translated_question = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        fields = ["id", "translated_question", "answer"]

    def get_translated_question(self, obj):
        lang = self.context.get("lang", "en")
        return obj.get_translated_question(lang)
