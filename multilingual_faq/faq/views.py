from rest_framework import generics
from rest_framework.response import Response
from django.http import HttpResponse
from .models import FAQ
from .serializers import FAQSerializer
from django.shortcuts import render

class FAQListView(generics.ListAPIView):  # Lists the FAQs at "url/api/faqs/"
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["lang"] = self.request.query_params.get("lang", "en")  # Default to English
        return context

# homeapage at base url
def home_view(request):
    return HttpResponse(
        "<h1>Welcome to the FAQ System</h1>"
        "<p>Visit <a href='/api/faqs/'>FAQs</a></p>"
    )

def faq_list_view(request):
    return render(request, "faq_list.html")