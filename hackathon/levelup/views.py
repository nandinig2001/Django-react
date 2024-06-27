from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import action
from rest_framework.response import Response
from .utils import generate_summary 
from .models import NewsArticle
from .serializers import NewsArticleSerializer
from rest_framework import viewsets

class NewsArticleViewSet(viewsets.ModelViewSet):
    queryset = NewsArticle.objects.all()
    serializer_class = NewsArticleSerializer

    # @action(detail=True, methods=['post'])
    # def summarize(self, request, pk=None):
    #     article = self.get_object()
    #     article.summary = generate_summary(article.content)
    #     article.save()
    #     serializer = self.get_serializer(article)
    #     return Response(serializer.data)