from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator
from django.core.cache import cache
import re

class FAQ(models.Model):
    question = models.TextField()  # Use plain text for better translation
    answer = RichTextField()  # Use WYSIWYG editor for rich text answers

    question_hi = models.TextField(blank=True, null=True)  #  Hindi translation
    question_bn = models.TextField(blank=True, null=True)  # Bengali translation

    answer_hi = RichTextField(blank=True, null=True)  # Hindi translated answer
    answer_bn = RichTextField(blank=True, null=True)  # Bengali translated answer

    def save(self, *args, **kwargs):
        translator = Translator()

        # Function to remove unwanted HTML & special characters
        def clean_text(text):
            text = re.sub(r'<.*?>', '', text)  # Remove HTML tags
            text = text.replace("&nbsp;", " ")  # Fix non-breaking spaces
            return text.strip()

        try:
            # Ensure translations for questions
            if self.question:
                self.question_hi = translator.translate(self.question, dest="hi").text
                self.question_bn = translator.translate(self.question, dest="bn").text

            # Ensure translations for answers
            if self.answer:
                clean_answer = clean_text(self.answer)
                self.answer_hi = translator.translate(clean_answer, dest="hi").text
                self.answer_bn = translator.translate(clean_answer, dest="bn").text

        except Exception as e:
            print(f"Translation Error: {e}")  # Catch errors and print

        super().save(*args, **kwargs)

    def get_translated_content(self, field_name, lang="en"):
        """ Fetch translated question/answer dynamically """
        cache_key = f"faq_{self.id}_{field_name}_{lang}"
        cached_translation = cache.get(cache_key)

        if cached_translation:
            return cached_translation  # Use cached translation if available

        # Fetch the translated field if available, else return the original
        translation = getattr(self, f"{field_name}_{lang}", getattr(self, field_name, ""))
        cache.set(cache_key, translation, timeout=86400)  # Cache for 24 hours
        return translation

    def __str__(self):
        return self.question  # Show English question in Django Admin
