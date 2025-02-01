from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator
from django.core.cache import cache

class FAQ(models.Model):
    question = RichTextField() # for english inpt
    answer = RichTextField()

    question_hi = models.TextField(blank=True, null=True) # this is for hindi
    question_be = models.TextField(blank=True, null=True) # this is for bengali

    def save(self, *args, **kwargs):
        """ Automatically translate the question to Hindi and Bengali before saving. """
        translator = Translator()

        # Only translate if question exists
        if self.question:
            if not self.question_hi:
                self.question_hi = translator.translate(self.question, dest="hi").text

            if not self.question_be:
                self.question_be = translator.translate(self.question, dest="be").text

        super().save(*args, **kwargs)

    def get_translated_question(self, lang="en"):
        """ Get the translated question dynamically from cache or database """
        cache_key = f"faq_{self.id}_question_{lang}"
        cached_translation = cache.get(cache_key)

        if cached_translation:
            return cached_translation

        translation = getattr(self, f"question_{lang}", self.question)
        cache.set(cache_key, translation, timeout=86400)
        return translation

    def __str__(self):
        return self.question  # Show English question in Django Admin

# Create your models here.
