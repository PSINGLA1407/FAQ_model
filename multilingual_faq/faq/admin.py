from django.contrib import admin
from .models import FAQ

class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "question_hi", "question_be")  # Display fields in admin
    search_fields = ("question",)  # Enable search by question

admin.site.register(FAQ, FAQAdmin)  # Register the FAQ model
