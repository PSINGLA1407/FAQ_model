from django.contrib import admin
from django.db import models
from ckeditor.widgets import CKEditorWidget
from .models import FAQ

class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "question_hi", "question_bn")  # Display fields in admin
    search_fields = ("question",)  # Enable search by question

    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},  # Enables CKEditor for TextFields
        models.CharField: {'widget': CKEditorWidget()},  # Enables CKEditor for CharFields (if needed)
    }

admin.site.register(FAQ, FAQAdmin)  # Register the FAQ model
