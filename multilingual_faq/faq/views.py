from rest_framework import generics
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer
from django.http import HttpResponse

class FAQListView(generics.ListAPIView): #this lists the faqs at "url/faqs"
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def list(self, request, *args, **kwargs):
        lang = request.query_params.get("lang", "en")  # Get language from request
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True, context={"lang": lang})
        return Response(serializer.data)

#this acts as homepage at base url
def home_view(request):
    return HttpResponse("<h1 >Welcome to the FAQ System</h1><p>Visit <a href='/api/faqs/'>FAQs</a></p>")
